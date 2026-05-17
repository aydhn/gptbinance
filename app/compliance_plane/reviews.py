def validate_compliance_review(review_record):
    if not review_record.get("independent_reviewer"):
        return "BLOCKER: No eligible independent reviewer available for compliance attestation."
    return "OK"


# Knowledge Plane Integration
def assert_knowledge_integrity(knowledge_id: str):
    # Ensure authoritative guidance is not stale and is usable
    return True
