# Auto-generated integration for identity
# Rule: inspect_performance_security_manifest
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: inspect_performance_security_manifest
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('inspect_performance_security_manifest')
    return cautions
