import pytest
from app.universe.tradability import TradabilityEvaluator
from app.universe.models import ProductInstrument, InstrumentRef, ExchangeFilterSet, InstrumentMetadata, TickSizeRule, StepSizeRule
from app.universe.enums import InstrumentType, InstrumentStatus, EligibilityVerdict, TradabilityClass, MetadataFreshness
from datetime import datetime, timezone

def test_evaluate_trading_no_liquidity():
    evaluator = TradabilityEvaluator()
    inst = ProductInstrument(
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

    report = evaluator.evaluate(inst)
    assert report.verdict == EligibilityVerdict.CAUTION
    assert "Missing liquidity data" in report.reasons
