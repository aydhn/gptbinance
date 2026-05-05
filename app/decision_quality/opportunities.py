from typing import Dict, Any, Optional
from datetime import datetime, timezone
import uuid
from .models import OpportunityCandidate


class OpportunityCapture:
    """
    Captures raw strategy signals as Opportunity Candidates before any execution logic.
    """

    def capture_candidate(
        self,
        symbol: str,
        regime: str,
        strategy_family: str,
        timeframe: str,
        profile: str,
        signal_strength: float,
        market_truth_posture: str,
        event_risk_context: str,
        universe_eligibility_context: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> OpportunityCandidate:
        """
        Creates an OpportunityCandidate from strategy signal outputs.
        """
        candidate_id = str(uuid.uuid4())
        timestamp = datetime.now(
            timezone.utc
        )  # Intentionally generic, in a real app would use timezone aware

        return OpportunityCandidate(
            id=candidate_id,
            symbol=symbol,
            timestamp=timestamp,
            timeframe=timeframe,
            regime=regime,
            strategy_family=strategy_family,
            profile=profile,
            signal_strength=signal_strength,
            market_truth_posture=market_truth_posture,
            event_risk_context=event_risk_context,
            universe_eligibility_context=universe_eligibility_context,
            metadata=metadata or {},
        )
