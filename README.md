# EAS Repository

A local, open-source dashboard for monitoring U.S. Emergency Alert System (EAS) and NOAA alerts.

It runs entirely on your machine, proxies the public GWES Central Alert Repository API and NOAA CAP feeds, and presents them in a clean interface with filtering, notifications, history, and more.

**Status:** v1.0.0-beta — usable early release. Core features are working; some polish and edge-case handling may still improve. Project name is temporary pending final confirmation.

## Screenshots

<!-- Replace these with actual screenshots of the dashboard -->

![Alerts list](https://via.placeholder.com/800x450.png?text=Alerts+List+Screenshot)
![Detail view](https://via.placeholder.com/800x450.png?text=Alert+Detail+Screenshot)
![Radar tab](https://via.placeholder.com/800x450.png?text=Radar+Tab+Screenshot)

To add real screenshots: run the dashboard, take screenshots of the main views, and replace the placeholder images above (or commit them to a `screenshots/` folder and update the links).

## Features
- Live GWES CAR + NOAA CAP alerts
- Source filtering
- Desktop notifications + simple keyword rules
- County/FIPS local alerting
- National radar loop
- Approximate alert map (Leaflet)
- Multiple themes (persisted)
- Alert history with timeline scrubber
- Offline/cached mode with clear last-update status
- Export/import settings packs (including rules)
- PWA (installable, basic offline support)
- 100% local — no accounts or API keys required

## Requirements
- Python 3.8 or newer (standard library only; no pip installs)
- Internet connection
- A modern browser

## Quick Start
1. Clone this repository:
   ```bash
   git clone https://github.com/colt98045-beep/eas-repository.git
   cd eas-repository
   ```
2. (Optional) Choose a port:
   ```bash
   export EAS_PORT=3000   # default is 8080
   ```
3. Run the server:
   ```bash
   python eas_monitor.py
   ```
4. Open your browser to http://localhost:8080 (or whatever port you set)

Press Ctrl+C in the terminal to stop the server.

## Attribution & Data Sources
This dashboard uses publicly available endpoints that require no API key:
- Global Weather & EAS Society (GWES) Central Alert Repository — https://alerts.globaleas.org
- NOAA CAP feeds via api.weather.gov and alerts.weather.gov

Requests include a descriptive User-Agent (`EASRepository/1.0`). Please respect the terms of the upstream services. Data is proxied and displayed locally; nothing is stored on remote servers by this project.

See the [NOTICE](NOTICE) file for a short list of third-party sources.

## Notes
- Alerts are cached briefly (≈10 seconds) to reduce load on upstream APIs.
- On feed errors the dashboard keeps showing the last good data and marks itself offline/cached.
- Settings (including theme, FIPS, and rules) can be exported/imported as a JSON pack from the Settings modal.
- The Map tab uses approximate marker positions (real county centroids can be added later).
- PWA support lets you install the dashboard on mobile or desktop.
- Some advanced UI features (radar, audio, history) are functional but may still receive polish in future updates.
- For questions about the GWES APIs, see https://alerts.globaleas.org/swagger/ or contact the GWES team.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to run the project, report issues, and submit changes.

## License

This project is licensed under the Apache License 2.0.

See the [LICENSE](LICENSE) file for the full text.

Copyright 2026 Colt
