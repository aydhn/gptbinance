def evaluate_risk_block(verdict):
    if verdict.verdict_class.name == "DENY":
        return True
    return False
