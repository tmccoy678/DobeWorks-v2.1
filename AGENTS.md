# DobeWorks

## Agent skills

### Issue tracker

Issues and specifications are tracked as local Markdown under `.scratch/`. See `docs/agents/issue-tracker.md`.

### Triage labels

The project uses the default five-role triage vocabulary. See `docs/agents/triage-labels.md`.

### Engineering assurance

Assurance: before accepting changes to code, documents, validators, evidence, AI-assisted artifacts, or Git phase records, select and apply the relevant [DEAS v1.0](docs/standards/deas/v1/standard.md) profile and overlays. Use the [enforcement matrix](docs/standards/deas/v1/enforcement-matrix.md) for gates and evidence; Exploratory work cannot promote itself.

### Domain docs

The project uses the multi-context layout in `CONTEXT-MAP.md`. The root `CONTEXT.md` owns the DobeWorks name, private scope, identity, and provenance; `contexts/operational-system/CONTEXT.md` owns Operational System language. Cross-context decisions live under `docs/adr/`, and future context-specific decisions live with their context. See `docs/agents/domain.md`.
