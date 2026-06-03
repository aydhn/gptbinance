# Meta-Governance Plane / Canon-Evolution Governance Layer

## Purpose
In a corporate system, as governance layers multiply, the actual risk is the inability to manage governance itself. A rule in one plane may conflict with an obligation in another; a hotfix might act like a permanent canon; legacy semantics might never die; what is deprecated might continue to live in runtime; a new rule may silently alter the meaning of old decisions.

If rule/canon/version/supersession/deprecation/migration semantics are not typed, the system generates governance chaos. This is why proposals, canon versions, dependencies, supersession, deprecation, migration, compatibility, conflicts, history, and trust require a dedicated governance layer.

## Proposals/Canons -> Supersession/Deprecation -> Migration/History -> Trust Flow
The flow of meta-governance is explicit:
1. **Proposals & Canons**: Changes to governance must go through typed proposals and result in new canon versions.
2. **Supersession & Deprecation**: Rules cannot just be "updated". The old rule must be explicitly superseded, or safely deprecated with a sunset trigger.
3. **Migration & History**: Consumers of the rule must migrate, and the historical truth of the old rule's existence and impact must be preserved.
4. **Trust**: Meta-Governance trust is evaluated based on canon clarity, lineage integrity, supersession safety, migration completeness, and history preservation.

## Why Updated != Superseded != Migrated != Canon-Safe
- **Updated** just means the text changed. **Superseded** means the new version explicitly takes over the old version's scope with a clear revocation path.
- **Superseded** means the old rule is no longer active canon. **Migrated** means the system actually stopped using the old rule and fully transitioned to the new one.
- **Migrated** means the transition is complete. **Canon-Safe** means the history of the old rule is preserved, and no shadow canons or silent rewrites exist.

## Why No Shadow Canon / No Silent Rewrite
- **Shadow Canons** are unofficial rules acting as canon. They bypass governance and create unpredictable behavior.
- **Silent Rewrites** change the meaning of rules without leaving a trace, destroying historical truth and accountability.

## Boundaries of this Phase
This phase does NOT create a generic config versioning system. It does NOT hide canon split paths. It does NOT treat a new rule doc as a true governance migration. It ONLY establishes institutional governance-evolution discipline by explicitly tracking meta-governance truth.
