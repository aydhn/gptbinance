import pytest
from datetime import datetime, timezone
from app.universe.registry import InstrumentRegistry
from app.universe.models import ProductInstrument, InstrumentRef, ExchangeFilterSet, InstrumentMetadata
from app.universe.enums import InstrumentType, InstrumentStatus, MetadataFreshness

def test_registry_upsert_and_get():
    registry = InstrumentRegistry()

    inst = ProductInstrument(
        ref=InstrumentRef(symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT"),
        status=InstrumentStatus.TRADING,
        filters=ExchangeFilterSet(),
        metadata=InstrumentMetadata(base_asset="BTC", quote_asset="USDT"),
        freshness=MetadataFreshness.FRESH,
        last_update=datetime.now(timezone.utc),
        raw_data={}
    )

    registry.upsert_instrument(inst)

    retrieved = registry.get_instrument("BTCUSDT", InstrumentType.SPOT)
    assert retrieved is not None
    assert retrieved.ref.symbol == "BTCUSDT"

    # Should be None for futures
    assert registry.get_instrument("BTCUSDT", InstrumentType.FUTURES) is None

def test_get_all_active():
    registry = InstrumentRegistry()

    inst1 = ProductInstrument(
        ref=InstrumentRef(symbol="BTCUSDT", product_type=InstrumentType.SPOT, canonical_symbol="BTCUSDT"),
        status=InstrumentStatus.TRADING,
        filters=ExchangeFilterSet(),
        metadata=InstrumentMetadata(base_asset="BTC", quote_asset="USDT"),
        freshness=MetadataFreshness.FRESH,
        last_update=datetime.now(timezone.utc),
        raw_data={}
    )

    inst2 = ProductInstrument(
        ref=InstrumentRef(symbol="ETHUSDT", product_type=InstrumentType.SPOT, canonical_symbol="ETHUSDT"),
        status=InstrumentStatus.DELISTED,
        filters=ExchangeFilterSet(),
        metadata=InstrumentMetadata(base_asset="ETH", quote_asset="USDT"),
        freshness=MetadataFreshness.FRESH,
        last_update=datetime.now(timezone.utc),
        raw_data={}
    )

    registry.upsert_instrument(inst1)
    registry.upsert_instrument(inst2)

    active = registry.get_all_active()
    assert len(active) == 1
    assert active[0].ref.symbol == "BTCUSDT"
