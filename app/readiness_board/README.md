# Release Readiness Board & Evidence Court

This module implements Phase 50 of the system, establishing a strict evidence court and release readiness board.

## Philosophy

A candidate cannot simply be promoted or released because a single report or experiment looks promising.
Instead, we require:
1. **Candidate Freeze**: An immutable snapshot of what is being evaluated.
2. **Evidence Court**: Admissibility checks on all supporting evidence (rejecting stale or out-of-scope evidence).
3. **Contradiction Resolution**: Handling cases where different domains report conflicting readiness states.
4. **Final Decision**: Go, No-Go, Hold, Needs Review, or Conditional Go.
5. **Final Memo**: An auditable document summarizing the decision.

**This module does NOT perform direct live activation.** It only produces the decision and memo that downstream orchestration uses.
