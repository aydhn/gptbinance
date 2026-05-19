from typing import Dict, List, Optional
from app.federation_plane.models import EvidenceTranslationRecord
from app.federation_plane.exceptions import FederationPlaneError


class EvidenceTranslationManager:
    def __init__(self):
        self._translations: Dict[str, EvidenceTranslationRecord] = {}

    def register(self, record: EvidenceTranslationRecord):
        if not record.translation_id:
            raise FederationPlaneError("No translation==equivalence shortcut allowed.")
        self._translations[record.translation_id] = record

    def get_translation(
        self, translation_id: str
    ) -> Optional[EvidenceTranslationRecord]:
        return self._translations.get(translation_id)

    def list_translations(self) -> List[EvidenceTranslationRecord]:
        return list(self._translations.values())
