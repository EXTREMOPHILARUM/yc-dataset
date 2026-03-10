"""
Validate that dataset updates only grow — no data loss.

Compares current raw/ and data/ against the previous git commit to ensure:
1. Raw JSON record counts don't decrease
2. Raw JSON files don't shrink significantly
3. No companies are removed from the index
4. No files are removed from existing companies
5. No markdown files shrink significantly (>20% smaller)

Exit code 0 = pass, 1 = validation failure.
"""

import json
import subprocess
import sys
from pathlib import Path

RAW_DIR = Path("raw")
DATA_DIR = Path("data")
SHRINK_THRESHOLD = 0.20  # Flag if file shrinks by more than 20%

RAW_FILES = {
    "raw/yc_directory.json": "slug",
    "raw/yc_details.json": "slug",
    "raw/startups_rip.json": "slug",
}


def git_show(path: str) -> str | None:
    """Get file contents from the previous commit."""
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    return result.stdout


def get_previous_file_sizes(prefix: str) -> dict[str, int]:
    """Get file paths and sizes from the previous commit under a prefix."""
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--long", "HEAD", prefix],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return {}

    files = {}
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        parts = line.split()
        size = int(parts[3])
        path = parts[4]
        files[path] = size
    return files


def validate_raw_jsons(issues: list, warnings: list):
    """Validate raw JSON files haven't lost data."""
    print("Validating raw JSON files...")

    for raw_path, key_field in RAW_FILES.items():
        current_path = Path(raw_path)
        if not current_path.exists():
            issues.append(f"Missing raw file: {raw_path}")
            continue

        current_data = json.load(open(current_path))
        current_count = len(current_data)
        current_slugs = {r.get(key_field, "") for r in current_data if isinstance(r, dict)}
        current_errors = sum(1 for r in current_data if isinstance(r, dict) and "error" in r)

        prev_content = git_show(raw_path)
        if prev_content is None:
            print(f"  {raw_path}: {current_count} records (new file)")
            continue

        prev_data = json.loads(prev_content)
        prev_count = len(prev_data)
        prev_slugs = {r.get(key_field, "") for r in prev_data if isinstance(r, dict)}
        prev_errors = sum(1 for r in prev_data if isinstance(r, dict) and "error" in r)

        # Check record count
        if current_count < prev_count:
            issues.append(
                f"{raw_path}: record count decreased {prev_count} → {current_count}"
            )

        # Check for removed slugs
        removed_slugs = prev_slugs - current_slugs
        if removed_slugs:
            issues.append(
                f"{raw_path}: {len(removed_slugs)} slugs removed: "
                f"{', '.join(sorted(removed_slugs)[:10])}"
            )

        # Check error count didn't increase significantly
        if current_errors > prev_errors and current_errors > prev_errors + 5:
            warnings.append(
                f"{raw_path}: error count increased {prev_errors} → {current_errors}"
            )

        # Check file size
        prev_size = len(prev_content.encode())
        curr_size = current_path.stat().st_size
        if prev_size > 0 and curr_size < prev_size:
            shrink_pct = (prev_size - curr_size) / prev_size
            if shrink_pct > SHRINK_THRESHOLD:
                issues.append(
                    f"{raw_path}: file shrunk by {shrink_pct:.0%} "
                    f"({prev_size:,} → {curr_size:,} bytes)"
                )

        added = current_count - prev_count
        print(f"  {raw_path}: {current_count} records ({'+' if added >= 0 else ''}{added}), "
              f"{current_errors} errors")


def validate_index(issues: list):
    """Validate no companies removed from index."""
    print("Validating index...")

    index_path = DATA_DIR / "index.json"
    if not index_path.exists():
        issues.append("data/index.json not found")
        return {}, {}

    current_index = {e["slug"]: e for e in json.load(open(index_path))}

    prev_content = git_show("data/index.json")
    if prev_content is None:
        print(f"  {len(current_index)} companies (new index)")
        return current_index, {}

    previous_index = {e["slug"]: e for e in json.loads(prev_content)}

    removed = set(previous_index) - set(current_index)
    if removed:
        issues.append(
            f"Index: {len(removed)} companies removed: {', '.join(sorted(removed)[:10])}"
        )

    if len(current_index) < len(previous_index):
        issues.append(
            f"Index: company count decreased {len(previous_index)} → {len(current_index)}"
        )

    added = len(current_index) - len(previous_index)
    print(f"  {len(current_index)} companies ({'+' if added >= 0 else ''}{added})")
    return current_index, previous_index


def validate_markdown_files(issues: list, warnings: list):
    """Validate no markdown files removed or shrunk."""
    print("Validating markdown files...")

    previous_files = get_previous_file_sizes("data/")
    if not previous_files:
        return

    current_files = {}
    for p in DATA_DIR.rglob("*"):
        if p.is_file():
            current_files[str(p)] = p.stat().st_size

    removed_count = 0
    shrunk_count = 0

    for prev_path, prev_size in previous_files.items():
        if prev_path == "data/index.json":
            continue

        if prev_path not in current_files:
            parts = prev_path.split("/")
            if len(parts) >= 4:  # data/batch/slug/file.md
                removed_count += 1
                if removed_count <= 10:
                    issues.append(f"File removed: {prev_path}")
            continue

        curr_size = current_files[prev_path]
        if prev_size > 0 and curr_size < prev_size:
            shrink_pct = (prev_size - curr_size) / prev_size
            if shrink_pct > SHRINK_THRESHOLD:
                shrunk_count += 1
                if shrunk_count <= 10:
                    issues.append(
                        f"File shrunk by {shrink_pct:.0%}: {prev_path} "
                        f"({prev_size} → {curr_size} bytes)"
                    )
            elif shrink_pct > 0.05:
                warnings.append(
                    f"File slightly smaller ({shrink_pct:.0%}): {prev_path}"
                )

    if removed_count > 10:
        issues.append(f"  ...and {removed_count - 10} more files removed")
    if shrunk_count > 10:
        issues.append(f"  ...and {shrunk_count - 10} more files shrunk")

    print(f"  {len(current_files)} files, {removed_count} removed, {shrunk_count} shrunk")


def validate():
    issues = []
    warnings = []

    validate_raw_jsons(issues, warnings)
    validate_index(issues)
    validate_markdown_files(issues, warnings)

    # Report
    if warnings:
        print(f"\n⚠ {len(warnings)} warnings:")
        for w in warnings:
            print(f"  {w}")

    if issues:
        print(f"\n✗ {len(issues)} validation failures:")
        for issue in issues:
            print(f"  {issue}")
        return 1

    print("\n✓ All validations passed")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
