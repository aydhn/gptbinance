def export_capacity_evidence():
    pass



# Cost plane evaluation integration
def append_cost_postmortem_bundles(existing_bundles):
    existing_bundles.extend(["spend_lineage", "budget_lineage"])
    return existing_bundles
