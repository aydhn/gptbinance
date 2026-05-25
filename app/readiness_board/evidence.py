# Auto-generated integration for readiness
# Rule: critical performance security integrity failures blocker/caution olsun
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: critical performance security integrity failures blocker/caution olsun
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('critical performance security integrity failures blocker/caution olsun')
    return cautions
