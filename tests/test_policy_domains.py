import pytest
from app.policy_kernel.enums import PolicyDomain
from app.policy_kernel.domains import get_domain_group, generate_domain_health_summary


def test_domain_groups():
    assert get_domain_group(PolicyDomain.RISK) == "risk_group"


def test_domain_health_summary():
    results = {
        PolicyDomain.RISK: {"verdict": "ALLOW", "findings": []},
        PolicyDomain.CAPITAL: {"verdict": "BLOCK", "findings": ["test"]},
    }
    summary = generate_domain_health_summary(results)
    assert summary["RISK"]["status"] == "HEALTHY"
    assert summary["CAPITAL"]["status"] == "UNHEALTHY"
