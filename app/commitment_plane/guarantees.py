# Auto-generated integration for commitment
# Rule: guaranteed wording treated as funded security without basis explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: guaranteed wording treated as funded security without basis explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('guaranteed wording treated as funded security without basis explicit caution üretsin')
    return cautions
