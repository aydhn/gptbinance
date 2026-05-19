from typing import Dict, List, Optional
from app.federation_plane.models import PartnerFederationRecord
from app.federation_plane.exceptions import FederationPlaneError


class PartnerManager:
    def __init__(self):
        self._partners: Dict[str, PartnerFederationRecord] = {}

    def register(self, record: PartnerFederationRecord):
        if not record.partner_id or not record.proof_notes:
            raise FederationPlaneError("No partner-black-box comfort allowed.")
        self._partners[record.partner_id] = record

    def get_partner(self, partner_id: str) -> Optional[PartnerFederationRecord]:
        return self._partners.get(partner_id)

    def list_partners(self) -> List[PartnerFederationRecord]:
        return list(self._partners.values())
