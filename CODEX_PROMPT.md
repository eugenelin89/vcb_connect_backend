Goal:
Initialize the backend for the "Vancouver Community Baseball (VCB)" project.

You are building a Django + Django REST Framework (DRF) backend that will serve as the REST API for the VCB mobile app (iOS SwiftUI client).

1. Scaffold the project folder structure.
2. Create a Django project called `vcb_backend` with the following apps:
   - `accounts` (users, JWT auth)
   - `leagues` (league + team management)
   - `volunteers` (volunteer slots, completions)
   - `games` (game results + rewards)
   - `shop` (store items + redemptions)
   - `points` (transactions, badges, streaks)
3. Add `requirements.txt` with minimal dependencies:
   - Django
   - djangorestframework
   - djangorestframework-simplejwt
   - django-environ
4. Create the following documentation files at the repo root with clear content:
   - `README.md` — overall description, setup instructions, roadmap.
   - `AGENTS.md` — define Codex’s role, project rules, and context.
   - `API.md` — initial API endpoint plan (empty placeholders are fine).
   - `architecture.md` — describe app relationships and future plans.
   - `CONTRIBUTING.md` — outline coding style and communication rules.
5. Ensure `.env.example` exists with the following placeholders:
   - `SECRET_KEY`
   - `DEBUG=True`
   (Note: SQLite will be used for development, so no database URL is required.)
6. Configure Django `settings.py` to use **SQLite 3** for development:
   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.sqlite3",
           "NAME": BASE_DIR / "db.sqlite3",
       }
   }


Rules:
- Use DRF ViewSets + Routers.
- Auth via `djangorestframework-simplejwt`.
- Organize code cleanly with separate `models.py`, `serializers.py`, and `views.py` per app.
- Include migrations setup (`python manage.py makemigrations` ready).
- Do not write all endpoints yet; just create project skeleton and documentation files.

When done, print the folder tree and short summary of each major file.

