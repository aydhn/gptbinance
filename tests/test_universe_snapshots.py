import pytest
from app.universe.snapshots import SnapshotBuilder
from app.universe.models import UniverseEligibilityResult, InstrumentRef
from app.universe.enums import InstrumentType, EligibilityVerdict
from app.workspaces.enums import ProfileType
from datetime import datetime, timezone


def test_build_snapshot():
    builder = SnapshotBuilder()

    evals = [
        UniverseEligibilityResult(
            ref=InstrumentRef(
                symbol="BTCUSDT",
                product_type=InstrumentType.SPOT,
                canonical_symbol="BTCUSDT",
            ),
            profile=ProfileType.PAPER_DEFAULT,
            verdict=EligibilityVerdict.ELIGIBLE,
            reasons=[],
            evaluation_time=datetime.now(timezone.utc),
        ),
        UniverseEligibilityResult(
            ref=InstrumentRef(
                symbol="SHIBUSDT",
                product_type=InstrumentType.SPOT,
                canonical_symbol="SHIBUSDT",
            ),
            profile=ProfileType.PAPER_DEFAULT,
            verdict=EligibilityVerdict.BLOCKED,
            reasons=["Denylist"],
            evaluation_time=datetime.now(timezone.utc),
        ),
        UniverseEligibilityResult(
            ref=InstrumentRef(
                symbol="ETHUSDT",
                product_type=InstrumentType.SPOT,
                canonical_symbol="ETHUSDT",
            ),
            profile=ProfileType.PAPER_DEFAULT,
            verdict=EligibilityVerdict.CAUTION,
            reasons=["Stale data"],
            evaluation_time=datetime.now(timezone.utc),
        ),
    ]

    snapshot = builder.build(ProfileType.PAPER_DEFAULT, evals)

    assert snapshot.profile == ProfileType.PAPER_DEFAULT
    assert len(snapshot.eligible_instruments) == 1
    assert snapshot.eligible_instruments[0].symbol == "BTCUSDT"
    assert len(snapshot.caution_instruments) == 1
    assert snapshot.caution_instruments[0].symbol == "ETHUSDT"
    assert len(snapshot.blocked_instruments) == 1
    assert snapshot.blocked_instruments[0].symbol == "SHIBUSDT"
