# Auto-generated integration for observability
# Rule: canonical performance security events ekle
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: canonical performance security events ekle
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('canonical performance security events ekle')
    return cautions
