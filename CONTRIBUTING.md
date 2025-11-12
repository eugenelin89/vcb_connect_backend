# Contributing

## Ground Rules
- Use feature branches and open small, reviewable pull requests.
- Keep discussions in GitHub issues; record design decisions in `architecture.md`.
- Match the SwiftUI client contract before exposing/altering APIs.

## Coding Style
- Python 3.11+, Django 5.x.
- Follow Django + DRF conventions: serializers in `serializers.py`, viewsets in `views.py`, routers in `urls.py`.
- Prefer `ViewSet` classes wired up via DRF routers. Function-based views are discouraged.
- Always add/modify tests alongside behavior changes.
- Default permissions: authenticated-only; explicitly annotate public endpoints.

## Tooling
- Format with `black` (line length 88) and `ruff` for linting once tooling is added.
- Run `python manage.py makemigrations && python manage.py migrate` before test runs to keep schema current.

## Communication
- Document new endpoints in `API.md` and update relevant runbooks.
- Surface breaking changes to the iOS team early via shared Slack channel.
