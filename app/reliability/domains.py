class AssuranceIntegrityReliabilityDomain:
    @staticmethod
    def calculate_reliability(assurance_record) -> int:
        return 100 if assurance_record.cases and not (assurance_record.expiry and assurance_record.expiry.is_expired) else 50

ACCOUNTABILITY_RELIABILITY_DOMAINS = ['accountability_integrity']


# Incentive Plane Reliability Domain
class IncentiveReliabilityDomain:
    name = "incentive_integrity"
    inputs = [
        "reward_hacking",
        "concealment_incentive",
        "symbolic_penalties",
        "hidden_conflicts"
    ]
