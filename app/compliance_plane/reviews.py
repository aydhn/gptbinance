def validate_compliance_review(review_record):
    if not review_record.get("independent_reviewer"):
        return "BLOCKER: No eligible independent reviewer available for compliance attestation."
    return "OK"
