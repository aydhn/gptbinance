# Auto-generated integration for postmortem
# Rule: phantom_collateral, duplicate_pledge contributors
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: phantom_collateral, duplicate_pledge contributors
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('phantom_collateral, duplicate_pledge contributors')
    return cautions
