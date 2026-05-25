# Auto-generated integration for policy_inv
# Rule: no trusted high-risk closure while material promised performance remains unsecured
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: no trusted high-risk closure while material promised performance remains unsecured
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('no trusted high-risk closure while material promised performance remains unsecured')
    return cautions
