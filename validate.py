"""
Validate that dataset updates only grow — no data loss.

Compares current data/ against the previous git commit to ensure:
1. No companies are removed
2. No files are removed from existing companies
3. No files shrink significantly (>20% smaller)

Exit code 0 = pass, 1 = validation failure.
"""

import json
import subprocess
import sys
from pathlib import Path

DATA_DIR = Path("data")
SHRINK_THRESHOLD = 0.20  # Flag if file shrinks by more than 20%


def get_previous_file_list() -> dict[str, int]:
    """Get file paths and sizes from the previous commit."""
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--long", "HEAD", "data/"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return {}  # No previous commit or no data/ in it

    files = {}
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        # Format: mode type hash size\tpath
        parts = line.split()
        size = int(parts[3])
        path = parts[4]
        files[path] = size
    return files


def get_previous_index() -> dict[str, dict]:
    """Get index.json from the previous commit."""
    result = subprocess.run(
        ["git", "show", "HEAD:data/index.json"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return {}
    entries = json.loads(result.stdout)
    return {e["slug"]: e for e in entries}


def validate():
    issues = []
    warnings = []

    # Load current index
    index_path = DATA_DIR / "index.json"
    if not index_path.exists():
        print("FAIL: data/index.json not found")
        return 1

    current_index = {e["slug"]: e for e in json.load(open(index_path))}
    previous_index = get_previous_index()

    # Check 1: No companies removed
    if previous_index:
        removed = set(previous_index) - set(current_index)
        if removed:
            issues.append(f"{len(removed)} companies removed: {', '.join(sorted(removed)[:10])}")

        # Check company count didn't decrease
        if len(current_index) < len(previous_index):
            issues.append(
                f"Company count decreased: {len(previous_index)} → {len(current_index)}"
            )

    # Check 2: No files removed from existing companies
    previous_files = get_previous_file_list()
    if previous_files:
        current_files = {}
        for p in DATA_DIR.rglob("*"):
            if p.is_file():
                rel = str(p)
                current_files[rel] = p.stat().st_size

        for prev_path, prev_size in previous_files.items():
            if prev_path == "data/index.json":
                continue

            if prev_path not in current_files:
                # Check if this is a company file (not just index)
                parts = prev_path.split("/")
                if len(parts) >= 4:  # data/batch/slug/file.md
                    issues.append(f"File removed: {prev_path}")
                continue

            # Check 3: Files don't shrink significantly
            curr_size = current_files[prev_path]
            if prev_size > 0 and curr_size < prev_size:
                shrink_pct = (prev_size - curr_size) / prev_size
                if shrink_pct > SHRINK_THRESHOLD:
                    issues.append(
                        f"File shrunk by {shrink_pct:.0%}: {prev_path} "
                        f"({prev_size} → {curr_size} bytes)"
                    )
                elif shrink_pct > 0.05:
                    warnings.append(
                        f"File slightly smaller ({shrink_pct:.0%}): {prev_path}"
                    )

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

    added = len(current_index) - len(previous_index) if previous_index else len(current_index)
    print(f"✓ Validation passed: {len(current_index)} companies ({'+' if added >= 0 else ''}{added})")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
