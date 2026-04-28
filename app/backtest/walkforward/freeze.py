import json
import logging
from app.backtest.walkforward.models import FrozenStrategyBundle
from app.backtest.walkforward.exceptions import FrozenBundleError
from app.strategies.models import StrategySpec

logger = logging.getLogger(__name__)


class FreezeManager:
    def __init__(self):
        pass

    def freeze(self, bundle: FrozenStrategyBundle) -> str:
        """Returns a deterministic representation (e.g. hash or serialized string) of the frozen bundle."""
        # Simple serialization for demonstration
        try:
            # StrategySpec has dict parameters, might need sorting for stable serialization
            # Pydantic v2 .model_dump_json() is useful
            data = bundle.spec.model_dump_json()
            return data
        except Exception as e:
            raise FrozenBundleError(f"Failed to serialize frozen bundle: {e}")

    def verify(self, bundle: FrozenStrategyBundle, frozen_snapshot: str) -> bool:
        """Verifies that the bundle hasn't changed relative to the snapshot."""
        try:
            current_data = bundle.spec.model_dump_json()
            return current_data == frozen_snapshot
        except Exception as e:
            raise FrozenBundleError(f"Failed to verify frozen bundle: {e}")
