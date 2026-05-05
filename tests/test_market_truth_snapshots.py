from app.market_truth.snapshots import SnapshotCapture
from app.market_truth.sources import BinanceOfficialRestAdapter


def test_snapshot_capture():
    cap = SnapshotCapture()
    adp = BinanceOfficialRestAdapter()
    res = cap.capture(adp)
    assert res["source"] == "official_rest"
