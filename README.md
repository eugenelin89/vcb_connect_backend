# Vancouver Community Baseball App (VCB) Backend

**Stack:** Django + Django REST Framework + PostgreSQL  
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
2. `python manage.py migrate`
3. `python manage.py runserver`
4. Create admin: `python manage.py createsuperuser`

## ENV
- `DATABASE_URL`
- `SECRET_KEY`
- `DEBUG=True/False`

## Roadmap
- MVP: off-chain token ledger, volunteer flow
- Phase 2: on-chain migration (Solana/Polygon via API bridge)

