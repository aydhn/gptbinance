from app.waterfall_plane.models import DistributionRuleRecord

def register_distribution_rule(rule_id: str, description: str) -> DistributionRuleRecord:
    return DistributionRuleRecord(rule_id=rule_id, description=description)
