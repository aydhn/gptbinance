# Auto-generated integration for evidence_graph
# Rule: performance security objects artefact family
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: performance security objects artefact family
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('performance security objects artefact family')
    return cautions
