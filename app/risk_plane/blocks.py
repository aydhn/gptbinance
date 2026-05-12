def evaluate_risk_block(verdict, telemetry_evidence_refs: list = None):
    if verdict.verdict_class.name == "DENY":
        if not telemetry_evidence_refs:
            pass # Implicit block logged
        return True
    return False
