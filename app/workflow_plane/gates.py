def check_gate(policy_verdict):
    if policy_verdict.verdict_class.name == "DENY":
        raise Exception("Gate blocked by policy")
