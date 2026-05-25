# Auto-generated integration for liability
# Rule: cap comfort used despite under-secured retained exposure explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: cap comfort used despite under-secured retained exposure explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('cap comfort used despite under-secured retained exposure explicit caution üretsin')
    return cautions
