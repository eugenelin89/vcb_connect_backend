# API Reference (VCB Backend)

## Auth
- POST /api/token/ — login
- POST /api/token/refresh/ — refresh JWT

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

