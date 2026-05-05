from typing import Dict, List
from app.policy_kernel.models import PolicyRule, PolicyRuleVersion
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from datetime import datetime, timezone

_REGISTRY: Dict[str, PolicyRule] = {}


def register_rule(rule: PolicyRule):
    _REGISTRY[rule.rule_id] = rule


def get_rule(rule_id: str) -> PolicyRule:
    return _REGISTRY.get(rule_id)


def list_rules() -> List[PolicyRule]:
    return list(_REGISTRY.values())


# Sample Rules
register_rule(
    PolicyRule(
        rule_id="RULE_STALE_EVENT_CALENDAR_PAPER",
        owner="event_risk_team",
        rationale="Stale event calendar under paper mode warrants caution.",
        domain=PolicyDomain.EVENT_RISK,
        severity=PolicyVerdict.CAUTION,
        required_evidence=["event_refs"],
        is_waivable=True,
        effective_scope=["paper"],
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
)

register_rule(
    PolicyRule(
        rule_id="RULE_LOW_CONF_STRESS_TESTNET",
        owner="stress_risk_team",
        rationale="Low confidence stress evidence under testnet mode blocks execution.",
        domain=PolicyDomain.STRESS_RISK,
        severity=PolicyVerdict.BLOCK,
        required_evidence=["stress_refs"],
        is_waivable=True,
        effective_scope=["testnet"],
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
)

register_rule(
    PolicyRule(
        rule_id="RULE_CAPITAL_SCALE_UP_FRESH_QUAL",
        owner="capital_team",
        rationale="Capital scale-up requires fresh qualification evidence.",
        domain=PolicyDomain.CAPITAL,
        severity=PolicyVerdict.BLOCK,
        required_evidence=["qualification_refs", "capital_refs"],
        is_waivable=True,
        effective_scope=["live"],
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
)
