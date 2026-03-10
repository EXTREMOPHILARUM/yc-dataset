# Technical Specs

## Table of Contents

1. [Overview](#1-overview)
2. [Core Features](#2-core-features)
3. [User Flows](#3-user-flows)
4. [Tech Stack](#4-tech-stack)
5. [Project Structure](#5-project-structure)
6. [Database Schema](#6-database-schema)
7. [API Routes](#7-api-routes)
8. [Pages & UI](#8-pages--ui)
9. [Authentication](#9-authentication)
10. [Implementation Notes](#10-implementation-notes)
11. [Environment Variables](#11-environment-variables)
12. [Getting Started](#12-getting-started)

---

## 1. Overview

20n is a cloud-hosted SaaS platform that accepts a target molecule as input and returns ranked biosynthetic pathway predictions validated through automated cloud lab integration. The system serves two primary user types: **research scientists** at mid-market specialty chemical companies ($50M–$500M revenue) who design and submit pathway predictions, and **project managers** who track validation results and manage the molecule pipeline across their organization.

The architecture follows an event-driven monolith pattern deployed on AWS ECS, with a separate worker tier for computationally intensive pathway scoring and cloud lab orchestration. This avoids premature microservice complexity while keeping the compute-heavy prediction pipeline decoupled from the request-response web tier. Background jobs are critical — pathway prediction runs take 5–30 minutes per molecule, and cloud lab validation cycles take 3–14 days, requiring robust async job management and webhook-based result ingestion.

Scale targets for the first 18 months: 50 concurrent users across 10–15 customer organizations, ~500 pathway predictions per month, ~2TB of protein structure and enzyme kinetics reference data, and a p95 API latency of <200ms for synchronous endpoints (prediction submissions and result retrieval, not the predictions themselves).

---

## 2. Core Features

### Pathway Prediction Engine
- **Molecule input and parsing** `[MVP]`: Accept target molecules via SMILES string, InChI, or common name lookup against PubChem. Validate input, resolve to canonical structure, display 2D structure preview.
- **Pathway prediction** `[MVP]`: Generate ranked biosynthetic routes from substrate (glucose) to target molecule by traversing KEGG/MetaCyc/BRENDA reaction databases. Score each route by: literature evidence (BioGPT-mined), AlphaFold2-predicted enzyme structural compatibility, and host organism expression likelihood.
- **Pathway visualization** `[MVP]`: Interactive reaction network graph showing each enzymatic step, candidate enzymes, and confidence scores. Expandable nodes for enzyme details and literature references.
- **DNA design generation** `[MVP]`: For selected pathways, generate codon-optimized DNA insertion sequences for target host organisms (E. coli K-12 MG1655 and S. cerevisiae S288C).

### Cloud Lab Integration
- **Automated validation submission** `[MVP]`: Submit DNA designs programmatically to Emerald Cloud Lab API for robotic construction, transformation, and fermentation. Track submission status and estimated completion time.
- **Result ingestion** `[MVP]`: Receive validation results via webhook — mass spectrometry confirmation of target molecule production, yield measurements, growth curves. Auto-update pathway confidence scores based on experimental results.
- **Iteration management** `[v2]`: Suggest pathway modifications based on failed validations — alternative enzymes, codon optimization tweaks, promoter strength adjustments — and auto-submit the next design iteration.

### Project Workspace
- **Multi-molecule projects** `[MVP]`: Organize work by customer engagement. Each project contains target molecules, pathway predictions, submitted designs, and validation results in a unified timeline view.
- **IP and regulatory flagging** `[MVP]`: Automatically query Google Patents API and EPA TSCA/EU REACH databases for each target molecule and biosynthetic intermediates. Display flags inline on pathway results.
- **Export and reporting** `[v2]`: Generate PDF reports for customer stakeholders summarizing pathway predictions, validation results, and IP landscape. Include methodology appendix for regulatory submissions.

---

## 3. User Flows

### Flow 1: First Pathway Prediction (Onboarding → Aha Moment)
1. User signs up via email invitation from admin, lands on `/onboarding` with a guided setup wizard
2. User selects their default host organism (E. coli or S. cerevisiae) and enters their Emerald Cloud Lab API credentials
3. User is redirected to `/projects` (empty state) and clicks "New Project," enters project name and target molecule (SMILES string or searches by common name)
4. System validates the molecule, displays 2D structure preview, and shows "Predict Pathways" button
5. User clicks "Predict Pathways" — system shows progress indicator with estimated time (5–30 min), user can navigate away
6. Notification appears when prediction completes. User clicks through to pathway results: ranked list of 3–10 biosynthetic routes with confidence scores
7. User expands top pathway to see the reaction network graph, enzyme details, and literature citations — this is the aha moment: a complete biosynthetic route they didn't have to design manually
8. User clicks "Generate DNA Design" on the top pathway, reviews the codon-optimized sequence, and clicks "Submit to Cloud Lab"

### Flow 2: Validation Result Review (Core Value Loop)
1. Emerald Cloud Lab webhook fires when fermentation results are ready (3–14 days after submission)
2. System processes results, updates pathway confidence scores, sends email notification to project members
3. User opens `/projects/:id/validations/:id` — sees mass spec confirmation (detected/not detected), yield measurement, growth curve chart
4. If target molecule detected: pathway status updates to "Validated," confidence score increases, user can export results
5. If not detected: system highlights likely failure points (expression level, enzyme activity, toxicity) and suggests modifications with "Re-submit Modified Design" button

### Flow 3: IP Conflict Resolution (Edge Case)
1. User submits a new molecule. Pathway prediction completes with 5 routes.
2. Route #1 (highest confidence) shows a red "Patent Flag" badge — system found an active patent covering one of the intermediate enzymatic steps
3. User clicks the flag to see patent details: patent number, holder, filing date, relevant claims, and expiry date
4. Routes #2 and #3 show green "Clear" badges — no known IP conflicts
5. User selects route #2 instead and proceeds with DNA design submission, noting the IP rationale in the project log

---

## 4. Tech Stack

### Frontend
- **Next.js 14 (App Router)** — Server components for the data-heavy pathway results pages; client components for the interactive reaction network graph. Incremental adoption of RSC reduces client bundle size for the large visualization library.
- **Tailwind CSS + shadcn/ui** — Rapid UI development with consistent design tokens. shadcn provides the data tables, command palette, and sheet components used throughout.
- **D3.js** — Pathway reaction network visualization. No suitable React wrapper handles the custom force-directed graph layout needed for enzymatic pathway display.

### Backend
- **Python 3.12 + FastAPI** — The bioinformatics ecosystem (BioPython, RDKit, ESM) is Python-native. FastAPI provides async request handling for the webhook-heavy architecture and auto-generates OpenAPI docs for customer API integrations.
- **Celery + Redis** — Background task queue for pathway prediction jobs (5–30 min compute) and cloud lab submission orchestration. Redis as both broker and result backend.
- **BioPython + RDKit** — Molecule parsing, SMILES/InChI conversion, sequence manipulation. RDKit for cheminformatics, BioPython for protein sequence handling.

### Database
- **PostgreSQL 16** — JSONB columns for flexible pathway result storage (varying numbers of steps, enzymes, scores per route). PostGIS not needed, but the JSONB indexing handles the semi-structured bioinformatics data well.
- **Redis 7** — Celery broker, session cache, and real-time notification pub/sub for pathway prediction progress updates.

### Infrastructure
- **AWS ECS Fargate** — Container orchestration without cluster management. Separate task definitions for web tier, worker tier, and scheduled jobs. Auto-scaling worker tier based on Celery queue depth.
- **AWS RDS (PostgreSQL)** — Managed database with automated backups, point-in-time recovery, and read replicas when needed.
- **AWS S3** — Storage for reference datasets (KEGG, MetaCyc, BRENDA dumps, AlphaFold2 structure cache), validation result files (mass spec raw data, growth curves), and generated PDF reports.
- **AWS CloudWatch + Sentry** — CloudWatch for infrastructure metrics and ECS log aggregation. Sentry for application error tracking with Celery integration for worker error visibility.
- **GitHub Actions** — CI/CD pipeline: lint, test, build Docker images, deploy to staging, manual promotion to production.

### External APIs / Services
- **Emerald Cloud Lab API** — Programmatic submission of DNA designs for robotic construction and fermentation. Webhook-based result delivery.
- **ESMFold API (Meta)** — Protein structure prediction for enzyme compatibility scoring. Fallback to local ESM-2 model for batch processing.
- **PubChem PUG REST API** — Molecule name-to-SMILES resolution and compound property lookup.
- **Google Patents API** — Patent landscape search for target molecules and biosynthetic intermediates.
- **Resend** — Transactional email for validation result notifications, weekly project digests, and invitation emails.
- **Stripe** — Subscription billing (platform access) and metered billing (per-molecule project fees).

---

## 5. Project Structure

```
20n/
├── apps/
│   ├── web/                          # Next.js 14 frontend
│   │   ├── src/
│   │   │   ├── app/                  # App Router pages and layouts
│   │   │   │   ├── (auth)/           # Login, signup, onboarding routes
│   │   │   │   ├── (dashboard)/      # Authenticated app routes
│   │   │   │   └── api/              # Next.js API routes (BFF for auth)
│   │   │   ├── components/
│   │   │   │   ├── pathway/          # Reaction network graph, pathway cards
│   │   │   │   ├── molecule/         # Structure viewer, SMILES input
│   │   │   │   └── ui/              # shadcn/ui components
│   │   │   └── lib/                  # API client, auth helpers, formatters
│   │   └── next.config.js
│   │
│   └── api/                          # FastAPI backend
│       ├── src/
│       │   ├── routes/               # API route handlers
│       │   │   ├── projects.py
│       │   │   ├── pathways.py
│       │   │   ├── validations.py
│       │   │   └── webhooks.py       # Emerald Cloud Lab callbacks
│       │   ├── services/             # Business logic layer
│       │   │   ├── prediction.py     # Pathway prediction orchestration
│       │   │   ├── scoring.py        # AlphaFold2 + literature scoring
│       │   │   ├── dna_design.py     # Codon optimization + sequence generation
│       │   │   ├── cloud_lab.py      # Emerald Cloud Lab API client
│       │   │   └── ip_check.py       # Patent + regulatory search
│       │   ├── models/               # SQLAlchemy models
│       │   ├── tasks/                # Celery task definitions
│       │   │   ├── predict.py        # Pathway prediction task
│       │   │   ├── submit_lab.py     # Cloud lab submission task
│       │   │   └── ip_scan.py        # IP flagging background task
│       │   ├── db/
│       │   │   ├── migrations/       # Alembic migrations
│       │   │   └── seed.py           # Reference data seeding
│       │   └── lib/                  # Shared utilities, config
│       ├── tests/
│       └── pyproject.toml
│
├── packages/
│   └── shared/                       # Shared types (TypeScript + Python via openapi-generator)
│       └── openapi.yaml              # API spec, source of truth for both sides
│
├── data/                             # Reference datasets (gitignored, downloaded on setup)
│   ├── kegg/
│   ├── metacyc/
│   └── brenda/
│
├── docker-compose.yml                # Local dev: postgres, redis, api, web, worker
├── Dockerfile.api
├── Dockerfile.web
├── Makefile                          # Common commands: setup, dev, test, migrate
└── .github/
    └── workflows/
        ├── ci.yml                    # Lint, test, build on PR
        └── deploy.yml                # Deploy to staging/production
```

---

## 6. Database Schema

```sql
-- Organizations (customer companies)
CREATE TABLE organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  stripe_customer_id VARCHAR(255),
  subscription_tier VARCHAR(50) NOT NULL DEFAULT 'starter', -- starter, professional, enterprise
  default_host_organism VARCHAR(50) NOT NULL DEFAULT 'e_coli_k12',
  emerald_api_key_encrypted BYTEA, -- encrypted at rest, decrypted in worker only
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Users within organizations
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES organizations(id),
  email VARCHAR(255) NOT NULL UNIQUE,
  full_name VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL DEFAULT 'member', -- admin, member, viewer
  password_hash VARCHAR(255), -- null if OAuth-only
  onboarding_completed BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_users_org ON users(organization_id);
CREATE INDEX idx_users_email ON users(email);

-- Projects group molecules for a customer engagement
CREATE TABLE projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES organizations(id),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(50) NOT NULL DEFAULT 'active', -- active, completed, archived
  created_by UUID NOT NULL REFERENCES users(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_projects_org ON projects(organization_id);

-- Target molecules within projects
CREATE TABLE molecules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES projects(id),
  name VARCHAR(255), -- common name if resolved
  smiles VARCHAR(2000) NOT NULL, -- canonical SMILES string
  inchi VARCHAR(2000), -- InChI identifier
  pubchem_cid BIGINT, -- PubChem compound ID if resolved
  molecular_weight DECIMAL(10,4),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_molecules_project ON molecules(project_id);
CREATE INDEX idx_molecules_smiles ON molecules(smiles);

-- Predicted biosynthetic pathways for a molecule
CREATE TABLE pathways (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  molecule_id UUID NOT NULL REFERENCES molecules(id),
  rank INTEGER NOT NULL, -- 1 = highest confidence
  confidence_score DECIMAL(5,4) NOT NULL, -- 0.0000–1.0000
  status VARCHAR(50) NOT NULL DEFAULT 'predicted', -- predicted, design_generated, submitted, validated, failed
  route_data JSONB NOT NULL, -- array of enzymatic steps: [{enzyme_id, ec_number, reaction, substrate, product, score}]
  literature_score DECIMAL(5,4), -- BioGPT literature evidence score
  structural_score DECIMAL(5,4), -- AlphaFold2 enzyme compatibility score
  expression_score DECIMAL(5,4), -- host organism expression likelihood
  host_organism VARCHAR(50) NOT NULL,
  ip_flags JSONB DEFAULT '[]', -- [{patent_id, status, claims, expiry_date}]
  regulatory_flags JSONB DEFAULT '[]', -- [{database, substance, status}]
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_pathways_molecule ON pathways(molecule_id);
CREATE INDEX idx_pathways_status ON pathways(status);

-- DNA designs generated for a pathway
CREATE TABLE dna_designs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  pathway_id UUID NOT NULL REFERENCES pathways(id),
  sequence TEXT NOT NULL, -- full codon-optimized DNA sequence
  host_organism VARCHAR(50) NOT NULL,
  codon_table VARCHAR(50) NOT NULL, -- codon optimization table used
  gc_content DECIMAL(5,4),
  sequence_length INTEGER NOT NULL,
  iteration INTEGER NOT NULL DEFAULT 1, -- tracks design iterations after failed validations
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_dna_designs_pathway ON dna_designs(pathway_id);

-- Cloud lab validation submissions and results
CREATE TABLE validations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  dna_design_id UUID NOT NULL REFERENCES dna_designs(id),
  emerald_experiment_id VARCHAR(255), -- Emerald Cloud Lab experiment reference
  status VARCHAR(50) NOT NULL DEFAULT 'pending', -- pending, submitted, in_progress, completed, failed, cancelled
  submitted_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  target_detected BOOLEAN, -- mass spec confirmation
  yield_mg_per_l DECIMAL(10,4), -- production yield
  growth_curve_data JSONB, -- time-series OD600 readings
  mass_spec_file_url VARCHAR(1000), -- S3 URL to raw mass spec data
  raw_results JSONB, -- full Emerald API response
  failure_analysis JSONB, -- system-generated analysis if target not detected
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_validations_design ON validations(dna_design_id);
CREATE INDEX idx_validations_status ON validations(status);
CREATE INDEX idx_validations_emerald ON validations(emerald_experiment_id);
```

---

## 7. API Routes

### Authentication
- `POST /api/v1/auth/register` — Create account via invitation token. Body: { email, password, invitation_token }. Returns: 201 + user + session token.
- `POST /api/v1/auth/login` — Email/password login. Body: { email, password }. Returns: 200 + session token.
- `POST /api/v1/auth/refresh` — Refresh session token. Body: { refresh_token }. Returns: 200 + new token pair.
- `POST /api/v1/auth/logout` — Invalidate session. Returns: 204.
- `GET /api/v1/auth/me` — Get current user profile. Returns: 200 + user with organization.

### Organizations
- `GET /api/v1/organizations/:id` — Get organization details and settings. Returns: 200 + organization.
- `PATCH /api/v1/organizations/:id` — Update organization settings (host organism, Emerald API key). Returns: 200 + updated org. Admin only.
- `POST /api/v1/organizations/:id/invite` — Send email invitation to join org. Body: { email, role }. Returns: 201. Admin only.
- `GET /api/v1/organizations/:id/members` — List organization members. Returns: 200 + paginated user list.

### Projects
- `POST /api/v1/projects` — Create project. Body: { name, description }. Returns: 201 + project.
- `GET /api/v1/projects` — List projects for current organization. Query: ?status, ?page, ?limit. Returns: 200 + paginated list with molecule counts.
- `GET /api/v1/projects/:id` — Get project with summary stats (molecules, predictions, validations). Returns: 200 + project.
- `PATCH /api/v1/projects/:id` — Update project name/description/status. Returns: 200 + updated project.
- `DELETE /api/v1/projects/:id` — Archive project (soft delete). Returns: 204.

### Molecules
- `POST /api/v1/projects/:id/molecules` — Add target molecule to project. Body: { smiles } or { name } (resolved via PubChem). Returns: 201 + molecule with 2D structure URL.
- `GET /api/v1/projects/:id/molecules` — List molecules in project. Returns: 200 + list with prediction status summary.
- `GET /api/v1/molecules/:id` — Get molecule details with all pathways. Returns: 200 + molecule + pathways.

### Pathways
- `POST /api/v1/molecules/:id/predict` — Start pathway prediction (async). Returns: 202 + { job_id, estimated_time }. Triggers Celery task.
- `GET /api/v1/molecules/:id/pathways` — List predicted pathways ranked by confidence. Returns: 200 + pathway list.
- `GET /api/v1/pathways/:id` — Get pathway detail including reaction steps, scores, and IP flags. Returns: 200 + full pathway.
- `POST /api/v1/pathways/:id/design` — Generate DNA design for pathway. Returns: 201 + dna_design with sequence and metadata.

### Validations
- `POST /api/v1/designs/:id/validate` — Submit DNA design to Emerald Cloud Lab (async). Returns: 202 + { validation_id, estimated_completion }.
- `GET /api/v1/designs/:id/validations` — List validation attempts for a design. Returns: 200 + validation list.
- `GET /api/v1/validations/:id` — Get validation result details. Returns: 200 + validation with results.
- `POST /api/v1/webhooks/emerald` — Emerald Cloud Lab result webhook. Validates HMAC signature, processes results, triggers notification. Returns: 200.

### Jobs & Status
- `GET /api/v1/jobs/:id` — Check async job status (prediction, validation). Returns: 200 + { status, progress_pct, estimated_remaining }.

### Billing
- `POST /api/v1/billing/checkout` — Create Stripe checkout session for subscription. Returns: 200 + { checkout_url }.
- `POST /api/v1/webhooks/stripe` — Stripe webhook for subscription events. Returns: 200.
- `GET /api/v1/billing/usage` — Current billing period usage (molecule count, validation count). Returns: 200 + usage summary.

### Health
- `GET /api/v1/health` — API health check. Returns: 200 + { status, db, redis, celery_workers }.

---

## 8. Pages & UI

### Public Pages
- `/` — Landing page. Hero with molecule structure animation, value proposition ("Target molecule → validated pathway in weeks"), feature grid (3 cards: Predict, Validate, Ship), pricing section, CTA to request demo.
- `/pricing` — Pricing tiers: Starter ($2K/mo, 5 molecules), Professional ($8K/mo, 25 molecules + cloud lab), Enterprise (custom). Feature comparison table.
- `/login` — Email/password form with "Request Access" link (no self-signup, invitation only).
- `/signup/:token` — Invitation-based registration. Pre-filled email from invitation token.

### Authenticated Pages
- `/onboarding` — 3-step wizard: (1) Select default host organism, (2) Enter Emerald Cloud Lab API credentials, (3) Create first project. Progress bar at top.
- `/projects` — Project list as card grid. Each card shows: project name, molecule count, active validations, last activity. Empty state: "Create your first project" CTA with illustration.
- `/projects/:id` — Project dashboard. Tab layout:
  - **Molecules** tab: Table of target molecules with status badges (predicted, validating, validated). Click row to expand pathway summary.
  - **Timeline** tab: Chronological activity feed — predictions completed, validations submitted, results received.
  - **Reports** tab [v2]: Generated PDF reports for stakeholders.
- `/projects/:id/molecules/:id` — Molecule detail. Split pane: left shows ranked pathway list with confidence scores and IP flag badges; right shows interactive reaction network graph (D3.js force-directed). Selecting a pathway updates the graph. Action buttons: "Generate DNA Design," "Submit to Cloud Lab."
- `/projects/:id/validations/:id` — Validation result page. Status header (pending/in-progress/completed/failed). Results section: mass spec confirmation badge (detected/not detected), yield measurement with unit, growth curve line chart. If failed: system-generated failure analysis with suggested modifications.
- `/settings` — Organization settings. Sections: team members (invite/remove), Emerald API credentials, default organism, billing (redirect to Stripe portal).

### Admin Pages
- `/admin/organizations` — Internal admin only. Table of all customer organizations with usage stats, subscription tier, last activity. Used for customer success monitoring.

---

## 9. Authentication

- **Auth method:** Email/password with invitation-only registration. No self-signup — new users receive an email invitation from their organization admin containing a single-use signup token. This matches the B2B enterprise sales model where the account is provisioned during onboarding.
- **Provider:** Custom implementation using FastAPI + python-jose for JWT. Auth is simple enough (no social login, no SSO in MVP) that a third-party service adds cost without value. SSO/SAML is a v2 feature for enterprise tier.
- **Session management:** JWT access tokens (15 min expiry) + refresh tokens (7 day expiry, stored in httpOnly cookie). Access token passed via Authorization header for API requests. Refresh rotation: each refresh issues a new refresh token and invalidates the old one.
- **Roles and permissions:**
  - **admin**: Full access. Invite/remove members, manage billing, update org settings, CRUD all projects.
  - **member**: Create projects, run predictions, submit validations, view all org projects.
  - **viewer**: Read-only access to all org projects and results. Cannot trigger predictions or validations.
- **API authentication:** Organization-level API keys for programmatic access (v2). Scoped to specific operations (read-only, predict, full-access). HMAC-SHA256 signature verification for incoming webhooks (Emerald, Stripe).

---

## 10. Implementation Notes

- **Reference data bootstrapping:** KEGG, MetaCyc, and BRENDA databases must be downloaded and indexed before the prediction engine works. Total ~2TB uncompressed. Use a one-time setup script (`make seed-reference-data`) that downloads, parses, and loads into PostgreSQL + builds a local search index. This takes 4–6 hours on first run. In production, pre-built AMI/Docker image includes the indexed data.
- **AlphaFold2/ESMFold rate limits:** The public ESMFold API (Meta) is rate-limited to ~100 requests/minute. For batch pathway scoring (which may evaluate 50+ enzymes per molecule), use a local ESM-2 model running on GPU. Budget one g4dn.xlarge instance ($0.526/hr) for the worker tier, falling back to CPU-only scoring (slower, 10x longer) if GPU is unavailable.
- **Emerald Cloud Lab API quirks:** Experiment submission is synchronous but result delivery is exclusively via webhook (no polling endpoint). Webhook payloads can arrive days after submission and are not idempotent — implement deduplication using `experiment_id + result_timestamp` as a composite key. Webhook HMAC uses SHA-256 with the API key as the secret.
- **SMILES canonicalization:** Different SMILES representations of the same molecule (e.g., `c1ccccc1` vs `C1=CC=CC=C1` for benzene) must resolve to the same canonical form. Use RDKit's `Chem.MolToSmiles(Chem.MolFromSmiles(input), canonical=True)` on every molecule input before storage or comparison.
- **Pathway prediction caching:** Two molecules requesting the same intermediate pathway steps should reuse cached sub-routes. Key cache entries by `(substrate_smiles, product_smiles, host_organism)` tuple. Redis with 24-hour TTL for intermediate results, PostgreSQL for validated pathway results (permanent).
- **Celery task design:** Pathway prediction must be idempotent and resumable — if a worker crashes mid-prediction, the task should pick up from the last completed step. Store intermediate state in Redis with the task ID. Use `acks_late=True` and `reject_on_worker_lost=True` for reliable redelivery.
- **Testing strategy:** Heavy testing on: (1) SMILES parsing and canonicalization (fuzz with random valid/invalid SMILES), (2) pathway scoring math (golden test set of 20 known pathways with expected scores), (3) webhook processing (replay captured Emerald payloads). Light testing on: UI components, admin pages, billing integration (use Stripe test mode).
- **Deployment pipeline:** PR → GitHub Actions (lint + test + build) → merge to main → auto-deploy to staging → manual promotion to production via GitHub Environment approval. Database migrations run automatically on deploy using Alembic with a pre-deploy hook. Zero-downtime deploys via ECS rolling update (min 1 healthy task).

---

## 11. Environment Variables

### App Configuration
- `APP_ENV` — Environment: development, staging, production (required)
- `APP_PORT` — API server port, default 8000 (optional)
- `APP_URL` — Public-facing URL for webhooks and email links (required)
- `FRONTEND_URL` — Next.js app URL, used for CORS and email links (required)
- `SECRET_KEY` — Application secret for JWT signing and encryption (required)
- `ENCRYPTION_KEY` — 256-bit key for encrypting customer API credentials at rest (required)

### Database
- `DATABASE_URL` — PostgreSQL connection string, e.g., `postgresql://user:pass@host:5432/twentyn` (required)
- `REDIS_URL` — Redis connection string for Celery broker and cache (required)

### Authentication
- `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` — Access token expiry, default 15 (optional)
- `JWT_REFRESH_TOKEN_EXPIRE_DAYS` — Refresh token expiry, default 7 (optional)

### External APIs
- `EMERALD_API_BASE_URL` — Emerald Cloud Lab API base URL (required)
- `EMERALD_WEBHOOK_SECRET` — HMAC secret for verifying Emerald webhooks (required)
- `ESMFOLD_API_URL` — ESMFold API endpoint, default public Meta API (optional)
- `PUBCHEM_API_BASE_URL` — PubChem PUG REST API, default `https://pubchem.ncbi.nlm.nih.gov/rest/pug` (optional)
- `GOOGLE_PATENTS_API_KEY` — Google Patents API key for IP flagging (required)
- `STRIPE_SECRET_KEY` — Stripe API key for billing (required)
- `STRIPE_WEBHOOK_SECRET` — Stripe webhook signature verification (required)
- `RESEND_API_KEY` — Resend API key for transactional email (required)
- `RESEND_FROM_EMAIL` — Sender email address, e.g., `noreply@20n.com` (required)

### Infrastructure
- `AWS_S3_BUCKET` — S3 bucket for file storage (required)
- `AWS_REGION` — AWS region, default us-east-1 (optional)
- `SENTRY_DSN` — Sentry error tracking DSN (required in staging/production)

### Feature Flags
- `ENABLE_CLOUD_LAB_SUBMISSION` — Enable live Emerald Cloud Lab submissions, default false in dev (optional)
- `ENABLE_GPU_SCORING` — Use GPU-accelerated ESM-2 model for scoring, default false (optional)

---

## 12. Getting Started

### Prerequisites
- Python 3.12+
- Node.js 20+
- PostgreSQL 16+
- Redis 7+
- Docker and Docker Compose (for local dev)
- Make

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/20n/platform.git && cd platform
   ```

2. Copy environment files:
   ```bash
   cp apps/api/.env.example apps/api/.env
   cp apps/web/.env.example apps/web/.env
   ```

3. Configure required environment variables in both `.env` files. For local dev, most external API keys can use test/sandbox values. Set `ENABLE_CLOUD_LAB_SUBMISSION=false` to skip Emerald integration.

4. Start infrastructure services:
   ```bash
   docker-compose up -d postgres redis
   ```

5. Install backend dependencies and run migrations:
   ```bash
   cd apps/api
   pip install -e ".[dev]"
   alembic upgrade head
   python -m src.db.seed  # Seeds a test organization + user
   ```

6. Install frontend dependencies:
   ```bash
   cd apps/web
   npm install
   ```

7. Start the development servers (from project root):
   ```bash
   make dev  # Starts API (port 8000), web (port 3000), and Celery worker
   ```

8. Download reference data (first time only — takes 4–6 hours):
   ```bash
   make seed-reference-data  # Downloads KEGG, MetaCyc, BRENDA
   ```
   For development without reference data, use `MOCK_PREDICTION=true` in `.env` to return fixture pathway results.

### Verify It's Working
- [ ] Open `http://localhost:3000` — login page loads
- [ ] Log in with seed credentials: `test@20n.dev` / `testpassword`
- [ ] Complete onboarding wizard (skip Emerald API key)
- [ ] Create a project and add a molecule (try `CC(=O)Nc1ccc(O)cc1` — acetaminophen)
- [ ] Click "Predict Pathways" — with `MOCK_PREDICTION=true`, results appear in ~5 seconds
- [ ] API health check: `curl http://localhost:8000/api/v1/health` returns `{"status": "ok"}`
