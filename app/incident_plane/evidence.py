# Auto-generated integration for incident
# Rule: incident evidence line without performance security posture explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: incident evidence line without performance security posture explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('incident evidence line without performance security posture explicit caution üretsin')
    return cautions
