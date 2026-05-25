# Auto-generated integration for reviews
# Rule: performance_security_integrity_review
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: performance_security_integrity_review
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('performance_security_integrity_review')
    return cautions
