def evaluate_assurance_policy(assurance_record) -> str:
    if not assurance_record.cases:
        return "DENY: Insufficient evidence context"
    if assurance_record.expiry and assurance_record.expiry.is_expired:
        return "DENY: Stale certification"
    return "ALLOW"
