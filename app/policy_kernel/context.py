# Auto-generated integration for policy_kernel
# Rule: high-risk actions için performance security sufficiency input’u olsun
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: high-risk actions için performance security sufficiency input’u olsun
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('high-risk actions için performance security sufficiency input’u olsun')
    return cautions
