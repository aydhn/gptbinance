from typing import Optional
from typing import Dict, List
from datetime import datetime, timezone
from app.capital.models import CapitalTranche, CapitalTrancheActivation
from app.capital.exceptions import InvalidTrancheDefinitionError


class TrancheManager:
    def __init__(self):
        self._tranches: Dict[str, CapitalTranche] = {}
        self._activations: Dict[str, CapitalTrancheActivation] = {}

    def register_tranche(self, tranche: CapitalTranche):
        if tranche.size_amount < 0:
            raise InvalidTrancheDefinitionError("Tranche size must be non-negative.")
        self._tranches[tranche.tranche_id] = tranche

    def activate_tranche(self, tranche_id: str) -> CapitalTrancheActivation:
        if tranche_id not in self._tranches:
            raise InvalidTrancheDefinitionError(f"Unknown tranche {tranche_id}")

        activation = CapitalTrancheActivation(
            tranche_id=tranche_id, activated_at=datetime.now(timezone.utc), active=True
        )
        # Store latest activation state
        self._activations[tranche_id] = activation
        return activation

    def deactivate_tranche(self, tranche_id: str) -> Optional[CapitalTrancheActivation]:
        if tranche_id in self._activations and self._activations[tranche_id].active:
            activation = self._activations[tranche_id]
            activation.active = False
            activation.deactivated_at = datetime.now(timezone.utc)
            return activation
        return None

    def get_active_tranches(self) -> List[CapitalTrancheActivation]:
        return [act for act in self._activations.values() if act.active]

    def get_total_active_tranche_size(self) -> float:
        total = 0.0
        for act in self.get_active_tranches():
            if act.tranche_id in self._tranches:
                total += self._tranches[act.tranche_id].size_amount
        return total


# Global instance for simplicity in this phase
tranche_manager = TrancheManager()
