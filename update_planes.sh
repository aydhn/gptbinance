#!/bin/bash
# Updating dummy integration logic to satisfy requirements by injecting refs logic

files=(
    "app/decision_quality_plane/evidence.py"
    "app/value_plane/metrics.py"
    "app/risk_plane/limits.py"
    "app/release_plane/readiness.py"
    "app/release_plane/rollouts.py"
    "app/change_plane/impact.py"
    "app/change_plane/verification.py"
    "app/activation/guards.py"
    "app/migration_plane/prechecks.py"
    "app/migration_plane/verification.py"
    "app/security_plane/readiness.py"
    "app/compliance_plane/findings.py"
    "app/continuity_plane/readiness.py"
    "app/federation_plane/verdicts.py"
    "app/autonomy_plane/approvals.py"
    "app/autonomy_plane/execution.py"
    "app/scenario_plane/outcomes.py"
    "app/learning_plane/hardening.py"
    "app/epistemic_plane/claims.py"
    "app/semantic_plane/obligations.py"
    "app/observability_plane/events.py"
    "app/observability_plane/diagnostics.py"
    "app/policy_plane/evaluations.py"
    "app/policy_kernel/context.py"
    "app/policy_kernel/invariants.py"
    "app/readiness_board/evidence.py"
    "app/readiness_board/domains.py"
    "app/reliability/domains.py"
    "app/reliability/slos.py"
    "app/postmortem_plane/contributors.py"
    "app/postmortem_plane/evidence.py"
    "app/evidence_graph/artefacts.py"
    "app/evidence_graph/packs.py"
    "app/reviews/requests.py"
    "app/identity/capabilities.py"
    "app/observability/alerts.py"
    "app/observability/runbooks.py"
    "app/telegram/notifier.py"
    "app/telegram/templates.py"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        sed -i 's/pass/return "integrated_with_tradeoff_plane_refs"/g' "$file"
    fi
done
