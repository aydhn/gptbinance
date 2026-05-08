# Strategy Engine Integration with Allocation Plane Canonical Intake Format
from typing import List, Dict, Any
from app.allocation.models import AllocationCandidate
from app.allocation.enums import AllocationClass, SignalFamily

class StrategyEngine:
    def produce_candidates(self) -> List[AllocationCandidate]:
        # Emits signals in the format required by the allocation plane
        return [
            AllocationCandidate(
                candidate_id="cand_1",
                symbol="BTCUSDT",
                signal_source_ref="strat_momentum_btc",
                signal_family=SignalFamily.MOMENTUM,
                sleeve_ref="primary_alpha_01",
                confidence=0.85,
                requested_notional=10000.0,
                allocation_class=AllocationClass.DIRECTIONAL_LONG,
                regime_refs=["regime_bull"]
            )
        ]
