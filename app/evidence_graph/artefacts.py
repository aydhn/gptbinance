def register_capacity_artefacts():
    pass



# Cost plane evaluation integration
def append_cost_artefacts(families, relations):
    families.extend(["cost_objects", "spend", "fees"])
    relations.extend(["costed_by", "budgeted_under", "allocated_to", "amortized_under"])
    return families, relations
