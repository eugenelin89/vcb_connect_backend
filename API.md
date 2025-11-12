# API Reference (VCB Backend)

## Auth
- POST /api/token/ — login
- POST /api/token/refresh/ — refresh JWT
- GET /api/schema/ — OpenAPI schema (JSON)
- GET /api/docs/ — Swagger UI powered by drf-spectacular

## Scaffolded Placeholders
The following endpoints currently return placeholder JSON via DRF `ViewSet`s. They prove routing + JWT wiring and will be replaced with model-backed implementations:
- GET /api/accounts/ — Accounts module placeholder
- GET /api/leagues/ — League + team placeholder
- GET /api/volunteers/ — Volunteer module placeholder
- GET /api/games/ — Games module placeholder
- GET /api/shop/ — Shop module placeholder
- GET /api/points/ — Points ledger placeholder

## Users
- GET /api/me/ — current profile
- POST /api/register/ — create user

## Leagues & Teams
- GET /api/leagues/
- POST /api/leagues/
- GET /api/teams/{id}/
- POST /api/teams/

## Volunteer Slots
- GET /api/teams/{id}/volunteer-slots/
- POST /api/teams/{id}/volunteer-slots/
- POST /api/volunteer-slots/{id}/claim/
- POST /api/volunteer-slots/{id}/complete/

## Games
- POST /api/teams/{id}/games/
- GET /api/teams/{id}/games/

## Store
- GET /api/store/items/
- POST /api/store/items/{id}/redeem-with-points/
