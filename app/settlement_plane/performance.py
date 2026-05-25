# Auto-generated integration for settlement
# Rule: structured settlement performance marked safe without security posture explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: structured settlement performance marked safe without security posture explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('structured settlement performance marked safe without security posture explicit caution üretsin')
    return cautions
