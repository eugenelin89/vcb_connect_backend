## Task: Implement data models
Task: Implement core Django models for the VCB backend

Context:
- This repo is the backend for the Vancouver Community Baseball (VCB) app.
- Stack: Django + DRF, SQLite for development.
- Apps: `accounts`, `leagues`, `volunteers`, `games`, `shop`, `points`.
- The README and architecture assume:
  - Leagues → Teams → Users
  - Volunteer slots + completions
  - Points (token) ledger
  - Store items + redemptions
  - Streaks and badges

Before coding:
- Read `README.md`, `architecture.md`, and `API.md` (if present).
- Inspect the existing app files so you don’t duplicate code Codex already generated.

Goal:
Define the **data models only** (no views/serializers yet) for each app, with sensible fields, relationships, and docstrings.

## Models to implement

### 1) `accounts/models.py`
Use Django’s built-in `User` model as the auth user (via `settings.AUTH_USER_MODEL`), and add a profile model.

Create:

- `UserProfile`
  - `user` → OneToOneField to `AUTH_USER_MODEL`
  - `role` → CharField with choices: `player`, `coach`, `admin`
  - `league` → ForeignKey to `leagues.League`, nullable/blank (user may not be in a league yet)
  - `team` → ForeignKey to `leagues.Team`, nullable/blank (user may not be on a team yet)
  - `points` → IntegerField, default 0 (denormalized balance)
  - `current_streak` → IntegerField, default 0
  - `last_activity_date` → DateField, null/blank (last date they earned points / did something)
  - `created_at` / `updated_at` → DateTimeField auto_add/auto_now

Add:
- `__str__` returning something like `"UserProfile(<user.email>, role=<role>)"`.
- Meta + docstring explaining this is the extension point for user-specific fields.

### 2) `leagues/models.py`

Create:

- `League`
  - `id` → default AutoField/BigAutoField
  - `name` → CharField
  - `slug` → SlugField, unique (e.g., `vancouver-community-baseball`)
  - `created_at` / `updated_at`
  - `__str__` = name

- `Team`
  - `league` → ForeignKey to `League`, related_name="teams"
  - `name` → CharField
  - `division` → optional CharField (e.g., "11U", "13U"), nullable/blank
  - `coach` → ForeignKey to `AUTH_USER_MODEL`, related_name="coached_teams", nullable/blank
  - `created_at` / `updated_at`
  - `__str__` = f"{league.slug} - {name}"

Membership relationship:
- We will rely on `UserProfile.team` to know which players belong to which team (no M2M on Team for now).

### 3) `volunteers/models.py`

Create:

- `VolunteerSlot`
  - `league` → ForeignKey to `leagues.League`, related_name="volunteer_slots"
  - `team` → ForeignKey to `leagues.Team`, related_name="volunteer_slots", nullable/blank (some slots might be league-wide)
  - `event_date` → DateTimeField
  - `role_name` → CharField (e.g., "Scorekeeper", "Field prep")
  - `status` → CharField with choices:
    - `open`
    - `claimed`
    - `completed`
  - `claimed_by` → ForeignKey to `AUTH_USER_MODEL`, related_name="claimed_volunteer_slots", null=True, blank=True
  - `created_at` / `updated_at`
  - `__str__` returns f"{role_name} on {event_date} ({status})"

### 4) `games/models.py`

Create:

- `Game`
  - `league` → ForeignKey to `leagues.League`, related_name="games"
  - `team` → ForeignKey to `leagues.Team`, related_name="games"
  - `date` → DateField
  - `opponent` → CharField
  - `result` → CharField with choices:
    - `win`
    - `loss`
  - `created_at` → DateTimeField auto_add
  - `__str__` returns something like `"Team vs Opponent on date (result)"`

Later the points app will award points when a win is recorded.

### 5) `shop/models.py`

Create:

- `StoreItem`
  - `league` → ForeignKey to `leagues.League`, related_name="store_items"
  - `name` → CharField
  - `description` → TextField (blank=True)
  - `price_cents` → IntegerField (e.g., 2500 = $25.00)
  - `points_discount_allowed` → IntegerField (max points that can be applied), default 0
  - `is_active` → BooleanField default True
  - `created_at` / `updated_at`
  - `__str__` returns name

Optional (only if you want it now): an `Order` model to represent a redemption, but it can be added later.

### 6) `points/models.py`

Create:

- `PointsTransaction`
  - `user` → ForeignKey to `AUTH_USER_MODEL`, related_name="points_transactions"
  - `league` → ForeignKey to `leagues.League`, related_name="points_transactions"
  - `delta` → IntegerField (positive or negative)
  - `reason` → CharField with choices such as:
    - `volunteer_completed`
    - `game_win_bonus`
    - `shop_redeem`
    - `manual_adjustment`
  - `created_at` → DateTimeField auto_add
  - `__str__` returns f"{user} {delta} points ({reason})"

(We can derive badges and streaks from this in code later, so a separate Badge model is optional for MVP.)

---

## Implementation details / constraints

- Use `from django.conf import settings` and `settings.AUTH_USER_MODEL` for user FKs.
- Add appropriate `related_name` values to avoid reverse name collisions.
- Add basic `Meta` options where helpful:
  - `ordering` by `-created_at` on transactional models
  - `unique_together` or `UniqueConstraint` on things like `League.slug`
- Add migrations (`python manage.py makemigrations`) code scaffolding, but you don’t need to run them; just ensure they generate cleanly.
- Do **not** create serializers or viewsets yet; this task is models-only.

## Output

When done:

1. Show the updated `models.py` files for each app that changed.
2. List the models created with a brief one-line description each.
3. Confirm that `makemigrations` should succeed (no import loops, all FKs resolvable).
