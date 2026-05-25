# Auto-generated integration for autonomy
# Rule: autonomous release treated as actual security release explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: autonomous release treated as actual security release explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('autonomous release treated as actual security release explicit caution üretsin')
    return cautions
