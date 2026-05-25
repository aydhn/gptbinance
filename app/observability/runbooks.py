# Auto-generated integration for observability_runbooks
# Rule: performance_security_drift_cleanup_review
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: performance_security_drift_cleanup_review
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('performance_security_drift_cleanup_review')
    return cautions
