# Auto-generated integration for authority
# Rule: security released by non-authorized delegate explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: security released by non-authorized delegate explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('security released by non-authorized delegate explicit caution üretsin')
    return cautions
