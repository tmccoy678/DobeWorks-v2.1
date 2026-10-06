#!/usr/bin/env python3
"""
bridge.dobeworks.com — webhook receiver for the Nova<->Grok bridge.

Replaces the borrowed webhook.site inbox. The Grok VM POSTs to /hook;
Nova polls /messages. Stdlib only — runs anywhere Python 3 exists.

Deploy:
  1. Copy to the host behind bridge.dobeworks.com (VPS, shared host with
     Python, Render/Railway/Fly, anything that can run a script).
  2. Set env vars:  BRIDGE_TOKEN=<long random secret>  (required)
                     BRIDGE_STORE=/var/lib/bridge/messages.jsonl (optional)
                     PORT=8787 (optional)
  3. Run:  BRIDGE_TOKEN=... python3 receiver.py
     Bind is 127.0.0.1 — put it behind nginx/Caddy as a reverse proxy for
     https://bridge.dobeworks.com. On a dedicated VPS you may bind 0.0.0.0
     instead (change the HTTPServer line below).
  4. Point DNS:  bridge.dobeworks.com  A  <server IP>   (or CNAME per host)

VM side (Grok): replace the webhook.site POST with:
  curl -s -X POST https://bridge.dobeworks.com/hook \
       -H "X-Bridge-Token: <same secret>" \
       --data-binary @-   (or -d "$message")

Nova side: poll new messages with:
  curl -s "https://bridge.dobeworks.com/messages?since=<unix_ts>&token=<secret>"

Security notes:
  - The token is a shared secret between Taylor's server and the Grok VM.
    Taylor should choose it and place it on both ends herself (server env
    + tell Grok directly) rather than sending it through the bridge lane,
    which is semi-public by design.
  - Bodies are capped at 1MB per POST. No secrets, credentials, or private
    files over this channel — same rule as the old inbox.
"""

import json
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

STORE = os.environ.get("BRIDGE_STORE", "/tmp/bridge_messages.jsonl")
TOKEN = os.environ.get("BRIDGE_TOKEN", "")
MAX_BODY = 1_000_000


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        data = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _token_ok(self, provided):
        # Empty TOKEN = open receiver. Don't run it that way.
        return bool(TOKEN) and provided == TOKEN

    def do_POST(self):
        url = urlparse(self.path)
        if url.path != "/hook":
            return self._send(404, {"ok": False, "error": "not found"})
        if not TOKEN:
            return self._send(503, {"ok": False, "error": "server not configured"})
        qs = parse_qs(url.query)
        provided = self.headers.get("X-Bridge-Token",
                                     qs.get("token", [""])[0])
        if not self._token_ok(provided):
            return self._send(403, {"ok": False, "error": "bad token"})
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX_BODY:
            return self._send(413, {"ok": False, "error": "body too large"})
        body = self.rfile.read(length).decode("utf-8", "replace")
        rec = {"ts": time.time(), "body": body}
        os.makedirs(os.path.dirname(STORE) or ".", exist_ok=True)
        with open(STORE, "a") as f:
            f.write(json.dumps(rec) + "\n")
        self._send(200, {"ok": True, "ts": rec["ts"]})

    def do_GET(self):
        url = urlparse(self.path)
        if url.path != "/messages":
            return self._send(404, {"ok": False, "error": "not found"})
        qs = parse_qs(url.query)
        if not self._token_ok(qs.get("token", [""])[0]):
            return self._send(403, {"ok": False, "error": "bad token"})
        try:
            since = float(qs.get("since", ["0"])[0] or 0)
        except ValueError:
            since = 0
        out = []
        if os.path.exists(STORE):
            with open(STORE) as f:
                for line in f:
                    try:
                        r = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if r.get("ts", 0) > since:
                        out.append(r)
        self._send(200, {"ok": True, "messages": out})

    def log_message(self, *args):
        pass  # quiet; put behind a real proxy for access logs


if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Set BRIDGE_TOKEN env var (long random secret). Refusing to run open.")
    port = int(os.environ.get("PORT", "8787"))
    bind = os.environ.get("BIND", "127.0.0.1")  # 0.0.0.0 on Render/VPS behind no proxy
    HTTPServer((bind, port), Handler).serve_forever()
