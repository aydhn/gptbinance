from typing import Dict, Optional, List
from app.supply_chain_plane.models import SourceOriginRecord, ComponentRef
from app.supply_chain_plane.enums import OriginClass


class SourceOriginRegistry:
    def __init__(self):
        self._origins: Dict[str, SourceOriginRecord] = {}

    def register_origin(self, origin: SourceOriginRecord) -> None:
        self._origins[origin.origin_id] = origin

    def get_origin(self, origin_id: str) -> Optional[SourceOriginRecord]:
        return self._origins.get(origin_id)

    def list_origins_for_component(self, component_id: str) -> List[SourceOriginRecord]:
        return [
            o
            for o in self._origins.values()
            if o.component_ref.component_id == component_id
        ]


class OriginTrustManager:
    def evaluate_origin_trust(self, origin: SourceOriginRecord) -> Dict[str, any]:
        # Evaluates the trust of an origin based on its class
        trust_hints = origin.trust_hints

        if origin.origin_class == OriginClass.INTERNAL_SOURCE:
            return {"trusted": True, "reason": "Internal source"}
        elif origin.origin_class == OriginClass.THIRD_PARTY_PACKAGE:
            if trust_hints.get("approved_vendor", False):
                return {"trusted": True, "reason": "Approved third-party vendor"}
            return {
                "trusted": False,
                "reason": "Unreviewed third-party origin",
                "requires_review": True,
            }

        return {"trusted": False, "reason": "Unknown or unhandled origin class"}
