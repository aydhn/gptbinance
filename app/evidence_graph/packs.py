# Auto-generated integration for evidence_graph_packs
# Rule: performance security integrity pack
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: performance security integrity pack
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('performance security integrity pack')
    return cautions
