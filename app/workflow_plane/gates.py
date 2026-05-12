def check_gate(policy_verdict, missing_observability: bool = False):
    if policy_verdict.verdict_class.name == "DENY":
        raise Exception("Gate blocked by policy")
    if missing_observability:
        raise Exception("Gate blocked due to missing telemetry coverage")
