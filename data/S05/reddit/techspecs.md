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

## 1. Overview

The system is a community discussion platform where users create topic-based communities (subreddits), submit text/link posts, vote on content, and comment in threaded discussions. An AI-powered search layer (Reddit Answers) provides LLM-generated summaries from community content. A self-serve advertising platform enables interest-targeted ad delivery based on subreddit membership.

Three primary user types: **Users** (browse, post, vote, comment), **Moderators** (manage community rules, approve/remove content, ban users), and **Advertisers** (create campaigns, target communities, track conversions). An **Admin** role handles platform-wide moderation and user management.

Deployment: cloud-hosted SaaS on AWS, single-region initially (us-east-1) with CDN edge caching. Architectural pattern: modular monolith in Python (FastAPI) with a React frontend — a monolith avoids premature microservice complexity while the modular structure (separate modules for posts, comments, voting, communities, ads, search) allows future extraction. Scale targets: 100K DAU at launch, 10K concurrent WebSocket connections, 500 RPS average / 2K RPS peak, <200ms p95 API latency, 50GB initial database with 10GB/month growth.

## 2. Core Features

### Community Management
- **Create subreddit** `[MVP]`: User creates a community with name, description, rules, and visual settings. System validates name uniqueness and generates URL slug. Output: live community page with mod tools.
- **Moderator tools** `[MVP]`: Mod queue (reported/flagged content), user ban/mute, post removal with reason, AutoMod-style rule engine (regex-based content filters, account age requirements). Input: moderator actions; output: enforcement applied, action logged.
- **Community wiki** `[v2]`: Collaborative markdown pages per subreddit, editable by approved users. Version history with diff view.

### Content & Voting
- **Submit post** `[MVP]`: Text post (markdown) or link post with optional thumbnail. User selects target subreddit, adds title (required) and flair (optional). System validates against community rules, renders markdown, generates preview.
- **Threaded comments** `[MVP]`: Nested comment threads with collapsible branches, markdown support, and vote counts. Comments load lazily below a configurable depth threshold (default: 3 levels, then "load more").
- **Voting system** `[MVP]`: Upvote/downvote on posts and comments. Real-time vote count updates via WebSocket. Ranking algorithm: Wilson score interval for comments, hot-rank (score × time-decay) for post feeds. Computed in Redis sorted sets, persisted to PostgreSQL.
- **Media uploads** `[v2]`: Image and video hosting (S3 + CloudFront), embedded in posts. Image processing via Sharp (resize, thumbnail generation).

### AI Search
- **Reddit Answers** `[MVP]`: Natural-language search bar that returns LLM-generated answer with cited source comments/posts. RAG pipeline: query → embedding → vector similarity search → context assembly → LLM summarization → response with attribution links. Multi-language via LLM translation.
- **Semantic search** `[MVP]`: Vector search across all indexed posts and comments. Returns ranked results with relevance scores and snippet previews.

### Advertising
- **Campaign creation** `[MVP]`: Advertiser creates campaign with budget, date range, targeting (subreddit interests, geography), and ad creative (promoted post format). Self-serve dashboard with campaign wizard.
- **Ad delivery** `[MVP]`: Promoted posts inserted into subreddit feeds at configurable frequency (1 per 25 organic posts). Real-time auction for ad placement based on bid and relevance score.
- **Analytics dashboard** `[MVP]`: Impressions, clicks, CTR, spend, conversions (via pixel tracking). Exportable reports.

## 3. User Flows

### First-Time User → First Value Moment
1. User lands on `/` (homepage) and sees a curated feed of popular posts across communities, plus a search bar for Reddit Answers
2. User types a question into Reddit Answers search bar (e.g., "best budget headphones 2026")
3. System returns an AI-generated answer with citations linking to specific community discussions
4. User clicks a citation link and lands on a post/comment thread in a subreddit
5. User sees a prompt: "Join this community to vote and comment" → clicks "Sign up"
6. User creates account (email + password or Google OAuth) and is auto-subscribed to the subreddit they arrived from
7. User upvotes the helpful comment and sees their home feed populated with posts from their first subscribed community

### Core Value Loop: Browse → Vote → Comment → Return
1. User opens `/home` and sees a feed of posts from subscribed subreddits, sorted by "hot" (default)
2. User scrolls, reads posts, upvotes/downvotes — vote counts update in real-time via WebSocket
3. User opens a post, reads threaded comments, and adds their own comment (markdown editor with preview)
4. User receives a notification when someone replies to their comment → returns to the thread
5. User discovers new subreddits via "Trending Communities" sidebar or Reddit Answers → subscribes → feed expands

### Advertiser: Campaign Creation
1. Advertiser signs up at `/advertiser` and completes business verification (company name, billing)
2. Advertiser clicks "New Campaign" → multi-step wizard: objective (awareness/traffic/conversions), budget ($5/day minimum), schedule, targeting (select subreddit interest categories + geography)
3. Advertiser creates ad creative: promoted post format with title, body, link, and optional image
4. System shows preview of how the ad appears in a subreddit feed
5. Advertiser submits → ad enters review queue (manual review for first campaign, automated thereafter)
6. Campaign goes live → advertiser monitors impressions/clicks/spend on `/advertiser/dashboard`

### Edge Case: Empty Community
1. Moderator creates a new subreddit with no posts yet
2. System displays an empty state: "This community is brand new! Be the first to post." with a prominent "Create Post" CTA
3. Sidebar shows community description, rules, and a "Share this community" link
4. If Reddit Answers returns results from this community, they link back to actual posts — no empty-state answers

## 4. Tech Stack

### Frontend
- **Next.js 15 (App Router)** — Server-side rendering for SEO (critical: every post and comment must be indexable), React Server Components for reduced client JS, streaming for fast initial loads

### Backend
- **FastAPI (Python 3.12)** — High-performance async Python framework; matches Reddit's Python heritage, excellent for ML/AI integrations (Reddit Answers RAG pipeline), strong typing with Pydantic

### Database
- **PostgreSQL 16** — Primary relational store for all structured data (users, posts, comments, communities, votes). Proven at Reddit-scale; supports JSONB for flexible metadata, full-text search for basic queries
- **Redis 7 (Valkey)** — Real-time vote counts (sorted sets), session cache, rate limiting (sliding window), hot post rankings, WebSocket pub/sub
- **Pinecone** — Vector database for Reddit Answers RAG pipeline; managed service eliminates operational overhead of self-hosted vector DB

### Infrastructure
- **AWS (ECS Fargate)** — Container orchestration without managing EC2 instances; auto-scaling based on CPU/memory
- **S3 + CloudFront** — Static assets, media uploads, CDN edge caching for global latency reduction
- **GitHub Actions** — CI/CD pipeline: lint → test → build → deploy to staging → manual promotion to production
- **Datadog** — APM, logging, metrics, and alerting; critical for diagnosing voting system latency and ad delivery performance
- **Celery + Redis** — Background job processing for: embedding generation, notification delivery, ad auction computation, moderation rule evaluation

### External APIs / Services
- **OpenAI API (text-embedding-3-large + GPT-4o)** — Embedding generation for vector search; LLM summarization for Reddit Answers
- **Clerk** — Authentication provider (OAuth, email/password, SSO); handles session management and user metadata
- **Stripe** — Advertiser billing: campaign budgets, usage-based billing, invoicing
- **Resend** — Transactional email: verification, notifications, weekly digest
- **Sentry** — Error tracking and performance monitoring

## 5. Project Structure

```
reddit-rebuild/
├── apps/
│   ├── web/                        # Next.js 15 frontend
│   │   ├── src/
│   │   │   ├── app/                # App Router pages and layouts
│   │   │   │   ├── (public)/       # Landing, login, signup
│   │   │   │   ├── (feed)/         # Home feed, subreddit pages
│   │   │   │   ├── (post)/         # Post detail, comment threads
│   │   │   │   ├── (advertiser)/   # Advertiser dashboard
│   │   │   │   └── (admin)/        # Admin panel
│   │   │   ├── components/         # Shared UI components
│   │   │   │   ├── post/           # PostCard, VoteButton, CommentThread
│   │   │   │   ├── community/      # SubredditHeader, Sidebar, RulesList
│   │   │   │   └── search/         # AnswerCard, SearchResults
│   │   │   └── lib/                # Client utilities, API client, hooks
│   │   └── next.config.ts
│   └── api/                        # FastAPI backend
│       ├── src/
│       │   ├── modules/
│       │   │   ├── posts/          # Post CRUD, ranking, feed generation
│       │   │   ├── comments/       # Comment CRUD, threading, voting
│       │   │   ├── communities/    # Subreddit CRUD, moderation, rules
│       │   │   ├── votes/          # Vote processing, ranking updates
│       │   │   ├── search/         # RAG pipeline, vector search, Reddit Answers
│       │   │   ├── ads/            # Campaign CRUD, auction, delivery, analytics
│       │   │   ├── notifications/  # Push, email, in-app notifications
│       │   │   └── auth/           # Clerk webhook handlers, user sync
│       │   ├── core/               # Database, Redis, config, middleware
│       │   ├── workers/            # Celery tasks (embeddings, notifications, auctions)
│       │   └── main.py             # FastAPI app entrypoint
│       ├── alembic/                # Database migrations
│       └── tests/
├── packages/
│   └── shared/                     # Shared types, validators, constants
├── docker-compose.yml              # Local dev: Postgres, Redis, API, worker
├── .github/
│   └── workflows/
│       ├── ci.yml                  # Lint, test, build
│       └── deploy.yml              # Deploy to staging/production
└── turbo.json                      # Turborepo configuration
```

## 6. Database Schema

```sql
-- User profiles synced from Clerk
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  clerk_id TEXT UNIQUE NOT NULL,
  username TEXT UNIQUE NOT NULL,
  display_name TEXT,
  avatar_url TEXT,
  karma_post INTEGER NOT NULL DEFAULT 0,
  karma_comment INTEGER NOT NULL DEFAULT 0,
  is_admin BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_users_clerk_id ON users(clerk_id);
CREATE INDEX idx_users_username ON users(username);

-- Communities (subreddits)
CREATE TABLE communities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT UNIQUE NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  description TEXT,
  rules JSONB NOT NULL DEFAULT '[]',
  settings JSONB NOT NULL DEFAULT '{}',
  banner_url TEXT,
  icon_url TEXT,
  subscriber_count INTEGER NOT NULL DEFAULT 0,
  created_by UUID NOT NULL REFERENCES users(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_communities_slug ON communities(slug);
CREATE INDEX idx_communities_subscriber_count ON communities(subscriber_count DESC);

-- Community membership and roles
CREATE TYPE community_role AS ENUM ('member', 'moderator', 'admin');

CREATE TABLE community_members (
  user_id UUID NOT NULL REFERENCES users(id),
  community_id UUID NOT NULL REFERENCES communities(id),
  role community_role NOT NULL DEFAULT 'member',
  joined_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, community_id)
);

CREATE INDEX idx_community_members_community ON community_members(community_id);

-- Posts (text or link)
CREATE TYPE post_type AS ENUM ('text', 'link');

CREATE TABLE posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  body TEXT,
  url TEXT,
  post_type post_type NOT NULL DEFAULT 'text',
  author_id UUID NOT NULL REFERENCES users(id),
  community_id UUID NOT NULL REFERENCES communities(id),
  flair TEXT,
  score INTEGER NOT NULL DEFAULT 0,
  comment_count INTEGER NOT NULL DEFAULT 0,
  is_removed BOOLEAN NOT NULL DEFAULT false,
  removed_by UUID REFERENCES users(id),
  removal_reason TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_posts_community ON posts(community_id, created_at DESC);
CREATE INDEX idx_posts_author ON posts(author_id, created_at DESC);
CREATE INDEX idx_posts_score ON posts(score DESC);
-- Hot ranking computed in Redis, not indexed here

-- Threaded comments
CREATE TABLE comments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  body TEXT NOT NULL,
  author_id UUID NOT NULL REFERENCES users(id),
  post_id UUID NOT NULL REFERENCES posts(id),
  parent_id UUID REFERENCES comments(id),
  depth INTEGER NOT NULL DEFAULT 0,
  score INTEGER NOT NULL DEFAULT 0,
  is_removed BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_comments_post ON comments(post_id, created_at);
CREATE INDEX idx_comments_parent ON comments(parent_id);
CREATE INDEX idx_comments_author ON comments(author_id);

-- Votes (posts and comments unified)
CREATE TYPE vote_target AS ENUM ('post', 'comment');
CREATE TYPE vote_direction AS ENUM ('up', 'down');

CREATE TABLE votes (
  user_id UUID NOT NULL REFERENCES users(id),
  target_type vote_target NOT NULL,
  target_id UUID NOT NULL,
  direction vote_direction NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, target_type, target_id)
);

CREATE INDEX idx_votes_target ON votes(target_type, target_id);

-- Ad campaigns
CREATE TYPE campaign_status AS ENUM ('draft', 'review', 'active', 'paused', 'completed');

CREATE TABLE ad_campaigns (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  advertiser_id UUID NOT NULL REFERENCES users(id),
  name TEXT NOT NULL,
  status campaign_status NOT NULL DEFAULT 'draft',
  daily_budget_cents INTEGER NOT NULL,
  total_budget_cents INTEGER NOT NULL,
  bid_cpm_cents INTEGER NOT NULL,
  target_communities UUID[] NOT NULL DEFAULT '{}',
  target_geos TEXT[] NOT NULL DEFAULT '{}',
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  creative_title TEXT NOT NULL,
  creative_body TEXT,
  creative_url TEXT NOT NULL,
  creative_image_url TEXT,
  impressions INTEGER NOT NULL DEFAULT 0,
  clicks INTEGER NOT NULL DEFAULT 0,
  spend_cents INTEGER NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_ad_campaigns_advertiser ON ad_campaigns(advertiser_id);
CREATE INDEX idx_ad_campaigns_status ON ad_campaigns(status) WHERE status = 'active';

-- Moderation log for audit trail
CREATE TABLE mod_actions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  moderator_id UUID NOT NULL REFERENCES users(id),
  community_id UUID NOT NULL REFERENCES communities(id),
  action TEXT NOT NULL,
  target_type TEXT NOT NULL,
  target_id UUID NOT NULL,
  reason TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_mod_actions_community ON mod_actions(community_id, created_at DESC);
```

## 7. API Routes

### Authentication (Clerk webhook sync)
- `POST /api/v1/auth/webhook` — Clerk webhook handler: user.created, user.updated, user.deleted events. Syncs user data to local users table. Verified via Clerk webhook signature.
- `GET /api/v1/auth/me` — Get current authenticated user profile. Returns: 200 + user object with karma, subscriptions.

### Communities
- `POST /api/v1/communities` — Create a new subreddit. Body: { name, description, rules }. Returns: 201 + community. Creator becomes first moderator.
- `GET /api/v1/communities` — List communities with pagination. Query: ?page, ?limit, ?sort=(popular|new|alphabetical), ?search. Returns: 200 + paginated list.
- `GET /api/v1/communities/:slug` — Get community by slug. Returns: 200 + community with subscriber count, rules, moderator list, or 404.
- `PATCH /api/v1/communities/:slug` — Update community settings (moderator only). Body: { description?, rules?, settings? }. Returns: 200.
- `POST /api/v1/communities/:slug/subscribe` — Subscribe to community. Returns: 200.
- `DELETE /api/v1/communities/:slug/subscribe` — Unsubscribe. Returns: 204.
- `GET /api/v1/communities/:slug/moderators` — List moderators. Returns: 200 + user list.

### Posts
- `POST /api/v1/communities/:slug/posts` — Create post in community. Body: { title, body?, url?, post_type, flair? }. Returns: 201 + post.
- `GET /api/v1/communities/:slug/posts` — List posts in community. Query: ?sort=(hot|new|top|controversial), ?time=(hour|day|week|month|year|all), ?page, ?limit. Returns: 200 + paginated posts with vote status.
- `GET /api/v1/posts/:id` — Get single post with community context. Returns: 200 + post or 404.
- `PATCH /api/v1/posts/:id` — Edit post body (author only, within 3-hour window). Returns: 200.
- `DELETE /api/v1/posts/:id` — Soft-delete post (author or moderator). Returns: 204.
- `GET /api/v1/feed/home` — Authenticated user's home feed from subscribed communities. Query: ?sort, ?page, ?limit. Returns: 200 + paginated posts.
- `GET /api/v1/feed/popular` — Global popular feed (all communities). Query: ?sort, ?page, ?limit. Returns: 200 + paginated posts.

### Comments
- `POST /api/v1/posts/:id/comments` — Add comment to post. Body: { body, parent_id? }. Returns: 201 + comment.
- `GET /api/v1/posts/:id/comments` — Get comment tree for post. Query: ?sort=(best|new|top|controversial), ?depth_limit. Returns: 200 + nested comment tree.
- `PATCH /api/v1/comments/:id` — Edit comment (author only). Returns: 200.
- `DELETE /api/v1/comments/:id` — Soft-delete comment (author or moderator). Returns: 204.

### Voting
- `POST /api/v1/votes` — Cast or change vote. Body: { target_type, target_id, direction }. Returns: 200 + updated score. Idempotent: re-voting same direction removes vote.

### Search
- `GET /api/v1/search` — Full-text and semantic search. Query: ?q, ?type=(posts|comments|communities), ?community, ?page, ?limit. Returns: 200 + ranked results.
- `POST /api/v1/search/answers` — Reddit Answers: AI-generated summary. Body: { query, language? }. Returns: 200 + { answer, citations: [{ post_id, comment_id, snippet, url }] }. Streamed response via SSE.

### Moderation
- `GET /api/v1/communities/:slug/modqueue` — Get reported/flagged content. Returns: 200 + items pending review.
- `POST /api/v1/communities/:slug/mod/remove` — Remove post or comment. Body: { target_type, target_id, reason }. Returns: 200.
- `POST /api/v1/communities/:slug/mod/ban` — Ban user from community. Body: { user_id, reason, duration_days? }. Returns: 200.

### Advertising
- `POST /api/v1/ads/campaigns` — Create ad campaign. Body: { name, daily_budget, total_budget, bid_cpm, target_communities, target_geos, start_date, end_date, creative }. Returns: 201.
- `GET /api/v1/ads/campaigns` — List advertiser's campaigns. Returns: 200 + paginated list.
- `GET /api/v1/ads/campaigns/:id` — Get campaign with analytics. Returns: 200 + campaign + { impressions, clicks, ctr, spend }.
- `PATCH /api/v1/ads/campaigns/:id` — Update campaign (draft/paused only). Returns: 200.
- `POST /api/v1/ads/campaigns/:id/activate` — Submit campaign for review / activate. Returns: 200.
- `POST /api/v1/ads/campaigns/:id/pause` — Pause active campaign. Returns: 200.

### System
- `GET /api/v1/health` — Health check. Returns: 200 + { status, db, redis, version }.
- `POST /api/v1/webhooks/stripe` — Stripe webhook for payment events. Verified via Stripe signature.

## 8. Pages & UI

### Public Pages
- `/` — Landing page with trending posts feed, Reddit Answers search bar (hero), trending communities sidebar. Dual CTA: "Sign up" and "Browse communities."
- `/r/:slug` — Community page with post feed (card list with vote buttons, title, snippet, metadata), community sidebar (description, rules, subscriber count, moderators), sort controls (hot/new/top).
- `/r/:slug/comments/:id` — Post detail page with full post content, threaded comment tree (collapsible, lazy-loaded below depth 3), vote buttons, comment compose box.
- `/login` — Email/password form + Google OAuth button. Clerk-hosted authentication.
- `/signup` — Registration form with username selection, email verification.
- `/search` — Search results page with tabs (posts/comments/communities) and Reddit Answers card at top if query is a question.

### Authenticated Pages
- `/home` — Personalized feed from subscribed communities. Card list layout with infinite scroll, sort selector, "Create Post" floating action button.
- `/submit` — Post creation form: community selector (searchable dropdown), title, body (markdown editor with live preview) or URL input, flair selector. Two-column layout: form left, community rules right.
- `/r/:slug/wiki` — Community wiki pages with markdown rendering and edit history.
- `/notifications` — Notification list: replies, mentions, mod actions. Split into "Messages" and "Notifications" tabs.
- `/settings` — User settings: profile (display name, avatar, bio), preferences (default sort, email notifications), subscriptions list.
- `/u/:username` — User profile page: post history, comment history, karma breakdown, account age. Tab navigation.

### Advertiser Pages
- `/advertiser` — Advertiser dashboard: campaign overview cards (active/paused/completed), total spend, aggregate metrics. Data table with filters.
- `/advertiser/campaigns/new` — Multi-step campaign creation wizard: objective → budget → targeting → creative → review → submit.
- `/advertiser/campaigns/:id` — Campaign detail: real-time metrics (impressions, clicks, CTR, spend), chart timelines, creative preview, targeting summary.

### Admin Pages
- `/admin` — Admin dashboard: platform metrics (DAU, posts/day, reports pending), recent mod actions.
- `/admin/users` — User management data table: search, filter by role/status, view profile, suspend/ban.
- `/admin/reports` — Global report queue: flagged content across all communities, bulk actions.

## 9. Authentication

- **Auth method:** OAuth2 (Google) + email/password for users. API keys for data licensing partners. Stripe-authenticated advertiser billing.
- **Provider:** Clerk — handles registration, login, session management, OAuth, email verification. Clerk webhooks sync user data to local database.
- **Session management:** Clerk-managed JWTs with 1-hour expiry and automatic refresh. Session cookies (httpOnly, secure, sameSite=strict) for web. Bearer tokens for API consumers.
- **Authorization model (RBAC):**
  - **User:** Browse, post, comment, vote, subscribe, manage own profile
  - **Moderator** (per-community): All user permissions + remove content, ban users, edit community settings, manage mod queue, edit wiki
  - **Advertiser:** All user permissions + create/manage ad campaigns, view ad analytics, manage billing
  - **Admin:** All permissions + global user management, global content moderation, platform settings, view system metrics
- **API authentication:** Clerk JWT for authenticated endpoints. Webhook signature verification (HMAC-SHA256) for Clerk and Stripe webhooks. API keys (SHA-256 hashed, stored in database) for data licensing partners accessing the firehose API.

## 10. Implementation Notes

- **Reddit Answers rate limiting is critical.** OpenAI API costs for GPT-4o are ~$5/1M input tokens. At 15M weekly queries (Reddit's current scale), even with aggressive caching, API costs can exceed $100K/month. Implement response caching (Redis, 24-hour TTL for common queries), request deduplication, and progressive quality degradation (use GPT-4o-mini for simple queries, GPT-4o for complex ones).
- **Vote count consistency.** Redis sorted sets provide real-time ranking, but must be reconciled with PostgreSQL periodically. Use a write-through pattern: vote → update Redis immediately → enqueue Celery task to persist to PostgreSQL. Run a reconciliation job every 15 minutes to correct drift.
- **Comment tree performance.** Deeply nested threads are expensive to render. Fetch top 3 levels eagerly; deeper levels load on demand via `/api/v1/comments/:id/children`. Use materialized path or closure table pattern for efficient subtree queries. Reddit's own approach used a flattened list with depth indicators.
- **Embedding pipeline backpressure.** Every new post and comment must be embedded for vector search. At scale, this is a high-throughput background job. Use Celery with dedicated queues and autoscaling workers. Batch embedding requests to OpenAI (up to 2048 texts per request) to reduce API call overhead.
- **Ad auction must be fast.** Ad selection for feed insertion happens on every feed request. Pre-compute eligible ads per community+geo combination in Redis (refreshed every 5 minutes by a Celery beat task). Feed endpoint reads from Redis, not PostgreSQL, for ad selection.
- **Testing strategy:** Core business logic (voting, ranking, moderation rules) tested with pytest + pytest-asyncio. API endpoints tested with httpx TestClient. Frontend tested with Playwright for critical user flows (signup → first post → first vote). Ad delivery tested with integration tests against Stripe test mode. Target: 80% backend coverage, 100% coverage on voting and ranking logic.
- **Deployment pipeline:** PR → GitHub Actions (ruff lint + mypy type check + pytest) → merge to main → build Docker images → deploy to staging (ECS) → smoke test → manual approval → production deploy with rolling update (zero downtime). Database migrations run in a pre-deploy step with Alembic.
- **Content moderation at scale.** AutoMod rule engine runs synchronously on post/comment creation (regex matching, account age checks). For hate speech / NSFW detection, use a Celery background task with a classification model (OpenAI moderation endpoint or Perspective API) that flags content for human review rather than auto-removing.

## 11. Environment Variables

### App Configuration
- `APP_ENV` — Environment: development, staging, production (required)
- `APP_PORT` — API server port, default 8000 (optional)
- `APP_URL` — Public-facing URL for callbacks and links, e.g., https://reddit.example.com (required)
- `NEXT_PUBLIC_APP_URL` — Frontend public URL (required)
- `NEXT_PUBLIC_API_URL` — API base URL for frontend requests (required)

### Database
- `DATABASE_URL` — PostgreSQL connection string, e.g., postgresql://user:pass@host:5432/reddit (required)
- `REDIS_URL` — Redis connection string, e.g., redis://host:6379/0 (required)

### Authentication
- `CLERK_SECRET_KEY` — Clerk backend API key (required)
- `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` — Clerk frontend publishable key (required)
- `CLERK_WEBHOOK_SECRET` — Clerk webhook signing secret for user sync (required)

### External APIs
- `OPENAI_API_KEY` — OpenAI API key for embeddings and Reddit Answers LLM (required)
- `PINECONE_API_KEY` — Pinecone vector database API key (required)
- `PINECONE_INDEX_NAME` — Pinecone index name, e.g., reddit-content (required)
- `STRIPE_SECRET_KEY` — Stripe API key for advertiser billing (required)
- `STRIPE_WEBHOOK_SECRET` — Stripe webhook verification secret (required)
- `RESEND_API_KEY` — Resend email API key for transactional emails (required)
- `SENTRY_DSN` — Sentry error tracking DSN (required in production)

### Feature Flags
- `ENABLE_REDDIT_ANSWERS` — Enable AI search feature, default true (optional)
- `ENABLE_ADS` — Enable advertising platform, default false (optional)

### Monitoring
- `DD_API_KEY` — Datadog API key for metrics and APM (required in production)
- `DD_APP_KEY` — Datadog application key (required in production)

## 12. Getting Started

### Prerequisites
- Python 3.12+
- Node.js 20+
- PostgreSQL 16+
- Redis 7+
- Docker and Docker Compose (for local development)

### Setup
1. Clone the repository: `git clone <repo-url> && cd reddit-rebuild`
2. Install dependencies:
   ```bash
   cd apps/api && uv sync && cd ../..
   cd apps/web && npm install && cd ../..
   ```
3. Copy environment file: `cp .env.example .env`
4. Configure required environment variables (see section 11) — at minimum: `DATABASE_URL`, `REDIS_URL`, `CLERK_SECRET_KEY`, `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`, `OPENAI_API_KEY`
5. Start infrastructure services: `docker compose up -d postgres redis`
6. Run database migrations: `cd apps/api && uv run alembic upgrade head`
7. Seed initial data: `cd apps/api && uv run python3 -m src.core.seed`
8. Start backend: `cd apps/api && uv run uvicorn src.main:app --reload --port 8000`
9. Start frontend (separate terminal): `cd apps/web && npm run dev`
10. Open `http://localhost:3000` — you should see the landing page with a trending feed and Reddit Answers search bar

### Verify It's Working
- [ ] Landing page loads at localhost:3000
- [ ] Can create an account via Clerk and log in
- [ ] Can create a community and submit a post
- [ ] Voting updates score in real-time
- [ ] Reddit Answers returns a summarized answer for a test query
- [ ] API health check returns 200: `curl http://localhost:8000/api/v1/health`
