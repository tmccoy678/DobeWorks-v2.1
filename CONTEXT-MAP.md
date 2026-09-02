# DobeWorks Context Map

## Contexts

- [DobeWorks](CONTEXT.md) — owns the complete name, private-personal scope, identity, mark, and provenance language.
- [Operational System](contexts/operational-system/CONTEXT.md) — owns hardware/software mission, roles, data and recovery classes, requirements, configuration, evidence, operations, maintenance, and retirement.

## Relationships

- **Operational System → DobeWorks**: The Operational System belongs to DobeWorks and inherits its Private Use and Public Release boundaries without redefining the name or identity.
- **Operational System ↔ Taylor AI Workbench and Command Center**: The Operational System uses the external supervised implementation and routing interfaces defined by [AI-Workspace domain guidance](../../docs/agents/domain.md); it does not own or rename them.
- **Operational System → DEGS**: The Operational System supplies task records and evidence to the external [DEGS sources](../../governance/); it does not copy DEGS policy or treat a gate result as execution authority.

## Decision placement

- Cross-context and repository-shape decisions live under `docs/adr/`.
- Decisions owned only by the Operational System live under `contexts/operational-system/docs/adr/` when the first such decision is recorded.
- The context map and each context glossary contain vocabulary and ownership only; program requirements and implementation details live outside the glossaries.
