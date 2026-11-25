# Changelog

All notable changes to this project are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Dates are DD/MM/YYYY.

## [Unreleased]

## 24/11/2026

### Added
- Temporary README notice that the hosted US API is down or degraded (marked
  `TEMP-OUTAGE-NOTICE` so it can be removed later). Docs only.
- Maintenance overlay shows the lockout reason (Outage, Maintenance, Update or
  Other) with its colour and icon. Covered by `tests/maintenance-overlay.test.mjs`.
  Client code only; the Turnstile gate and APIs are unchanged.
- Tab icon (inline `data:` SVG) on the dashboard, challenge, fail and privacy
  pages. `img-src data:` was added to the challenge, fail and privacy CSPs only.
  Service worker cache `eas-v5`. No new gate exemption.
- Public `/privacy` page (effective 24/11/2026), readable without passing
  Turnstile. Exact-path exemption for `GET`/`HEAD` `/privacy` and `/privacy/`
  with no query string, served as a static string from `src/privacy.js`. Every
  other path, including `/privacy.html` and `/privacy?x=1`, still gets the
  Turnstile 403. Service worker cache `eas-v4`.
- Access log rows include the full client IP (`ip`, from `CF-Connecting-IP`)
  next to `ip_hash`. Run `schema/migrations/0002_add_ip.sql` once; until then
  the logger falls back to the old insert. Logging hook only: the Turnstile
  gate, the API routes and `.assetsignore` are unchanged.
- Access logging to a shared D1 database (`ACCESS_LOG`). Writes are scheduled
  with `waitUntil` and cannot change the Turnstile gate or API responses.
- Dashboard maintenance lockout, toggled from the EAS launcher admin page. If
  the maintenance request fails, the dashboard stays normal.
- Dismissible announcement banner from the EAS launcher. It fails silently if
  that API is unreachable.
- `DEPLOY.md`, `SECURITY.md`, `CHANGELOG.md`, `.editorconfig`, issue and pull
  request templates.
- GitHub Actions CI (ruff, JavaScript syntax, JSON validation, server smoke
  test) and a Cloudflare Worker deploy guard (`wrangler.jsonc`, `.assetsignore`,
  Turnstile gate and API route tests, `wrangler deploy --dry-run`).
- Footer with GWES / NOAA attribution and a non-affiliation note.
- The server also reads the `PORT` environment variable when `EAS_PORT` is not set.

### Fixed
- NOAA alerts now use the feed's entry ID, so the same alert no longer
  re-triggers notifications on every refresh.

### Changed
- Removed the temporary README notice that the hosted US API was down or degraded. Docs only.
- `eas_monitor.py` formatted with ruff (no behavior change).
- External links open with `rel="noopener noreferrer"`.

## 20/11/2026 — 1.0.0-beta

### Added
- Local Python backend (standard library only) proxying the GWES Central Alert
  Repository and NOAA CAP feeds, with a short in-memory cache.
- Dashboard: active alerts, source and event filters, search, pins, history with
  a timeline scrubber, approximate Leaflet map, NWS radar loop, links, and stats.
- Desktop notifications, sound, mute, keyword notification rules, and county
  (FIPS) alerting.
- Multiple persisted themes, settings pack export/import, and JSON export.
- PWA manifest and service worker, offline/cached status indicator.
- Password lock screen, configurable port via `EAS_PORT`.
- Apache 2.0 license, NOTICE, and CONTRIBUTING guide.
- README screenshots of the Active, History and Radar tabs.

### Fixed
- Map tab reliably displays the Leaflet map.
