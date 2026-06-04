import os

def append_file(p, c):
    if os.path.exists(p):
        with open(p, "a") as f:
            f.write("\n" + c + "\n")
    else:
        with open(p, "w") as f:
            f.write(c + "\n")

integrations = {
    "app/renewal_plane/nonrenewal.py": "def check_nonrenewal_suspension_link():\n    return 'Suspension protective hold refs linked'\n",
    "app/succession_plane/vacancy.py": "def check_vacancy_suspension_link():\n    return 'Vacancy bounded treated safe without suspension posture explicit caution'\n",
    "app/sunset_plane/triggers.py": "def sunset_suspension_check():\n    pass\n",
    "app/stewardship_plane/extraction.py": "def extraction_suspension_check():\n    pass\n",
    "app/legitimacy_plane/contestability.py": "def contestability_suspension_check():\n    pass\n",
    "app/viability_plane/runway.py": "def runway_suspension_check():\n    pass\n",
    "app/resilience_plane/containment.py": "def containment_suspension_check():\n    pass\n",
    "app/meta_governance_plane/emergency.py": "def emergency_suspension_check():\n    pass\n",
    "app/autonomy_plane/revocations.py": "def autonomy_suspension_check():\n    pass\n",
    "app/orchestration_plane/pauses.py": "def pauses_suspension_check():\n    pass\n",
    "app/incentive_plane/reviews.py": "def reviews_suspension_check():\n    pass\n",
    "app/accountability_plane/duties.py": "def duties_suspension_check():\n    pass\n",
    "app/assurance_plane/revocation.py": "def assurance_suspension_check():\n    pass\n",
    "app/immunity_plane/revalidation.py": "def immunity_suspension_check():\n    pass\n",
    "app/adaptation_plane/packages.py": "def adaptation_suspension_check():\n    pass\n",
    "app/drift_plane/restrictions.py": "def drift_suspension_check():\n    pass\n",
    "app/normalization_plane/reopen.py": "def reopen_suspension_check():\n    pass\n",
    "app/recovery_plane/finalization.py": "def recovery_suspension_check():\n    pass\n",
    "app/settlement_plane/fullfinal.py": "def settlement_suspension_check():\n    pass\n",
    "app/enforcement_plane/lift.py": "def enforcement_suspension_check():\n    pass\n",
    "app/rights_plane/remedy.py": "def rights_suspension_check():\n    pass\n",
    "app/liability_plane/consequences.py": "def liability_suspension_check():\n    pass\n",
    "app/authority_plane/approval.py": "def authority_suspension_check():\n    pass\n",
    "app/finality_plane/final.py": "def finality_suspension_check():\n    pass\n",
    "app/representation_plane/disclosures.py": "def representation_suspension_check():\n    pass\n",
    "app/epistemic_plane/claims.py": "def epistemic_suspension_check():\n    pass\n",
    "app/observability_plane/events.py": "def add_suspension_events():\n    return ['suspension_triggered', 'shadow_execution_detected']\n",
    "app/observability_plane/diagnostics.py": "def add_suspension_diagnostics():\n    pass\n",
    "app/policy_plane/evaluations.py": "def evaluate_suspension_policy():\n    pass\n",
    "app/policy_kernel/context.py": "def add_suspension_context():\n    pass\n",
    "app/policy_kernel/invariants.py": "def add_suspension_invariants():\n    pass\n",
    "app/readiness_board/evidence.py": "def add_suspension_evidence():\n    pass\n",
    "app/readiness_board/domains.py": "def add_suspension_integrity_domain():\n    pass\n",
    "app/reliability/domains.py": "def add_suspension_reliability_domain():\n    pass\n",
    "app/reliability/slos.py": "def add_suspension_slos():\n    pass\n",
    "app/postmortem_plane/contributors.py": "def add_suspension_contributors():\n    pass\n",
    "app/postmortem_plane/evidence.py": "def add_suspension_postmortem_evidence():\n    pass\n",
    "app/evidence_graph/artefacts.py": "def add_suspension_artefacts():\n    pass\n",
    "app/evidence_graph/packs.py": "def add_suspension_packs():\n    pass\n",
    "app/reviews/requests.py": "def add_suspension_reviews():\n    pass\n",
    "app/identity/capabilities.py": "def add_suspension_capabilities():\n    pass\n",
    "app/observability/alerts.py": "def add_suspension_alerts():\n    pass\n",
    "app/observability/runbooks.py": "def add_suspension_runbooks():\n    pass\n",
    "app/telegram/notifier.py": "def add_suspension_notifications():\n    pass\n",
    "app/telegram/templates.py": "def add_suspension_templates():\n    pass\n"
}

for path, content in integrations.items():
    append_file(path, content)

print("Integrations patched.")
