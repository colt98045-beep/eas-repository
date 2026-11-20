#!/usr/bin/env python3
import json
import urllib.request
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import os

API_BASE = "https://alerts.globaleas.org"
PORT = 8080
HTML_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
USER_AGENT = "EASRepository/1.0 (https://github.com/colt98045-beep/eas-repository)"

_cache = {"data": None, "ts": 0}
CACHE_TTL = 10

def fetch_json(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))

def fetch_active_alerts():
    now = time.time()
    if _cache["data"] is not None and now - _cache["ts"] < CACHE_TTL:
        return _cache["data"]
    try:
        data = fetch_json(f"{API_BASE}/api/v2/alerts/active")
        _cache["data"] = data
        _cache["ts"] = now
        return data
    except Exception as e:
        print(f"GlobalEAS fetch error: {e}")
        return _cache["data"] or []

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # Serve the frontend
        if path in ("/", "/index.html"):
            try:
                with open(HTML_FILE, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(500, "index.html not found")
            return

        # GlobalEAS active alerts
        if path == "/api/active":
            alerts = fetch_active_alerts()
            self._send_json(alerts)
            return

        # NOAA national CAP/Atom feed
        if path == "/api/noaa":
            self._proxy(
                "https://alerts.weather.gov/cap/us.php?x=1",
                content_type="application/xml"
            )
            return

        # Optional: NOAA by state (example: /api/noaa/FL)
        if path.startswith("/api/noaa/"):
            state = path.split("/")[-1].upper()
            if len(state) == 2:
                self._proxy(
                    f"https://alerts.weather.gov/cap/wwaatmget.php?x={state}",
                    content_type="application/xml"
                )
                return

        # Optional: api.weather.gov JSON (cleaner)
        if path == "/api/nws":
            self._proxy(
                "https://api.weather.gov/alerts/active",
                content_type="application/json",
                headers={"Accept": "application/geo+json", "User-Agent": USER_AGENT}
            )
            return

        self.send_error(404)

    def _send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _proxy(self, url, content_type="application/xml", headers=None, timeout=20):
        try:
            hdrs = {"User-Agent": USER_AGENT}
            if headers:
                hdrs.update(headers)
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            print(f"Proxy error ({url}): {e}")
            self.send_error(502, "Upstream feed unavailable")

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    print(f"Starting EAS Repository on http://localhost:{PORT}")
    print(f"Serving HTML from: {HTML_FILE}")
    print("Press Ctrl+C to stop")
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.shutdown()
