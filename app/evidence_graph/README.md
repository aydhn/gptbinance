# Evidence Graph & Queryable Governance Memory

This layer provides an immutable, audit-grade graph of all system decisions, incidents, experiments, and policies.

## Key Principles
1. **No Hallucination**: Relations are explicit and typed. If it's not in the graph, it doesn't exist.
2. **Immutability**: Source artefacts are never mutated. We only build indexes and relations.
3. **Scope & Redaction**: Queries respect workspace, profile, and domain boundaries. Restricted data is clearly marked as redacted.
4. **Lineage & Dependency**: Enables backward tracing ("why did we do this?") and forward tracing ("what depends on this?").

## Components
- `artefacts.py`: Registry for typed artefacts (Memos, Incidents, etc).
- `relations.py`: Typed relation registry (DERIVED_FROM, INVALIDATED_BY).
- `lineage.py` & `dependencies.py`: Traversal logic.
- `cases.py` & `packs.py`: Assemblers for review cases and evidence bundles.
- `queries.py`: Explicit, scope-aware querying.
- `gaps.py`: Detection of broken chains or dangling evidence.
