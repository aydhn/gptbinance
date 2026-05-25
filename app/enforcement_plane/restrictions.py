# Auto-generated integration for enforcement
# Rule: restriction lifted on unfunded promise explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: restriction lifted on unfunded promise explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('restriction lifted on unfunded promise explicit caution üretsin')
    return cautions
