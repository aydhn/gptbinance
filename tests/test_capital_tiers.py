from app.capital.tiers import get_tier, get_all_tiers
from app.capital.exceptions import InvalidCapitalTierError
import pytest


def test_tier_registry():
    tiers = get_all_tiers()
    assert len(tiers) > 0

    tier = get_tier("canary_micro")
    assert tier.id == "canary_micro"
    assert tier.budget.max_deployable_capital == 50.0

    with pytest.raises(InvalidCapitalTierError):
        get_tier("non_existent_tier")
