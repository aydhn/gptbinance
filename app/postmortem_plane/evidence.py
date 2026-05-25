# Auto-generated integration for postmortem_ev
# Rule: securities and residual under-security refs export
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: securities and residual under-security refs export
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('securities and residual under-security refs export')
    return cautions
