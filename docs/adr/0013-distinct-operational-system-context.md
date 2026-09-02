---
status: accepted
---

# Keep the Operational System as a distinct bounded context

DobeWorks previously used one repository context whose root glossary owns the complete name, private-personal scope, identity, and provenance language; the AI-Workspace root separately owns Workbench and Command Center terminology, while `governance/**` owns DEGS. The Operational System is a distinct bounded context at `contexts/operational-system/`; `CONTEXT-MAP.md` records the relationship, the existing root `CONTEXT.md` remains unchanged, and future context-specific ADRs live under `contexts/operational-system/docs/adr/`.

## Considered options

- **Merge operational terminology into the existing root context.** Rejected because identity/provenance and operational lifecycle concepts have different ownership and change pressures, and a silent merge was expressly prohibited.
- **Place the operational context at the AI-Workspace root.** Rejected because the root owns the Workbench/Command Center control plane and cross-workspace routing, not DobeWorks mission data or device-role dispositions.
- **Create a sibling repository.** Rejected for v1 because it introduces a second DobeWorks project source of truth and additional synchronization/provenance seams without a demonstrated isolation need.
- **Create a distinct context inside the existing private repository.** Selected because it preserves one DobeWorks project owner while making boundaries, interfaces, terminology, and ADR placement explicit.

## Consequences

- The DobeWorks repository would deliberately become multi-context and its project domain instructions would need a reviewed update.
- The existing DobeWorks root glossary and ADRs remain authoritative for the name, private scope, identity, and provenance.
- The Operational System context owns mission, roles, data/recovery classes, requirements, configurations, evidence, operations, maintenance, and retirement.
- The root Workbench control plane and DEGS remain external sources; the Operational System references their interfaces without copying or redefining their terms.
- Establishing the canonical context records ownership and program definitions only. It does not qualify a device, begin Phase 2, authorize implementation, or change the existing Private Use and Public Release boundaries.
