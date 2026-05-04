import re

# Update app/control/actions.py to include capital actions
with open("app/control/actions.py", "r") as f:
    content = f.read()

action_classes = """    capital_escalation = "capital_escalation"
    capital_reduction_apply = "capital_reduction_apply"
    capital_freeze_apply = "capital_freeze_apply"
    tranche_activation = "tranche_activation"
"""

if "capital_escalation" not in content:
    content = re.sub(r'(class ActionClass\(str, Enum\):)', r'\1\n' + action_classes, content)

with open("app/control/actions.py", "w") as f:
    f.write(content)


# Update app/control/authorization.py to include stale evidence logic
with open("app/control/authorization.py", "r") as f:
    content = f.read()

stale_logic = """
    if action.action_type in ["capital_escalation", "tranche_activation"]:
        # Specific check for capital operations: evidence freshness
        # Simulate evidence check
        has_stale_evidence = False # In a real implementation, this checks the CapitalEvidenceBundle
        if has_stale_evidence:
            return AuthorizationResult(
                is_authorized=False,
                decision_reason="Deny: Stale capital evidence detected despite available approvals."
            )
"""

if "capital_escalation" not in content:
    content = re.sub(r'(def authorize_action\(.*?\).*?:)', r'\1\n' + stale_logic, content, count=1)

with open("app/control/authorization.py", "w") as f:
    f.write(content)
