# Architecture

## Overview
- **Framework:** Django + Django REST Framework (DRF).
- **Project:** `vcb_backend` orchestrates six domain apps focused on user identity, gameplay, volunteering, rewards, and commerce.
- **Client:** SwiftUI mobile app consuming JWT-protected REST endpoints under `/api/`.

## App Responsibilities
- `accounts` — user profiles, JWT auth integration, future parent/player role management.
- `leagues` — leagues, teams, and roster relationships.
- `volunteers` — volunteer opportunity definitions, assignments, and completion tracking that convert to points.
- `games` — schedules, score submissions, and post-game point rewards.
- `points` — ledger for earning/spending, badge tracking, and streak logic.
- `shop` — catalog + redemption workflows for spending points.

## Data Flow
1. Users authenticate via JWT, obtaining tokens from `/api/token/`.
2. Authenticated calls hit DRF viewsets routed through `vcb_backend/urls.py`.
3. Business logic lives inside each app, with serializers enforcing data contracts for the SwiftUI client.
4. Points transactions will emit domain events (future Celery hook) allowing analytics + blockchain sync.

## Persistence Strategy
- **Development:** SQLite (`db.sqlite3`).
- **Production:** PostgreSQL via `DATABASE_URL` in the environment.
- `django-environ` coordinates env-specific settings to keep deployments consistent.

## Future Plans
- Replace placeholder viewsets with model-backed CRUD endpoints.
- Introduce signals/services so games, volunteers, and shop redemptions manipulate the points ledger atomically.
- Add async workers for token-minting once on-chain integration (Solana/Polygon) is ready.
