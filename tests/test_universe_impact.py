import pytest
from app.universe.impact import ImpactAnalyzer
from app.universe.models import UniverseDiff, InstrumentRef
from app.universe.enums import InstrumentType
from datetime import datetime, timezone


def test_analyze_impact_low():
    analyzer = ImpactAnalyzer()
    diff = UniverseDiff(
        diff_id="diff1",
        old_snapshot_id="snap1",
        new_snapshot_id="snap2",
        added=[
            InstrumentRef(
                symbol="BTCUSDT",
                product_type=InstrumentType.SPOT,
                canonical_symbol="BTCUSDT",
            )
        ],
        removed=[],
        status_changed=[],
        eligibility_changed=[],
        created_at=datetime.now(timezone.utc),
    )

    report = analyzer.analyze(diff)
    assert report.severity == "low"


def test_analyze_impact_medium():
    analyzer = ImpactAnalyzer()
    diff = UniverseDiff(
        diff_id="diff1",
        old_snapshot_id="snap1",
        new_snapshot_id="snap2",
        added=[],
        removed=[
            InstrumentRef(
                symbol="BTCUSDT",
                product_type=InstrumentType.SPOT,
                canonical_symbol="BTCUSDT",
            )
        ],
        status_changed=[],
        eligibility_changed=[],
        created_at=datetime.now(timezone.utc),
    )

    report = analyzer.analyze(diff)
    assert report.severity == "medium"
    assert "all_active_strategies" in report.impacted_strategies
