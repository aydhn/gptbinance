import pytest
from app.universe.diff import DiffEngine
from app.universe.models import UniverseSnapshot, InstrumentRef
from app.workspaces.enums import ProfileType
from app.universe.enums import InstrumentType
from datetime import datetime, timezone


def create_ref(symbol):
    return InstrumentRef(
        symbol=symbol, product_type=InstrumentType.SPOT, canonical_symbol=symbol
    )


def test_compute_diff():
    engine = DiffEngine()

    ref1 = create_ref("BTCUSDT")
    ref2 = create_ref("ETHUSDT")
    ref3 = create_ref("SOLUSDT")

    old_snap = UniverseSnapshot(
        snapshot_id="snap1",
        profile=ProfileType.PAPER_DEFAULT,
        created_at=datetime.now(timezone.utc),
        eligible_instruments=[ref1, ref2],
        caution_instruments=[],
        blocked_instruments=[],
        manifest_ref="man1",
    )

    new_snap = UniverseSnapshot(
        snapshot_id="snap2",
        profile=ProfileType.PAPER_DEFAULT,
        created_at=datetime.now(timezone.utc),
        eligible_instruments=[ref1, ref3],  # removed ref2, added ref3
        caution_instruments=[],
        blocked_instruments=[],
        manifest_ref="man2",
    )

    diff = engine.compute_diff(old_snap, new_snap)

    assert diff.old_snapshot_id == "snap1"
    assert diff.new_snapshot_id == "snap2"

    assert len(diff.added) == 1
    assert diff.added[0].symbol == "SOLUSDT"

    assert len(diff.removed) == 1
    assert diff.removed[0].symbol == "ETHUSDT"

    assert len(diff.eligibility_changed) == 0


def test_compute_diff_eligibility_changed():
    engine = DiffEngine()
    ref1 = create_ref("BTCUSDT")

    old_snap = UniverseSnapshot(
        snapshot_id="snap1",
        profile=ProfileType.PAPER_DEFAULT,
        created_at=datetime.now(timezone.utc),
        eligible_instruments=[ref1],
        caution_instruments=[],
        blocked_instruments=[],
        manifest_ref="man1",
    )

    new_snap = UniverseSnapshot(
        snapshot_id="snap2",
        profile=ProfileType.PAPER_DEFAULT,
        created_at=datetime.now(timezone.utc),
        eligible_instruments=[],
        caution_instruments=[ref1],  # Changed from eligible to caution
        blocked_instruments=[],
        manifest_ref="man2",
    )

    diff = engine.compute_diff(old_snap, new_snap)

    assert len(diff.added) == 0
    assert len(diff.removed) == 0
    assert len(diff.eligibility_changed) == 1
    assert diff.eligibility_changed[0].symbol == "BTCUSDT"
