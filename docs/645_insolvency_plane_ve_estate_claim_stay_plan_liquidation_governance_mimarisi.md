# Phase 127: Insolvency Plane and Estate/Claim/Stay/Plan/Liquidation Governance

## Purpose
The Insolvency Plane provides canonical governance for institutional insolvency events. It ensures that performance failure, settlement defaults, and recovery shortfalls are managed via a strictly typed lifecycle (trigger -> estate -> claims -> stays -> plans -> distributions -> trust) rather than opaque "system-down" states.

## Why 'Filed' != 'Allowed' != 'Paid' != 'Closed'
- **Filed Claim**: Merely an assertion against the estate.
- **Allowed Claim**: Judicially or administratively admitted to the estate.
- **Paid**: Distributions actually sent to the beneficiary, leaving no residual deficit.
- **Closed**: All duties executed; the estate has no leakages and no outstanding contests.
Equating these states leads to priority inversions and hidden deficit debt.

## Estate Leakage Prevention
Estates must be completely scoped. Assets cannot secretly exit the estate boundary (leakage) without formal avoidance or distribution records. Any unrecorded exit degrades the Insolvency Trust Verdict to "blocked" or "degraded".

## The Governance Logic
We separate facts from assertions. A user can file a claim, but that does not guarantee priority. A plan can be supported, but it is not binding until explicitly *confirmed*. This ensures recovery, liability, and settlement decisions base their conclusions on hard facts, not "restructuring theater".
