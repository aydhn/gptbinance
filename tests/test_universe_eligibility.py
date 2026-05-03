import pytest
from app.universe.eligibility import ProfileEligibilityEvaluator
from app.universe.models import ProductInstrument, InstrumentRef, ExchangeFilterSet, InstrumentMetadata, TickSizeRule, StepSizeRule, UniverseProfileConfig
from app.universe.enums import InstrumentType, InstrumentStatus, MetadataFreshness, EligibilityVerdict, LiquiditySeverity, SpreadSeverity
from app.workspaces.enums import ProfileType
from datetime import datetime, timezone

@pytest.fixture
def base_instrument():
    return ProductInstrument(
        ref=InstrumentRef(symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT"),
        status=InstrumentStatus.TRADING,
        filters=ExchangeFilterSet(
            tick_size=TickSizeRule(tick_size=0.01, min_price=0.01, max_price=100000),
            step_size=StepSizeRule(step_size=0.001, min_qty=0.001, max_qty=100)
        ),
        metadata=InstrumentMetadata(base_asset="BTC", quote_asset="USDT"),
        freshness=MetadataFreshness.FRESH,
        last_update=datetime.now(timezone.utc),
        raw_data={}
    )

def test_profile_eligibility_eligible(base_instrument):
    evaluator = ProfileEligibilityEvaluator()
    config = UniverseProfileConfig(
        allowed_products=[InstrumentType.SPOT],
        min_liquidity=LiquiditySeverity.UNKNOWN, # Checked in Tradability
        max_spread=SpreadSeverity.UNKNOWN,
        require_fresh_metadata=True
    )

    res = evaluator.evaluate(base_instrument, config, ProfileType.PAPER_DEFAULT)
    assert res.verdict == EligibilityVerdict.ELIGIBLE

def test_profile_eligibility_wrong_product(base_instrument):
    evaluator = ProfileEligibilityEvaluator()
    config = UniverseProfileConfig(
        allowed_products=[InstrumentType.FUTURES], # Only futures
        min_liquidity=LiquiditySeverity.UNKNOWN,
        max_spread=SpreadSeverity.UNKNOWN,
        require_fresh_metadata=True
    )

    res = evaluator.evaluate(base_instrument, config, ProfileType.PAPER_DEFAULT)
    assert res.verdict == EligibilityVerdict.BLOCKED
    assert any("Product type InstrumentType.SPOT not allowed" in r for r in res.reasons)

def test_profile_eligibility_stale_metadata(base_instrument):
    base_instrument.freshness = MetadataFreshness.STALE
    evaluator = ProfileEligibilityEvaluator()
    config = UniverseProfileConfig(
        allowed_products=[InstrumentType.SPOT],
        min_liquidity=LiquiditySeverity.UNKNOWN,
        max_spread=SpreadSeverity.UNKNOWN,
        require_fresh_metadata=True
    )

    res = evaluator.evaluate(base_instrument, config, ProfileType.CANARY_LIVE_CAUTION)
    assert res.verdict == EligibilityVerdict.CAUTION
    assert "Metadata is stale" in res.reasons
