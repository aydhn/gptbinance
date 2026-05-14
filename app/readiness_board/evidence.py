def add_capacity_evidence():
    pass



# Cost plane evaluation integration
def check_critical_cost_integrity(critical_cost_integrity_failures: bool):
    if critical_cost_integrity_failures:
        return "blocked"
    return "ready"
