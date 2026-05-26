# estate.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import EstateRecord, EstateScopeRecord, EstateAssetRecord
from app.insolvency_plane.enums import EstateClass
from app.insolvency_plane.exceptions import InvalidEstateError

class EstateManager:
    def __init__(self):
        self.estates: Dict[str, EstateRecord] = {}

    def form_estate(self, estate: EstateRecord):
        if estate.estate_class == EstateClass.LEAK_RISK:
            # Maybe log or warn, but allow it so it can be surfaced
            pass
        self.estates[estate.estate_id] = estate

    def get_estate(self, estate_id: str) -> Optional[EstateRecord]:
        return self.estates.get(estate_id)

    def list_estates(self) -> List[EstateRecord]:
        return list(self.estates.values())
