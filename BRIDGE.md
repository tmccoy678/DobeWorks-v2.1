# bridge/ — retired

## What was here

From October 5–6, 2026, this repo contained a `bridge/` directory used by the
Nova↔Grok terminal bridge experiment:

- `bridge/inbox.md` — a message inbox. Nova (an AI agent built by Meta, working
  for Taylor McCoy) wrote task messages here. A Linux VM provisioned by xAI
  ("grok-bot-vm") polled this file every ~15 seconds and printed new messages
  to its terminal, where Grok (xAI's AI agent) read them. Grok replied through
  a webhook inbox. No secrets were ever stored here; the channel was treated
  as semi-public by design.
- `bridge/receiver/` (October 6, briefly) — a small Python webhook receiver
  intended to move the Grok→Nova lane from a borrowed webhook.site inbox to
  bridge.dobeworks.com. Removed the same day it was added.

## Who put it here

Nova, acting on direct instructions from Taylor McCoy (tmccoy678), the repo owner.

## Why it was here

The experiment needed a message lane both sides could reach, and this repo was
the available channel. It was scaffolding, never part of the project itself.

## Why it's gone

Taylor's rule for her public repos: hands off — experimental infrastructure
belongs on dobeworks.com, not in public project repos. On October 6, 2026 she
ordered this repo restored to its post-review state and this note left in place
of the bridge files.

## Where the work lives now

- Bridge infrastructure: dobeworks.com (bridge.dobeworks.com).
- Public security writeup of the experiment: tmccoy678/grok-bridge-writeup.
- The experiment itself continues off-repo.
