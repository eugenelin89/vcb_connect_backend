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
1. Install or select the latest stable Python (3.12.x recommended). With `pyenv`:
   ```bash
   pyenv install 3.12.3   # or newest patch
   pyenv local 3.12.3
   python3 --version      # verify it reports 3.12.x
   ```
2. Create and activate a virtual environment using that interpreter:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # Windows: .venv\Scripts\activate
   ```
3. Install dependencies from the pinned list:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   (Re-run this step whenever `requirements.txt` changes so new packages like `drf-spectacular` are available.)
4. Copy the sample env file if you do not already have one: `cp .env.example .env`, then populate `SECRET_KEY` and adjust `DEBUG`/`DATABASE_URL` as needed.
5. Apply migrations against the default SQLite database: `python manage.py migrate`
6. Run the dev server: `python manage.py runserver`
7. (Optional) Create an admin user for local testing: `python manage.py createsuperuser`

-## Viewing the REST Interface
- **Browsable API:** Once `python manage.py runserver` is running, open `http://127.0.0.1:8000/api/` in a browser. DRF ships its browsable interface by default, so each placeholder endpoint (accounts, leagues, etc.) renders interactive JSON forms. Use the “Login” link in the top-right (wired via `/api/auth/login/`) to authenticate with your Django credentials; you’ll be redirected back to `/api/` on success and subsequent requests use the session cookie.
- **Swagger UI:** Visit `http://127.0.0.1:8000/api/docs/` for an interactive OpenAPI explorer backed by `drf-spectacular`. The raw schema (JSON) is available at `http://127.0.0.1:8000/api/schema/` if you need to import it into Postman or other tooling.
- **Auth endpoints:** `http://127.0.0.1:8000/api/token/` provides a simple form to obtain JWTs; POSTing valid credentials returns access/refresh tokens. Include `Authorization: Bearer <token>` in subsequent requests (set headers manually or via Postman’s auth helpers). Browser sessions already authenticated through `/api/auth/login/` also work because DRF SessionAuthentication is enabled.
- **cURL/Postman:** You can use `curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/api/accounts/` or import the endpoints into Postman. Everything is namespaced under `/api/`.

### Updating an Existing Virtualenv to Python 3.12.x
If your `.venv` was created with an older interpreter, recreate it so it points at Python 3.12.x. This does **not** change the system/global Python, only the interpreter embedded in `.venv`:
1. Install (or download) Python 3.12.x somewhere local. Using `pyenv` keeps it scoped to the project: `pyenv install 3.12.3 && pyenv local 3.12.3`. Alternatively, install with Homebrew (`brew install python@3.12`) and call the binary via its full path.
2. Remove the old venv folder: `rm -rf .venv`.
3. Recreate the environment using the 3.12 binary explicitly:
   ```bash
   /path/to/python3.12 -m venv .venv   # e.g., ~/.pyenv/versions/3.12.3/bin/python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Continue with the usual `python manage.py migrate` / `runserver` steps.

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
