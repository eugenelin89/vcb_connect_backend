Goal:
Initialize the backend for the "Vancouver Community Baseball (VCB)" project.

You are building a Django + Django REST Framework (DRF) backend that will serve as the REST API for the VCB mobile app (iOS SwiftUI client).

Your first task:
1. Scaffold the project folder structure.
2. Create a Django project called `vcb_backend` with the following apps:
   - `accounts` (users, JWT auth)
   - `leagues` (league + team management)
   - `volunteers` (volunteer slots, completions)
   - `games` (game results + rewards)
   - `shop` (store items + redemptions)
   - `points` (transactions, badges, streaks)
3. Add `requirements.txt` with minimal dependencies (Django, DRF, simplejwt, psycopg2, django-environ).
4. Create the following documentation files at the repo root with clear content:
   - `README.md` — overall description, setup instructions, roadmap.
   - `AGENTS.md` — define Codex’s role, project rules, and context.
   - `API.md` — initial API endpoint plan (empty placeholders are fine).
   - `architecture.md` — describe app relationships and future plans.
   - `CONTRIBUTING.md` — outline coding style and communication rules.
5. Ensure `.env.example` exists with `DATABASE_URL`, `SECRET_KEY`, and `DEBUG` placeholders.
6. Add an initial `docker-compose.yml` for Postgres + web service (optional if time allows).
7. Output a brief summary of the file tree you created.

Assume Python 3.11+ and Postgres as the DB.

Rules:
- Use DRF ViewSets + Routers.
- Auth via `djangorestframework-simplejwt`.
- Organize code cleanly with separate `models.py`, `serializers.py`, and `views.py` per app.
- Include migrations setup (`python manage.py makemigrations` ready).
- Do not write all endpoints yet; just create project skeleton and documentation files.

When done, print the folder tree and short summary of each major file.

