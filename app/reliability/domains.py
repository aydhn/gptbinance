# Auto-generated integration for reliability
# Rule: phantom collateral and under-security reliability inputs
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: phantom collateral and under-security reliability inputs
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('phantom collateral and under-security reliability inputs')
    return cautions
