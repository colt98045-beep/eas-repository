# Changelog

All notable changes to this project are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Dismissible announcement banner on the dashboard. It reads active notices from the EAS launcher (`/api/announcements?site=us`) and fails silently if that API is unreachable. The Turnstile gate, the API routes and `.assetsignore` are unchanged.

- `DEPLOY.md` (replaces `DEPLOY.txt`) with Markdown formatting.
- `SECURITY.md`, `CHANGELOG.md`, `.editorconfig`, issue and pull request templates.
- GitHub Actions CI: ruff lint/format check, JavaScript syntax check, JSON validation,
  and a server smoke test.
- Footer in the dashboard with GWES / NOAA attribution and a non-affiliation note.
- CI job "Cloudflare Worker deploy guard": checks `wrangler.jsonc` and `.assetsignore`,
  runs Turnstile gate and API route tests for `src/index.js`, and a `wrangler deploy --dry-run`.
- The server also reads the `PORT` environment variable when `EAS_PORT` is not set.

### Fixed
- NOAA alerts now use the feed's entry ID, so the same alert no longer re-triggers
  notifications on every refresh.

### Changed
- `eas_monitor.py` formatted with ruff (no behavior change).
- External links open with `rel="noopener noreferrer"`.

## [1.0.0-beta] - 2026-11-20

### Added
- Local Python backend (standard library only) proxying the GWES Central Alert Repository
  and NOAA CAP feeds, with a short in-memory cache.
- Dashboard: active alerts, source and event filters, search, pins, history with timeline
  scrubber, approximate Leaflet map, NWS radar loop, links, and stats.
- Desktop notifications, sound, mute, keyword notification rules, and county (FIPS) alerting.
- Multiple persisted themes, settings pack export/import, and JSON export.
- PWA manifest and service worker, offline/cached status indicator.
- Password lock screen, configurable port via `EAS_PORT`.
- Apache 2.0 license, NOTICE, and CONTRIBUTING guide.
- README screenshots of the Active, History and Radar tabs.

### Fixed
- Map tab reliably displays the Leaflet map.

