# Domain Docs

## Before exploring

Read:

- `CONTEXT-MAP.md` to identify the owning context
- the relevant context's `CONTEXT.md`
- relevant cross-context decisions under `docs/adr/`
- relevant context-specific decisions under that context's `docs/adr/`, when the directory exists

If these files do not yet exist, proceed silently. `/domain-modeling`, normally reached through `/grill-with-docs`, creates them when terms or decisions are actually resolved.

## Layout

This is a multi-context repository:

```
/
├── CONTEXT-MAP.md
├── CONTEXT.md
├── docs/adr/
└── contexts/
    └── operational-system/
        ├── CONTEXT.md
        └── docs/
            ├── adr/
            └── program/
```

The root context owns the complete DobeWorks name, personal-project scope, public-source boundary, identity, and provenance. The Operational System context owns hardware/software mission, roles, data and recovery classes, requirements, configuration, evidence, operations, maintenance, and retirement. AI-Workspace Workbench/Command Center terminology and DEGS policy remain external sources and are not redefined here.

## Vocabulary

Use terms exactly as defined by the owning context. Do not drift to synonyms a glossary explicitly avoids, copy one context's implementation details into another glossary, or silently equate external Workbench/DEGS terms with DobeWorks terms.

If a needed concept is absent, reconsider whether the term belongs or record the gap for `/domain-modeling`.

## Context boundaries

- Use the root `CONTEXT.md` for DobeWorks, identity, provenance, Private Use, and Public Release language.
- Use `contexts/operational-system/CONTEXT.md` for Control Plane, Storage Resource, Worker, Observer, job/output, evidence, degradation, and System Release Decision language.
- Put a decision in root `docs/adr/` when it changes ownership or relationships between contexts.
- Put a decision in a context's `docs/adr/` when only that context owns its consequences.
- Preserve external ownership: `governance/**` defines DEGS, and the AI-Workspace root defines Workbench/Command Center routing.

## Decision conflicts

If proposed work contradicts an existing root or context ADR, identify the conflict explicitly rather than silently overriding the decision. A context-local decision cannot override a cross-context boundary.
