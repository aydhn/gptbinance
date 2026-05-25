# Auto-generated integration for state
# Rule: state reconciled but performance security still impaired explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: state reconciled but performance security still impaired explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('state reconciled but performance security still impaired explicit caution üretsin')
    return cautions
