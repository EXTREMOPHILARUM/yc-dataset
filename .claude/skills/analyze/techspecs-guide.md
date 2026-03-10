# Technical Specs Guide

Write as `# Technical Specs`. This is a realistic system architecture document for rebuilding the company TODAY. It should be specific enough that a senior engineer could use it to scaffold the project and start building.

The tech stack and architecture must match what was described in the Build Plan's MVP features. If the build plan says "cloud lab API integration," the tech specs must include the API routes, database tables, and implementation notes for that integration.

---

## Section 1: Table of Contents (## Table of Contents)

Numbered list of all 12 sections:
```
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
```

---

## Section 2: Overview (## 1. Overview)

**Length:** 2-3 paragraphs

**Cover:**
- What the system does in technical terms (not business terms — that's the build plan)
- Primary user types/roles and what each does in the system
- Deployment model: cloud-hosted SaaS, self-hosted, hybrid, desktop, mobile, CLI
- Key architectural pattern: monolith, microservices, serverless, event-driven — pick one and justify
- Scale targets: expected concurrent users, data volume (GB/TB), request throughput (RPS), latency requirements

**Checklist:**
- [ ] Deployment model is stated
- [ ] Architectural pattern is chosen with rationale
- [ ] Scale targets are quantified

---

## Section 3: Core Features (## 2. Core Features)

**Format:** Bullet list grouped by category

```
### Category Name
- **Feature name:** 1-2 sentences with enough specificity to write a JIRA ticket. Include input, processing, and output.
- **Feature name:** ...

### Category Name
- ...
```

**Requirements:**
- 6-10 features total across 2-4 categories
- Mark each as `[MVP]` or `[v2]`
- Each description should answer: what does the user do, what does the system do, what's the output?
- No vague features like "analytics dashboard" — specify WHAT analytics: "Real-time pathway success rate dashboard showing validation results per design iteration, filterable by organism, target molecule, and date range"

**Checklist:**
- [ ] Every MVP feature from the build plan is represented
- [ ] Each feature is specific enough to estimate engineering effort
- [ ] MVP vs. v2 is clearly marked

---

## Section 4: User Flows (## 3. User Flows)

**Format:** 2-4 primary flows as numbered step lists

```
### Flow Name (e.g., "First-Time Pathway Design")
1. User lands on [page/screen] and sees [what]
2. User clicks/enters [action] on [element]
3. System [processes/displays/sends]
4. User sees [result] and can [next action]
...
```

**Required flows:**
- **Onboarding/first use:** New user → first value moment. This is the most important flow.
- **Core value loop:** The primary repeated action that delivers value
- **Key edge case:** A flow that handles failure, error, or empty state gracefully

**Checklist:**
- [ ] Each step names a specific page/component/action
- [ ] The "aha moment" is identifiable in the core flow
- [ ] Edge cases are addressed (empty state, error, waiting state)

---

## Section 5: Tech Stack (## 4. Tech Stack)

**Format:** Organized by layer with justifications

```
### Frontend
- **[Technology]** — 1 sentence justification

### Backend
- **[Technology]** — 1 sentence justification

### Database
- **[Technology]** — 1 sentence justification

### Infrastructure
- **[Technology]** — 1 sentence justification

### External APIs / Services
- **[Service]** — what it's used for
```

**Rules:**
- Be opinionated. Pick ONE option per slot, don't say "React or Vue."
- Prefer widely-adopted, well-documented technologies with active maintenance
- Justify each choice in terms of THIS product's requirements, not generically
- If the product has unusual requirements (real-time, heavy computation, specific compliance), the stack should reflect that
- Include monitoring/observability tools

**Checklist:**
- [ ] Every layer has a concrete choice
- [ ] Justifications reference this product's specific needs
- [ ] No deprecated or unmaintained technologies
- [ ] Infrastructure includes CI/CD, monitoring, and hosting

---

## Section 6: Project Structure (## 5. Project Structure)

**Format:** Directory tree, 2-3 levels deep

```
project-root/
├── apps/
│   ├── web/                    # Next.js frontend
│   │   ├── src/
│   │   │   ├── app/            # App router pages
│   │   │   ├── components/     # UI components
│   │   │   └── lib/            # Client utilities
│   │   └── ...
│   └── api/                    # Backend service
│       ├── src/
│       │   ├── routes/         # API route handlers
│       │   ├── services/       # Business logic
│       │   ├── models/         # Database models
│       │   └── lib/            # Shared utilities
│       └── ...
├── packages/
│   └── shared/                 # Shared types, validators
├── docker-compose.yml
└── ...
```

**Rules:**
- Use monorepo (Turborepo/Nx) for full-stack apps, polyrepo only if services are truly independent
- Show key directories with 1-line inline comments explaining purpose
- The structure must match the tech stack chosen in section 5
- Include config files (docker-compose, CI config) at the root level

**Checklist:**
- [ ] Structure matches the chosen tech stack
- [ ] Key directories have explanatory comments
- [ ] Both frontend and backend are represented
- [ ] Config and infra files are included

---

## Section 7: Database Schema (## 6. Database Schema)

**Format:** SQL CREATE TABLE statements in code blocks

```sql
-- Core entity: brief explanation of what this table represents
CREATE TABLE table_name (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  field_name TYPE NOT NULL,
  foreign_key UUID REFERENCES other_table(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Index for common query pattern
CREATE INDEX idx_table_field ON table_name(field_name);
```

**Requirements:**
- 4-8 core tables covering the essential data model
- Use PostgreSQL syntax (most common for new projects)
- Include: primary keys (UUID preferred), foreign keys with references, NOT NULL constraints, default values, timestamps
- Add indexes for columns used in WHERE clauses and JOINs
- Brief comment above each table explaining its purpose
- Include at least one enum type if applicable

**Do NOT include:**
- Every junction table for many-to-many relationships (just note them in comments)
- Audit/log tables (mention in implementation notes)
- Migration files (just the target schema)

**Checklist:**
- [ ] All entities from the core features have corresponding tables
- [ ] Foreign key relationships are correct
- [ ] Indexes cover the primary query patterns
- [ ] Schema could be copy-pasted into psql and would run

---

## Section 8: API Routes (## 7. API Routes)

**Format:** Grouped by resource

```
### Resource Name
- `POST /api/v1/resource` — Create a new resource. Body: { field1, field2 }. Returns: 201 + created resource.
- `GET /api/v1/resource` — List resources with pagination. Query: ?page, ?limit, ?filter. Returns: 200 + paginated list.
- `GET /api/v1/resource/:id` — Get single resource. Returns: 200 + resource or 404.
- `PATCH /api/v1/resource/:id` — Update resource fields. Body: { field1? }. Returns: 200 + updated resource.
- `DELETE /api/v1/resource/:id` — Soft-delete resource. Returns: 204.
```

**Requirements:**
- 15-25 endpoints covering the full MVP
- Include for each: HTTP method, path, brief description, key request/response details
- Group by resource (users, projects, [domain-specific entities])
- Must include: auth endpoints (register, login, logout, refresh), health check, webhook endpoints if applicable
- Use RESTful conventions: plural nouns, nested resources for relationships
- Version the API: `/api/v1/`

**Checklist:**
- [ ] Every core feature from section 3 has corresponding API endpoints
- [ ] Auth endpoints are included
- [ ] Pagination is specified for list endpoints
- [ ] Response codes are mentioned for key endpoints
- [ ] Webhook/callback endpoints included if the product has async operations

---

## Section 9: Pages & UI (## 8. Pages & UI)

**Format:** Grouped by access level

```
### Public Pages
- `/` — Landing page with value proposition, pricing, CTA. Hero section, feature grid, testimonials.
- `/pricing` — Pricing tiers with feature comparison table.
- `/login` — Email/password + OAuth login form.
- `/signup` — Registration with email verification.

### Authenticated Pages
- `/dashboard` — Overview of active projects with key metrics. Card grid layout.
- `/projects/:id` — Project detail view with tabs for [specific sections].
...

### Admin Pages (if applicable)
- `/admin/users` — User management table with search, filter, role assignment.
...
```

**Requirements:**
- Every page has a route path and 1-2 sentences describing purpose and key UI elements
- Name specific UI patterns: "card grid," "data table with sort/filter," "multi-step form wizard," "split-pane with list and detail"
- Include empty states and loading states for key pages
- Match pages to the user flows from section 4

**Checklist:**
- [ ] Every user flow step has a corresponding page
- [ ] Key UI patterns are named (not just "a page that shows X")
- [ ] Public, authenticated, and admin sections are separated

---

## Section 10: Authentication (## 9. Authentication)

**Length:** 3-5 bullet groups

**Cover:**
- **Auth method:** What strategy fits this product? OAuth2 + email/password for B2C, SSO/SAML for B2B enterprise, API keys for developer tools. Pick what fits.
- **Provider:** Name a specific auth service (Clerk, Auth0, Supabase Auth, NextAuth, Lucia) or describe custom implementation.
- **Session management:** JWT vs. session cookies, token refresh strategy, expiry times.
- **Authorization model:** RBAC roles and what each can do. Name the roles and their permissions.
- **API authentication:** How external API consumers authenticate (API keys, OAuth tokens, webhook signatures).

**Checklist:**
- [ ] Auth method matches the product type (B2B vs B2C vs developer tool)
- [ ] A specific provider is chosen
- [ ] Roles and permissions are defined
- [ ] Both UI auth and API auth are covered

---

## Section 11: Implementation Notes (## 10. Implementation Notes)

**Format:** 5-10 bullet points

**Required topics:**
- **Critical gotchas:** Things that will bite you if you don't know about them upfront. Specific to this product — rate limits on key APIs, data format quirks, regulatory requirements.
- **Performance:** Where are the performance bottlenecks? What needs caching, queueing, or optimization?
- **Background jobs:** What work happens asynchronously? Job queue technology choice.
- **Data migration:** If replacing an existing system, how is data migrated? If greenfield, what seed data is needed?
- **Testing strategy:** What to test heavily (core business logic, integrations) vs. what's lower priority (UI layout, admin pages). Name specific testing tools.
- **Deployment pipeline:** How does code go from PR to production? Staging environment?

**Checklist:**
- [ ] At least one gotcha specific to a third-party API used
- [ ] Background job processing is addressed
- [ ] Testing approach names specific tools/frameworks

---

## Section 12: Environment Variables (## 11. Environment Variables)

**Format:** Grouped list

```
### App Configuration
- `NODE_ENV` — Environment: development, staging, production (required)
- `PORT` — Server port, default 3000 (optional)
- `APP_URL` — Public-facing URL for callbacks and links (required)

### Database
- `DATABASE_URL` — PostgreSQL connection string (required)

### Authentication
- `AUTH_SECRET` — Session encryption key (required)
- `GOOGLE_CLIENT_ID` — OAuth client ID (required for Google login)
- `GOOGLE_CLIENT_SECRET` — OAuth client secret (required for Google login)

### External APIs
- `STRIPE_SECRET_KEY` — Stripe API key for billing (required)
- `STRIPE_WEBHOOK_SECRET` — Stripe webhook verification (required)
...
```

**Requirements:**
- Every external service from the tech stack has corresponding env vars
- Mark each as (required) or (optional) with defaults for optional ones
- Group by: app config, database, auth, external APIs, feature flags
- Do NOT include actual values or example secrets

**Checklist:**
- [ ] Every external service in the tech stack has env vars listed
- [ ] Required vs. optional is marked for each
- [ ] No actual secrets or example values included

---

## Section 13: Getting Started (## 12. Getting Started)

**Format:** Step-by-step numbered list

```
### Prerequisites
- Node.js 20+
- PostgreSQL 15+
- [Other tools]

### Setup
1. Clone the repository: `git clone ...`
2. Install dependencies: `npm install` (or equivalent)
3. Copy environment file: `cp .env.example .env`
4. Configure required environment variables (see section 11)
5. Set up database: `npm run db:migrate && npm run db:seed`
6. Start development server: `npm run dev`
7. Open `http://localhost:3000` — you should see [specific thing]

### Verify It's Working
- [ ] Landing page loads at localhost:3000
- [ ] Can create an account and log in
- [ ] [Core feature] works: try [specific action]
```

**Requirements:**
- Prerequisites with specific version requirements
- 5-10 concrete steps with copy-pasteable commands
- Commands must match the tech stack (don't say `npm` if the stack uses `bun`)
- Include a verification section so devs know when setup is complete
- Mention seed data if applicable

**Checklist:**
- [ ] Prerequisites list specific versions
- [ ] Commands are copy-pasteable
- [ ] Verification steps confirm core functionality works
- [ ] Commands match the chosen tech stack
