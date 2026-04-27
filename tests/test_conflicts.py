from datetime import datetime
from app.strategies.conflicts import ConflictResolver
from app.strategies.models import EntryIntentCandidate
from app.strategies.enums import SignalDirection, ResolutionType, ConflictType


def test_conflict_resolver():
    resolver = ConflictResolver()
    now = datetime.utcnow()

    i1 = EntryIntentCandidate(
        strategy_name="s1",
        symbol="BTC",
        timestamp=now,
        direction=SignalDirection.LONG,
        score=80.0,
        confidence=0.9,
    )
    i2 = EntryIntentCandidate(
        strategy_name="s2",
        symbol="BTC",
        timestamp=now,
        direction=SignalDirection.SHORT,
        score=95.0,
        confidence=0.9,
    )

    conflict = resolver.detect_conflicts([i1, i2], "BTC", now)
    assert conflict is not None
    assert conflict.conflict_type == ConflictType.OPPOSING_DIRECTION

    resolution = resolver.resolve([i1, i2], "BTC", now)
    assert resolution.resolution_type == ResolutionType.HIGHEST_SCORE
    assert resolution.resolved_intent == i2

    # Close scores
    i3 = EntryIntentCandidate(
        strategy_name="s3",
        symbol="BTC",
        timestamp=now,
        direction=SignalDirection.SHORT,
        score=85.0,
        confidence=0.9,
    )
    resolution = resolver.resolve([i1, i3], "BTC", now)
    assert resolution.resolution_type == ResolutionType.NO_CLEAR_INTENT
