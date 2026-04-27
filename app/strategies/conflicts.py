from typing import List, Optional
from datetime import datetime

from app.strategies.models import EntryIntentCandidate, SignalConflict, SignalResolution
from app.strategies.enums import ConflictType, ResolutionType


class ConflictResolver:
    """
    Resolves conflicts when multiple intents are generated for the same symbol at the same time.
    """

    def resolve(
        self, intents: List[EntryIntentCandidate], symbol: str, timestamp: datetime
    ) -> SignalResolution:
        if not intents:
            return SignalResolution(
                symbol=symbol,
                timestamp=timestamp,
                resolution_type=ResolutionType.NO_CLEAR_INTENT,
                reason="No intents to resolve.",
            )

        if len(intents) == 1:
            return SignalResolution(
                symbol=symbol,
                timestamp=timestamp,
                resolution_type=ResolutionType.HIGHEST_SCORE,
                resolved_intent=intents[0],
                reason="Only one intent, auto-resolved.",
            )

        # Check if directions conflict
        directions = set(intent.direction for intent in intents)

        if len(directions) > 1:
            # Opposing directions
            # Simple policy: higher score wins, or no clear intent if scores are close
            sorted_intents = sorted(intents, key=lambda x: x.score, reverse=True)
            top_intent = sorted_intents[0]
            runner_up = sorted_intents[1]

            # If the difference is marginal, reject both
            if (top_intent.score - runner_up.score) < 10.0:
                return SignalResolution(
                    symbol=symbol,
                    timestamp=timestamp,
                    resolution_type=ResolutionType.NO_CLEAR_INTENT,
                    reason=f"Opposing intents with close scores: {top_intent.score:.2f} vs {runner_up.score:.2f}",
                )

            return SignalResolution(
                symbol=symbol,
                timestamp=timestamp,
                resolution_type=ResolutionType.HIGHEST_SCORE,
                resolved_intent=top_intent,
                reason=f"Opposing intents. Resolved by highest score: {top_intent.score:.2f} vs {runner_up.score:.2f}",
            )

        else:
            # Multiple intents in the same direction
            sorted_intents = sorted(intents, key=lambda x: x.score, reverse=True)
            top_intent = sorted_intents[0]

            return SignalResolution(
                symbol=symbol,
                timestamp=timestamp,
                resolution_type=ResolutionType.HIGHEST_SCORE,
                resolved_intent=top_intent,
                reason="Multiple intents in same direction. Picked highest score.",
            )

    def detect_conflicts(
        self, intents: List[EntryIntentCandidate], symbol: str, timestamp: datetime
    ) -> Optional[SignalConflict]:
        if len(intents) <= 1:
            return None

        directions = set(intent.direction for intent in intents)
        conflict_type = (
            ConflictType.OPPOSING_DIRECTION
            if len(directions) > 1
            else ConflictType.MULTIPLE_SAME_DIRECTION
        )

        return SignalConflict(
            symbol=symbol,
            timestamp=timestamp,
            conflict_type=conflict_type,
            intents=intents,
        )
