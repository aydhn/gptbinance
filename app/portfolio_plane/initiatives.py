from typing import Dict, Optional
from app.portfolio_plane.models import InitiativeRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class InitiativeManager:
    def __init__(self):
        self._initiatives: Dict[str, InitiativeRecord] = {}

    def register(self, initiative: InitiativeRecord):
        if initiative.initiative_id in self._initiatives:
            raise PortfolioStorageError(f"Initiative {initiative.initiative_id} already exists")
        self._initiatives[initiative.initiative_id] = initiative

    def get(self, initiative_id: str) -> Optional[InitiativeRecord]:
        return self._initiatives.get(initiative_id)

    def get_all(self) -> Dict[str, InitiativeRecord]:
        return self._initiatives.copy()
