def check_assurance_invariants(assurance_record) -> list:
    violations = []
    if not assurance_record.cases and assurance_record.certifications:
        violations.append("no posture may be treated as assured without explicit claim integrity and evidence sufficiency")
    if assurance_record.expiry and assurance_record.expiry.is_expired and assurance_record.surveillance:
        violations.append("no contractual or rights-safe claim may stand while the governing assurance remains stale")
    return violations

ACCOUNTABILITY_INVARIANTS = [
    'No trusted high-risk closure may be emitted while material accountability remains unresolved.',
    'No accountability posture may be treated as remediated without explicit subject clarity and restitution analysis.'
]
