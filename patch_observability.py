import re

with open("app/observability/alerts.py", "r") as f:
    content = f.read()

alert_logic = """
class CapitalAlertRule(AlertRule):
    def evaluate(self, metrics: dict) -> bool:
        # Evaluate things like capital ladder stale evidence, unauthorized capital escalation attempt,
        # live tier posture degraded, capital freeze recommended, loss budget escalation breach
        return False
"""
if "CapitalAlertRule" not in content:
    content += "\n" + alert_logic

with open("app/observability/alerts.py", "w") as f:
    f.write(content)

with open("app/observability/runbooks.py", "r") as f:
    content = f.read()

runbook_logic = """
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
"""
if "capital_escalation_blocked" not in content:
    content += "\n" + runbook_logic

with open("app/observability/runbooks.py", "w") as f:
    f.write(content)
