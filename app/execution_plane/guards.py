def enforce_execution_guard(verdict):
    if verdict.verdict_class.name == "DENY":
        raise Exception("Execution blocked by policy")
