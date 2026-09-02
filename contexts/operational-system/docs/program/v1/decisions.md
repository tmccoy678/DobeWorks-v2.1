# Taylor Decision Register

These are human value judgments, not facts derived from the research. Taylor explicitly accepted `DEC-001` through `DEC-007` as recommended on 2026-09-01 at 16:45 CDT. Acceptance makes the Phase 1 requirements testable; it does not qualify a device, promote the canonical home, authorize Phase 2, accept later residual risk, or authorize Public Release.

## DEC-001 — Loss and downtime budgets

**Accepted decision: use the following service classes.**

| Class | Scope | Proposed RPO | Proposed RTO | Rationale and boundary |
|---|---|---:|---:|---|
| `S0_ACCEPTED_STATE` | Accepted requirements, configuration, manifests, evidence index, and promoted authoritative artifacts | `0` after Promotion Event | 24 hours | State is not considered accepted until an independent recoverable copy is evidenced; zero applies to accepted state, not an unsaved draft |
| `S1_ACTIVE_WORK` | Active private engineering work not yet promoted | 24 hours | 24 hours | Bounded personal-work loss while avoiding unsupported continuous-replication assumptions |
| `S2_IRREPLACEABLE` | Any in-scope `R3_IRREPLACEABLE` data | `0` after controlled intake | 72 hours | Source retirement is prohibited until two independent protected copies exist and representative restore is proven |
| `S3_REBUILDABLE` | Worker tooling, clones, caches, temporary artifacts, reproducible telemetry views | Not applicable; source must remain available | 72 hours | Recovery is rebuild from an approved source, not backup of disposable state |

`RPO 0` here is a commit rule requiring verified independent copies before acceptance; it is not a claim of continuous availability.

Status: `ACCEPTED`

## DEC-002 — Worker exposure ceiling

**Accepted decision:** the Worker may initiate only job-required outbound connections to approved sources; it exposes no public inbound service; receives no broad or reusable credential values; processes only `C0`, `C1`, and specifically approved `C2` copies; never receives `C3`, `CX`, `R3`, or sole-copy `R2` data; and cannot promote output. If its exact operating system is outside the security-support boundary required for a networked role, qualify it out of networked work. Any offline synthetic-only role requires its own explicit contract.

Status: `ACCEPTED`

## DEC-003 — Observer retention and action timing

**Accepted decision:** retain raw permitted operational events locally for 30 days, daily aggregates for 180 days, and release/audit evidence according to the evidence-retention policy rather than telemetry retention. Stop-relevant conditions block the next affected dispatch immediately; actionable warnings are presented within one day; trend-only findings are reviewed weekly. No content, private filenames, secret values, full serials, or PRIVATE VAULT data may be retained at any duration.

Status: `ACCEPTED`

## DEC-004 — Patch and support policy

**Accepted decision:** both Control Plane and any networked Worker must run an operating-system release receiving applicable security updates. Apply actively exploited or critical applicable security fixes within 72 hours, other applicable security fixes within 14 days, and feature updates only after a supported recovery point, compatibility test, and rollback plan. If the Worker falls outside required security support, suspend its networked role and qualify it out unless Taylor later accepts a separately analyzed compensating design.

Status: `ACCEPTED`

## DEC-005 — Qualification-out and replacement boundary

**Accepted decision:** no sunk-cost exception. Qualify a candidate out when it cannot meet an essential role requirement after one bounded evidence/remediation cycle; lacks required supported software for its exposure; fails relevant diagnostics or representative workload stability; cannot be rebuilt or recovered within its accepted RTO; or requires authority, data placement, or risk outside the v1 contract. Repair-versus-replacement spending remains `UNKNOWN` until exact device facts and actual quotes exist and requires Taylor's separate purchase/value decision.

Status: `ACCEPTED`

## DEC-006 — Residual-risk boundary

**Accepted decision:** the following are absolute no-go conditions for a clean System Release Decision:

- any critical `UNKNOWN` concerning recovery, privacy, security, data loss, exact device fitness, or authoritative source identity;
- sole-copy `R2` or `R3` data on the Seagate or Worker;
- exposed unsupported Worker software handling credentials, private content, or authoritative output;
- missing representative restore, Control Plane recovery, Worker rebuild, or accepted fault evidence;
- telemetry that captures prohibited data, remediates automatically, or reports silence as health;
- mismatch between reviewed, tested, executed, and handed-off artifacts;
- non-independent audit or unresolved critical audit finding; or
- any inferred credential, physical, destructive, exception, or residual-risk authority.

Taylor may consider only noncritical warnings after fixed evidence and independent review, such as lower-than-preferred performance, delayed low-value work, a nonessential telemetry gap with explicit `UNKNOWN`, or a platform diagnostic unavailable through a bridge when other bounded evidence is sufficient. Acceptance must name the warning and does not establish a reusable exception.

Status: `ACCEPTED`

## DEC-007 — Canonical home and context relationship

**Accepted decision:** use `projects/dobeworks/contexts/operational-system/` as the permanent home; deliberately convert the private DobeWorks repository to an explicit multi-context layout; retain the existing root `CONTEXT.md`; add a context map; place the boundary decision at `projects/dobeworks/docs/adr/0013-distinct-operational-system-context.md`; and place future context-only ADRs beneath the Operational System context.

No canonical promotion is authorized by accepting the recommendation alone. Promotion requires a separately scoped, verified file change after Phase 1.

Status: `ACCEPTED`

## Acceptance record

Taylor's exact in-band decision was: `Accept DEC-001 through DEC-007 as recommended.` No broader authority is inferred from that statement.
