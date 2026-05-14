def check_compliance_capacity_findings():
    pass



# Cost plane evaluation integration
def emit_missing_budget_guardrails_finding(budget_guardrails_missing: bool):
    findings = []
    if budget_guardrails_missing:
        findings.append("Missing budget guardrails")
    return findings
