# Auto-generated integration for replenishment
# Rule: replenishment obligation open while security marked healthy explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: replenishment obligation open while security marked healthy explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('replenishment obligation open while security marked healthy explicit caution üretsin')
    return cautions
