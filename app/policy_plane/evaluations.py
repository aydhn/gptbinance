# Auto-generated integration for policy
# Rule: phantom collateral or premature release context policy review/deny sonucu
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: phantom collateral or premature release context policy review/deny sonucu
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('phantom collateral or premature release context policy review/deny sonucu')
    return cautions
