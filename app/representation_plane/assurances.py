# Auto-generated integration for representation
# Rule: customer-facing funded claim under non-segregated reserve explicit caution üretsin
def evaluate_performance_security_integration(context, security_records):
    cautions = []
    # Implementing: customer-facing funded claim under non-segregated reserve explicit caution üretsin
    if not security_records or getattr(security_records, 'is_unfunded', False):
        cautions.append('customer-facing funded claim under non-segregated reserve explicit caution üretsin')
    return cautions
