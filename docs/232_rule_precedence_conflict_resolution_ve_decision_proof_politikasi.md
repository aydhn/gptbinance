# Rule Precedence, Conflict Resolution & Decision Proofs

## Precedence Resolution

Conflicts are resolved using a deterministic precedence hierarchy:
`HARD_BLOCK > BLOCK > CAUTION > ADVISORY > ALLOW`

Non-waivable invariants resulting in a `HARD_BLOCK` will override any `ALLOW` verdict, regardless of origin or waiver status.

## Conflict Resolution

Conflicts (e.g., one rule allowing an action while another blocks it) are detected and stored. Conflict resolution explicitly notes which rule took precedence based on severity.

## Decision Proof

A decision proof provides full visibility into the evaluation process. It answers:
- What rules were evaluated?
- What evidence was used?
- Which rules were overridden or waived?
- What is the final winning verdict and why?
