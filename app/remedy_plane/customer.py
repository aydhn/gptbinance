# Auto-generated integration for remedy
# Rule: promised compensation without secured execution path explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: promised compensation without secured execution path explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('promised compensation without secured execution path explicit caution üretsin')
    return cautions
