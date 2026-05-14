def check_recovery_capacity_allocations():
    pass



# Cost plane evaluation integration
def prevent_unbounded_recovery_spend(unbounded_emergency_spend: bool):
    if unbounded_emergency_spend:
         return "caution"
    return "ready"
