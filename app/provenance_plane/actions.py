# Auto-generated integration for provenance
# Rule: security action without accountable funder/controller/approver explicit anomaly üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: security action without accountable funder/controller/approver explicit anomaly üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('security action without accountable funder/controller/approver explicit anomaly üretsin')
    return cautions
