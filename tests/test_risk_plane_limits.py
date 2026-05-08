from app.risk_plane.limits import RiskLimitRegistry
from app.risk_plane.models import RiskLimitDefinition
from app.risk_plane.enums import LimitClass, RiskDomain


def test_risk_limit_registry():
    registry = RiskLimitRegistry()
    limit = RiskLimitDefinition(
        limit_id="lim_1",
        limit_class=LimitClass.HARD,
        owner_domain="POLICY",
        domain=RiskDomain.ACCOUNT,
        target_id="MAIN",
        value=1000.0,
        description="Test limit",
    )
    registry.register_limit(limit)

    assert registry.get_limit("lim_1") is not None
    assert len(registry.get_limits_by_domain(RiskDomain.ACCOUNT, "MAIN")) == 1

    registry.clear()
    assert len(registry.all_limits()) == 0
