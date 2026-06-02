# Phase 137 - Orchestration Plane Governance Architecture

## Neden Orchestration Plane Gerekiyor?
Kurumsal sistemlerde "planned" != "dispatched" != "executed" != "verified".
Execution theater, orphan handoffs, skipped approvals ve hidden automation gibi
sorunları engellemek için action graph, rollback path ve compensation net olarak
typed bir governance modeline oturtulmuştur.

## Workflow vs. Governance
Bu katman düz bir workflow runner değildir. Executed ile Safely Closed arasındaki
farkı kanıtlayan (evidence-based) bir orkestrasyon kanıt (truth) motorudur.
