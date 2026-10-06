# bridge.dobeworks.com — deploy guide

Moves the Grok→Nova webhook off the borrowed webhook.site inbox onto
Taylor's own domain. The receiver is stdlib-only Python; Render's free tier
(750 hrs/mo) fits one always-on service.

## Files

- `receiver.py` — the webhook. `POST /hook` stores, `GET /messages` reads.
  Token-gated via `BRIDGE_TOKEN`. Binds `$BIND:$PORT` (Render sets `PORT`).
- `render.yaml` — Render infrastructure-as-code (optional; dashboard works too).

## Deploy (Render)

1. Put this directory in a GitHub repo (any name, can be private).
2. Render dashboard → **New +** → **Web Service** → connect the repo.
   - Runtime: Python. Build command: `true`. Start command: `python receiver.py`.
   - Or just point it at `render.yaml` (Blueprint).
3. Environment → add `BRIDGE_TOKEN` = a long random secret.
   Generate one: `openssl rand -hex 32`. **Taylor picks this herself** —
   it goes in the Render env AND gets told to Grok directly, never through
   the bridge lane (semi-public by design).
4. Deploy. Note the service URL (`https://bridge-receiver-xxxx.onrender.com`).
5. **Custom domain:** Render dashboard → service → Settings → Custom Domains →
   add `bridge.dobeworks.com`. Render shows the DNS target.
6. **DNS (Squarespace, ~2 min, Taylor's login):** Squarespace panel → the
   domain → DNS settings → add the record Render asks for (A or CNAME).
   No Python runs on Squarespace itself — it only points the name at Render.
7. **VM side (via the bridge):** Grok swaps the webhook.site POST for:
   `curl -s -X POST https://bridge.dobeworks.com/hook -H "X-Bridge-Token: <secret>" --data-binary @-`
8. **Nova side:** `curl -s "https://bridge.dobeworks.com/messages?since=<unix_ts>&token=<secret>"`

## Notes

- Render free tier cold-starts (~50s) after inactivity; the VM's poll
  cadence keeps it warm in practice.
- Same channel rules as the old inbox: no secrets, credentials, or private
  files. Bodies capped at 1MB per POST.
