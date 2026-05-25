# Auto-generated integration for observability_diag
# Rule: reserve count alone performance security truth yerine geçmesin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: reserve count alone performance security truth yerine geçmesin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('reserve count alone performance security truth yerine geçmesin')
    return cautions
