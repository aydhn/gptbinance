import pytest
import os
import tempfile
from pathlib import Path
from app.universe.storage import UniverseStorage
from app.universe.models import (
    ProductInstrument,
    InstrumentRef,
    ExchangeFilterSet,
    InstrumentMetadata,
)
from app.universe.enums import InstrumentType, InstrumentStatus, MetadataFreshness
from datetime import datetime, timezone
import app.universe.storage


def test_storage_save_load():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Save original base_dir
        storage = UniverseStorage()
        orig_base_dir = storage.base_dir

        try:
            # Set base_dir to tmpdir for test
            storage.base_dir = Path(tmpdir)

            inst = ProductInstrument(
                ref=InstrumentRef(
                    symbol="BTCUSDT",
                    product_type=InstrumentType.SPOT,
                    canonical_symbol="BTCUSDT",
                ),
                status=InstrumentStatus.TRADING,
                filters=ExchangeFilterSet(),
                metadata=InstrumentMetadata(base_asset="BTC", quote_asset="USDT"),
                freshness=MetadataFreshness.FRESH,
                last_update=datetime.now(timezone.utc),
                raw_data={},
            )

            storage.save_registry_snapshot([inst], "test_snap")

            loaded = storage.load_registry_snapshot("test_snap")
            assert len(loaded) == 1
            assert loaded[0].ref.symbol == "BTCUSDT"
            assert loaded[0].status == InstrumentStatus.TRADING
        finally:
            storage.base_dir = orig_base_dir
