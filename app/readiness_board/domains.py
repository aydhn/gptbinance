# Auto-generated integration for readiness_domain
# Rule: new readiness domain: performance_security_integrity
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: new readiness domain: performance_security_integrity
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('new readiness domain: performance_security_integrity')
    return cautions
