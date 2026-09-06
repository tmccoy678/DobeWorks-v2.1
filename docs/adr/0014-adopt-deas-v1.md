---
status: accepted
---

# Adopt DEAS v1.0 as the DobeWorks engineering-assurance baseline

DobeWorks needs one cross-context way to prevent defects in code, documents, validators, evidence, Git history, and AI-assisted work. We adopt the DobeWorks Engineering Assurance Standard v1.0 as a prospective repository baseline, adapting the preventive intent of the Power of Ten into Core, Strict, and Exploratory profiles plus context overlays instead of copying a C-specific checklist or relying on ad hoc review.

## Consequences

- Every accepted change selects a DEAS profile and every applicable overlay.
- Strict work receives deterministic limits, semantic checks, negative tests, exact artifact identity, and a Git-first review boundary.
- Exploratory work remains visibly provisional and cannot promote itself.
- An exception is explicit, scoped, temporary, evidenced, and human-approved; it never supplies missing task authority.
- This decision does not certify or release DobeWorks, retroactively rewrite history, or adopt DEAS outside this repository.
