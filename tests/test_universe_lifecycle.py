import pytest
from app.universe.lifecycle import LifecycleManager
from app.universe.models import ProductInstrument, InstrumentRef, ExchangeFilterSet, InstrumentMetadata, TickSizeRule
from app.universe.enums import InstrumentType, InstrumentStatus, MetadataFreshness, LifecycleEventType
from datetime import datetime, timezone

def create_inst(status: InstrumentStatus, tick: float = 0.01) -> ProductInstrument:
    return ProductInstrument(
        ref=InstrumentRef(symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT"),
        status=status,
        filters=ExchangeFilterSet(tick_size=TickSizeRule(tick_size=tick, min_price=0.01, max_price=10000)),
        metadata=InstrumentMetadata(base_asset="BTC", quote_asset="USDT"),
        freshness=MetadataFreshness.FRESH,
        last_update=datetime.now(timezone.utc),
        raw_data={}
    )

def test_detect_changes_listed():
    manager = LifecycleManager()
    new_inst = create_inst(InstrumentStatus.TRADING)

    events = manager.detect_changes(None, new_inst)
    assert len(events) == 1
    assert events[0].event_type == LifecycleEventType.LISTED

def test_detect_changes_status_change():
    manager = LifecycleManager()
    old_inst = create_inst(InstrumentStatus.TRADING)
    new_inst = create_inst(InstrumentStatus.MAINTENANCE)

    events = manager.detect_changes(old_inst, new_inst)
    assert len(events) == 1
    assert events[0].event_type == LifecycleEventType.MAINTENANCE_STARTED
    assert events[0].old_status == InstrumentStatus.TRADING
    assert events[0].new_status == InstrumentStatus.MAINTENANCE

def test_detect_changes_filters_change():
    manager = LifecycleManager()
    old_inst = create_inst(InstrumentStatus.TRADING, tick=0.01)
    new_inst = create_inst(InstrumentStatus.TRADING, tick=0.001)

    events = manager.detect_changes(old_inst, new_inst)
    assert len(events) == 1
    assert events[0].event_type == LifecycleEventType.FILTERS_CHANGED
