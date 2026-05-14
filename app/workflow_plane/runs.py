def record_workflow_run_capacity(run_id: str, allocations: list):
    pass



# Cost plane evaluation integration
def detect_workflow_cost_debt(retries: int):
    if retries > 3:
         return "exported_to_debt_surface"
    return "ok"
