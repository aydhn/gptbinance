import os
from datetime import datetime
from app.research.regime.storage import RegimeStorage
from app.research.regime.models import (
    RegimeSnapshot,
    RegimeContext,
    RegimeSuitabilityMap,
)
from app.research.regime.enums import ContextQuality


def test_storage(tmp_path):
    storage = RegimeStorage(base_dir=str(tmp_path))
    ctx = RegimeContext(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        evaluations={},
        transitions={},
        suitability=RegimeSuitabilityMap(
            timestamp=datetime.now(),
            symbol="BTCUSDT",
            interval="15m",
            compatibilities={},
        ),
        overall_quality=ContextQuality.HIGH,
    )
    snap = RegimeSnapshot(
        timestamp=datetime.now(), symbol="BTCUSDT", interval="15m", context=ctx
    )

    storage.save_snapshot(snap)
    loaded = storage.load_recent_snapshots("BTCUSDT", "15m", 1)

    assert len(loaded) == 1
    assert loaded[0].symbol == "BTCUSDT"
