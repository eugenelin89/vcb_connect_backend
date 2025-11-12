# Vancouver Community Baseball App (VCB) Backend

**Stack:** Django + Django REST Framework (SQLite for development, PostgreSQL for production)  
**Frontend client:** iOS SwiftUI app (consumes JSON REST API)

## Purpose
This backend powers the VCB mobile app, enabling:
- League & team management
- Volunteer signups and tracking
- Token (points) system for engagement
- Simple in-app store and redemptions
- Off-chain reward system, future on-chain migration

## Architecture
- Django project: `vcb_backend/`
- Core app modules:
  - `accounts/` – users, authentication (JWT)
  - `leagues/` – leagues, teams, roles
  - `volunteers/` – volunteer slots, completions
  - `games/` – game results and point rewards
  - `shop/` – store items, redemptions
  - `points/` – transactions, streaks, badges

## Auth
- JWT via `djangorestframework-simplejwt`
- Clients authenticate with `Authorization: Bearer <token>`

## API Base
All endpoints are under `/api/`.

## Setup
1. `pip install -r requirements.txt`
2. Ensure your `.env` has `SECRET_KEY` and `DEBUG=True` (sample values belong in `.env.example`).
3. Run migrations against the default SQLite database: `python manage.py migrate`
4. Start the dev server: `python manage.py runserver`
5. (Optional) Create an admin user: `python manage.py createsuperuser`

## Database
- **Development:** SQLite 3 at `BASE_DIR / db.sqlite3` (no extra configuration needed).
- **Production:** PostgreSQL via `DATABASE_URL`. When this env var is set, Django should be configured to use it.

## ENV
- `SECRET_KEY`
- `DEBUG=True/False`
- `DATABASE_URL` (only when targeting PostgreSQL, e.g., staging/production)

## Roadmap
- MVP: off-chain token ledger, volunteer flow
- Phase 2: on-chain migration (Solana/Polygon via API bridge)
