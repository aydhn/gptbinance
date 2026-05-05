from app.experiments.baselines import BaselineRegistry
from app.experiments.models import BaselineReference
from datetime import datetime, timezone


def test_baseline_registry():
    reg = BaselineRegistry()
    b = BaselineReference(
        baseline_id="b_1",
        strategy_id="s_1",
        profile_id="p_1",
        frozen_at=datetime.now(timezone.utc),
        manifest_hash="abc",
    )
    reg.register(b)

    assert reg.get("b_1").strategy_id == "s_1"
    assert reg.check_freshness("b_1") is True
