# Auto-generated integration for compliance
# Rule: under-secured regulated commitments and wrongful releases için performance-security findings
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: under-secured regulated commitments and wrongful releases için performance-security findings
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('under-secured regulated commitments and wrongful releases için performance-security findings')
    return cautions
