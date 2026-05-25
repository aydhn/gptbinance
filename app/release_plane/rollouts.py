# Auto-generated integration for release_rollout
# Rule: rollout losses treated secured under cosmetic reserve explicit anomaly üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: rollout losses treated secured under cosmetic reserve explicit anomaly üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('rollout losses treated secured under cosmetic reserve explicit anomaly üretsin')
    return cautions
