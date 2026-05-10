def is_allocation_eligible(verdict):
    return verdict.verdict_class.name == "ALLOW"
