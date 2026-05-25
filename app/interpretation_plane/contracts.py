# Auto-generated integration for interpretation
# Rule: reserve text interpreted as beneficiary-controlled escrow without basis explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: reserve text interpreted as beneficiary-controlled escrow without basis explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('reserve text interpreted as beneficiary-controlled escrow without basis explicit caution üretsin')
    return cautions
