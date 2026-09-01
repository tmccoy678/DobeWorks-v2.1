# Domain Docs

## Before exploring

Read:

- `CONTEXT.md` at the repository root, if it exists
- Relevant decisions under `docs/adr/`

If these files do not yet exist, proceed silently. `/domain-modeling`, normally reached through `/grill-with-docs`, creates them when terms or decisions are actually resolved.

## Layout

This is a single-context repository:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
└── src/
```

## Vocabulary

Use terms exactly as defined in `CONTEXT.md`. Do not drift to synonyms the glossary explicitly avoids.

If a needed concept is absent, reconsider whether the term belongs or record the gap for `/domain-modeling`.

## Decision conflicts

If proposed work contradicts an existing ADR, identify the conflict explicitly rather than silently overriding the decision.
