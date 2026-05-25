# Auto-generated integration for observability_alerts
# Rule: material_undersecurity_detected
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: material_undersecurity_detected
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('material_undersecurity_detected')
    return cautions
