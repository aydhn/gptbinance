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


# Incentive Plane Invariants
INCENTIVE_INVARIANTS = [
    "no trusted high-risk closure, settlement, discharge, final-safe or behavior-aligned claim may be emitted while material incentive treatment remains unresolved in eligible scopes",
    "no subject, target, reward, penalty, friction, clawback, escalation or recalibration event may alter an incentive posture beyond its explicit domain, beneficiary, authority, scope and jurisdiction boundaries",
    "no posture may be treated as aligned, deterrent, risk-adjusted or beneficiary-safe without explicit target integrity, formula rigor, gaming/conflict visibility, friction sufficiency and externality analysis",
    "no contractual, rights-safe, liability-safe, remedy-safe, final-safe or compliance-safe claim may stand while the governing incentive remains materially gameable, conflict-bearing, beneficiary-costly, symbolic or clawback-deficient"
]
