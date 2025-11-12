# AGENTS.md

## Active Agents
- **you (human)** – Project owner, architect, lead developer
- **codex** – Assistant developer; writes Django + DRF code, obeys style guide below.

## Context
- Primary backend: Django + DRF, PostgreSQL.
- Frontend: iOS SwiftUI app consuming REST endpoints.
- Points system is off-chain for now.
- Later migration to token (Solana/Polygon).

## Rules for Codex
1. Never delete models or migrations unless explicitly told.
2. Always update docs when making new modules.
3. Use DRF `ViewSet` + `Router` structure for consistency.
4. Explain new endpoints briefly in `API.md` after creation.
5. Keep JWT auth compatible with Swift iOS client (Bearer header).

