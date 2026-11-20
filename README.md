# EAS Repository

A local, open-source dashboard for monitoring U.S. Emergency Alert System (EAS) and NOAA alerts.

It runs entirely on your machine, proxies the public GWES Central Alert Repository API and NOAA CAP feeds, and presents them in a clean interface with filtering, notifications, history, and more.

**Status:** Initial release (v1). Name is temporary pending final confirmation; the current name is descriptive and non-conflicting.

## Features
- Live GWES CAR + NOAA CAP alerts
- Source filtering
- Desktop notifications
- County/FIPS local alerting
- National radar loop
- Multiple themes
- Alert history, detail view, and audio playback
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
2. Run the server:
   ```bash
   python eas_monitor.py
   ```
3. Open your browser to http://localhost:8080

Press Ctrl+C in the terminal to stop the server.

## Attribution & Data Sources
This dashboard uses publicly available endpoints that require no API key:
- Global Weather & EAS Society (GWES) Central Alert Repository — https://alerts.globaleas.org
- NOAA CAP feeds via api.weather.gov and alerts.weather.gov

Requests include a descriptive User-Agent (`EASRepository/1.0`). Please respect the terms of the upstream services. Data is proxied and displayed locally; nothing is stored on remote servers by this project.

## Notes
- Alerts are cached briefly (≈10 seconds) to reduce load on upstream APIs.
- Some advanced UI features (radar, audio, history) are functional but may still receive polish in future updates.
- For questions about the GWES APIs, see https://alerts.globaleas.org/swagger/ or contact the GWES team.

## License
See LICENSE file.
