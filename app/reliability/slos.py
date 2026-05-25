# Auto-generated integration for reliability_slo
# Rule: performance security integrity SLO families
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: performance security integrity SLO families
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('performance security integrity SLO families')
    return cautions
