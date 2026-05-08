from typing import Dict, List
from datetime import datetime, timezone
from app.strategy_plane.models import StrategyLifecycleRecord
from app.strategy_plane.enums import LifecycleState
from app.strategy_plane.exceptions import InvalidLifecycleTransition


class StrategyLifecycleEvaluator:
    # Defines allowed transitions
    ALLOWED_TRANSITIONS = {
        LifecycleState.HYPOTHESIS_ONLY: [
            LifecycleState.RESEARCH_CANDIDATE,
            LifecycleState.RETIRED,
        ],
        LifecycleState.RESEARCH_CANDIDATE: [
            LifecycleState.REPLAY_QUALIFIED,
            LifecycleState.RETIRED,
        ],
        LifecycleState.REPLAY_QUALIFIED: [
            LifecycleState.PAPER_CANDIDATE,
            LifecycleState.RETIRED,
        ],
        LifecycleState.PAPER_CANDIDATE: [
            LifecycleState.PAPER_ACTIVE,
            LifecycleState.RETIRED,
        ],
        LifecycleState.PAPER_ACTIVE: [
            LifecycleState.PROBATIONARY_LIVE,
            LifecycleState.FROZEN,
            LifecycleState.RETIRED,
        ],
        LifecycleState.PROBATIONARY_LIVE: [
            LifecycleState.ACTIVE_LIMITED,
            LifecycleState.FROZEN,
            LifecycleState.RETIRED,
            LifecycleState.DEGRADED,
        ],
        LifecycleState.ACTIVE_LIMITED: [
            LifecycleState.ACTIVE_FULL,
            LifecycleState.FROZEN,
            LifecycleState.RETIRED,
            LifecycleState.DEGRADED,
        ],
        LifecycleState.ACTIVE_FULL: [
            LifecycleState.FROZEN,
            LifecycleState.RETIRED,
            LifecycleState.DEGRADED,
        ],
        LifecycleState.DEGRADED: [
            LifecycleState.FROZEN,
            LifecycleState.RETIRED,
            LifecycleState.PROBATIONARY_LIVE,
        ],  # Can go back to probation after fix
        LifecycleState.FROZEN: [
            LifecycleState.PAPER_ACTIVE,
            LifecycleState.RETIRED,
        ],  # Must prove in paper again
        LifecycleState.RETIRED: [LifecycleState.ARCHIVED],
        LifecycleState.ARCHIVED: [],
    }

    def __init__(self):
        self._history: Dict[str, List[StrategyLifecycleRecord]] = {}

    def transition(
        self,
        strategy_id: str,
        new_state: LifecycleState,
        reason: str,
        evidence_refs: List[str] = None,
    ) -> StrategyLifecycleRecord:
        current_state = self.get_current_state(strategy_id)

        if current_state and new_state not in self.ALLOWED_TRANSITIONS.get(
            current_state, []
        ):
            raise InvalidLifecycleTransition(
                f"Cannot transition from {current_state} to {new_state}"
            )

        record = StrategyLifecycleRecord(
            strategy_id=strategy_id,
            state=new_state,
            reason=reason,
            evidence_refs=evidence_refs or [],
        )

        if strategy_id not in self._history:
            self._history[strategy_id] = []
        self._history[strategy_id].append(record)
        return record

    def get_current_state(self, strategy_id: str) -> LifecycleState:
        history = self._history.get(strategy_id)
        if not history:
            return LifecycleState.HYPOTHESIS_ONLY
        return history[-1].state

    def get_history(self, strategy_id: str) -> List[StrategyLifecycleRecord]:
        return self._history.get(strategy_id, [])
