# Phase 2 Entry Criteria — Read-Only Qualification

Phase 2 is not authorized by this document. Every required gate below must pass, then Taylor must separately authorize Phase 2 after a fresh context-opening check.

## Required Phase 1 closure

- [x] Taylor has explicitly resolved `DEC-001` through `DEC-007`; no decision is inferred.
- [x] The accepted values are synchronized into the spec, requirements, traceability matrix, fault matrix, and DEGS task record.
- [x] Taylor has accepted the proposed canonical home and context relationship.
- [x] `validation/validate_phase1.py --completion` passes.
- [x] The canonical DEGS schema validates `degs/phase1-task.json`.
- [x] Deterministic DEGS evaluation of the completed Phase 1 record is `PASS` with no warning.
- [x] Source hashes and security invariants match the Phase 1 source register.
- [x] No out-of-scope or canonical mutation occurred during staging.
- [x] The Phase 1 package is handed back to Taylor and Phase 1 stops without Phase 2 work.

## Canonical ownership prerequisite

- [x] The permanent operational context home has been accepted.
- [x] Any canonical promotion is separately scoped, authorized, identity-mapped, validated, reversible, and completed without duplicating a source of truth.
- [x] The promoted operational glossary and ADR placement match the accepted Phase 1 decision.
- [ ] Phase 2 evidence has one exact canonical destination before collection begins.

## Phase 2 task definition prerequisite

- [ ] A separate Phase 2 DEGS task record defines exact read-only targets, commands/methods, evidence destinations, privacy-safe identifiers, stop conditions, physical/human actions, and forbidden paths.
- [ ] The task remains in `TAYLOR_AI_WORKBENCH`; AgentOps has no delegation.
- [ ] PRIVATE VAULT, credential stores, secret values, full serials, and unrelated user content remain excluded.
- [ ] Historical values are explicitly planning context and will not be copied forward as current measurements.
- [ ] The qualification plan states which evidence can be gathered without additional permission and which Taylor-only action would be required.
- [ ] No permission request, Full Disk Access action, Seagate/Time Machine content inspection, or 2015 MacBook physical action occurs without its own exact human step and authority check.
- [ ] Read-only evidence collection cannot repair, mount, unmount, write, install, update, reconfigure, delete, reorganize, repartition, erase, sanitize, or wipe.

## Phase 2 planned outputs

- refreshed, privacy-safe current-Mac qualification baseline;
- exact Seagate device/volume evidence available within the authorized read-only surface, with inaccessible topology left `UNKNOWN`;
- exact 2015 MacBook evidence only if Taylor performs separately defined physical steps; otherwise `BLOCKED_PENDING_EVIDENCE` remains valid;
- current Observer feasibility/surface inventory without implementation;
- discrepancies and explicit unknowns;
- evidence identities ready for Phase 3 architecture and Role Disposition decisions.

## Hard stop conditions

- drift in context, governance, source identity, or canonical destination;
- reappearance of the governance lock or an active conflicting writer;
- any required access to PRIVATE VAULT, credential values, recovery keys, full serials, or unrelated private content;
- any command or UI step that can write, repair, mutate permissions, alter Time Machine, or change a device;
- pressure to infer a backup identity, exact Mac model, security-support state, fitness, redundancy, or recoverability;
- need for a purchase, physical action, credential action, destructive action, or wider authority not separately granted; or
- attempt to begin Phase 3 from a qualification result without a new phase boundary and authorization.
