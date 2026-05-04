from app.observability.models import RunbookRef
# Integration hook for ledger accounting phase 35

# Ledger accounting integration hook for phase 35 (balance provenance)


# Added in Phase 38
def add_stress_runbook_refs(self):
    pass


_RUNBOOK_REGISTRY["capital_escalation_blocked"] = RunbookRef(
    runbook_id="capital_escalation_blocked",
    title="Capital Escalation Blocked",
    url="docs/runbooks/capital_escalation_blocked.md"
)

_RUNBOOK_REGISTRY["capital_freeze_advisory"] = RunbookRef(
    runbook_id="capital_freeze_advisory",
    title="Capital Freeze Advisory",
    url="docs/runbooks/capital_freeze_advisory.md"
)

_RUNBOOK_REGISTRY["tranche_activation_caution"] = RunbookRef(
    runbook_id="tranche_activation_caution",
    title="Tranche Activation Caution",
    url="docs/runbooks/tranche_activation_caution.md"
)

_RUNBOOK_REGISTRY["stale_evidence_live_caution"] = RunbookRef(
    runbook_id="stale_evidence_live_caution",
    title="Stale Evidence During Live Caution",
    url="docs/runbooks/stale_evidence_live_caution.md"
)

_RUNBOOK_REGISTRY["loss_budget_breach"] = RunbookRef(
    runbook_id="loss_budget_breach",
    title="Loss Budget Breach",
    url="docs/runbooks/loss_budget_breach.md"
)

# Added in Phase 40
def add_crossbook_runbook_refs(self):
    pass
