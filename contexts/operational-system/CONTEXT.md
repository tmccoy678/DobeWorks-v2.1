# Operational System

The Operational System is the bounded DobeWorks context for Taylor's private hardware, software, storage, worker execution, telemetry, recovery, maintenance, and retirement. It defines operational roles and evidence without redefining the DobeWorks name, identity, or provenance context; the Taylor AI Workbench and DEGS remain external systems with explicit interfaces.

## Language

**Operational System**:
The private system of roles, contracts, evidence, and lifecycle decisions that supports Taylor's DobeWorks engineering work across the control plane, storage resources, workers, and observer.
_Avoid_: DobeWorks Operations, public service, hardware collection

**Control Plane**:
The authoritative, Taylor-supervised operational role that holds approved configuration, dispatches bounded jobs, validates returned outputs, records evidence, and orchestrates recovery. A device is not the Control Plane until it is qualified for that role.
_Avoid_: Main computer, automatic authority, Command Center

**Storage Resource**:
A physical device or logical volume considered for one or more explicitly classified storage roles. Connection or readability alone does not qualify a Storage Resource.
_Avoid_: Backup, archive, safe disk

**Storage Role**:
A bounded purpose assigned to a qualified Storage Resource, such as backup target, archive, transfer medium, or scratch space, together with its data, recovery, capacity, and retirement contract.
_Avoid_: General storage, mixed-use disk

**Worker**:
A rebuildable, non-authoritative executor that accepts a bounded Job Envelope and returns Staged Output. A Worker never holds sole-copy important data or promotes its own results.
_Avoid_: Control plane, autonomous agent, authoritative node

**Observer**:
The local, read-only telemetry role that reports purpose-bound operational metadata and its own health. It cannot remediate, authorize, or convert missing data into a healthy state.
_Avoid_: Autopilot, monitoring control plane, remediation agent

**Job Envelope**:
The immutable operational contract for one Worker execution, including job identity, input and configuration digests, data class, delivery semantics, expiry, retry/cancellation rules, and expected output.
_Avoid_: Prompt, loose task, command bundle

**Staged Output**:
A Worker result held outside authoritative state until the Control Plane verifies its identity, integrity, semantics, and acceptance criteria.
_Avoid_: Final output, accepted evidence, canonical artifact

**Promotion Event**:
The explicit, evidenced Control Plane event that accepts a specific Staged Output into an authorized source of truth after required validation. Promotion cannot be performed by the Worker or Observer.
_Avoid_: File copy, successful exit, automatic sync

**Role Disposition**:
The evidence-backed result for a candidate device or component: `QUALIFIED_FOR_BOUNDED_ROLE`, `QUALIFIED_OUT`, or `BLOCKED_PENDING_EVIDENCE`.
_Avoid_: Healthy, passed diagnostics, probably suitable

**Evidence Set**:
The indexed objective records tied to exact requirements, configurations, roles, tests, and results for a defined claim.
_Avoid_: Notes folder, screenshots alone, gate result

**Frozen Evidence Set**:
An Evidence Set whose complete manifest and artifact identities are fixed before independent review so reviewed evidence cannot change silently.
_Avoid_: Current folder, latest results, editable audit packet

**Safe Degradation**:
An explicitly permitted reduced service state that preserves authority, data, privacy, and recovery boundaries while a fault or unknown remains unresolved.
_Avoid_: Best effort, silent fallback, automatic bypass

**System Release Decision**:
Taylor's explicit acceptance of one fixed Operational System baseline for Private Use after objective evidence, deterministic DEGS evaluation, and independent review. It is separate from an identity Personal Release and never authorizes Public Release.
_Avoid_: Deployment complete, gate approval, certification
