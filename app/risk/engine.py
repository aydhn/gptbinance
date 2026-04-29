from typing import Dict, Any, List
from app.execution.live.models import ExecutionIntent


class RiskEngine:
    """Mock Risk Engine for execution handoff."""

    def approve_intent(
        self, raw_signal: Dict[str, Any], live_caps_config: Dict[str, Any] = None
    ) -> ExecutionIntent:
        # In reality, this checks limits, max position, etc.
        # Now it also optionally accepts live capital caps metadata for aware intent creation.
        pass
