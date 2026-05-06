from typing import List, Dict, Optional
from uuid import UUID
from app.identity.enums import TrustZone, CapabilityClass
from app.identity.models import TrustZoneBinding
from app.identity.storage import identity_storage


class TrustZoneRegistry:
    # Defines which capabilities are generally safe/expected in which zones.
    # This is an extra layer of defense (policy).
    ZONE_CAPABILITY_MAP: Dict[TrustZone, List[CapabilityClass]] = {
        TrustZone.PUBLIC_READONLY: [],
        TrustZone.OPERATIONAL_READONLY: [
            CapabilityClass.ACCESS_RESTRICTED_EVIDENCE_SUMMARY,
            CapabilityClass.ACCESS_RUNTIME_POSTURE,
        ],
        TrustZone.REVIEW_RESTRICTED: [
            CapabilityClass.READ_EVIDENCE_PACK,
            CapabilityClass.BUILD_CASE_FILE,
            CapabilityClass.REQUEST_REVIEW,
            CapabilityClass.ADJUDICATE_REVIEW,
        ],
        TrustZone.RELEASE_CONTROLLED: [
            CapabilityClass.REQUEST_ACTIVATION_TRANSITION,
            CapabilityClass.REQUEST_RELEASE_HOLD_REVIEW,
        ],
        TrustZone.INCIDENT_SENSITIVE: [
            CapabilityClass.REVIEW_INCIDENT_CONTAINMENT,
            CapabilityClass.FINALIZE_POSTMORTEM,
            CapabilityClass.REVIEW_CAPA_EFFECTIVENESS,
        ],
        TrustZone.SECRET_ADJACENT: [
            # Secret access isn't explicitly a capability here yet,
            # but this zone allows interacting with systems that have secrets
        ],
        TrustZone.BREAKGLASS_EMERGENCY: [CapabilityClass.REVIEW_BREAKGLASS],
        TrustZone.RUNTIME_SENSITIVE: [
            CapabilityClass.REQUEST_MIGRATION_APPLY,
            CapabilityClass.REVIEW_NON_REVERSIBLE_MIGRATION,
        ],
    }

    def bind_zone(self, principal_id: UUID, zone: TrustZone) -> None:
        binding = TrustZoneBinding(principal_id=principal_id, zone=zone)
        identity_storage.save_trust_zone_binding(binding)

    def is_in_zone(self, principal_id: UUID, zone: TrustZone) -> bool:
        bindings = identity_storage.get_trust_zones(principal_id)
        return any(b.zone == zone for b in bindings)

    def list_all_zones(self) -> List[TrustZone]:
        return list(TrustZone)


zone_registry = TrustZoneRegistry()
