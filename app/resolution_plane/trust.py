from app.resolution_plane.base import TrustEvaluatorBase
from app.resolution_plane.models import ResolutionTrustVerdict, ResolutionObject
from app.resolution_plane.enums import TrustVerdict, TransferClass, ContinuityClass

class TrustedResolutionVerdictEngine(TrustEvaluatorBase):
    def __init__(self, registry):
        self.registry = registry

    def evaluate_trust(self, resolution_id: str) -> ResolutionTrustVerdict:
        resolution = self.registry.get_resolution(resolution_id)
        if not resolution:
            return ResolutionTrustVerdict(
                id=resolution_id,
                verdict=TrustVerdict.BLOCKED,
                factors={"existence": "Not found in registry"},
                caveats=["Resolution ID is invalid or not registered"]
            )

        factors = {}
        caveats = []
        verdict = TrustVerdict.TRUSTED

        # Evaluate Transfer Posture
        factors["transfer_posture"] = resolution.transfer_posture.value
        if resolution.transfer_posture == TransferClass.CONTAMINATED_PERIMETER:
            verdict = TrustVerdict.DEGRADED
            caveats.append("Transfer perimeter is contaminated")
        elif resolution.transfer_posture == TransferClass.PARTIAL_TRANSFER:
            verdict = TrustVerdict.CAUTION
            caveats.append("Partial transfer detected")

        # Evaluate Continuity Posture
        factors["continuity_posture"] = resolution.continuity_posture.value
        if resolution.continuity_posture == ContinuityClass.BROKEN_CONTINUITY:
            verdict = TrustVerdict.BLOCKED
            caveats.append("Broken continuity detected")
        elif resolution.continuity_posture == ContinuityClass.PROVISIONAL_CONTINUITY:
            if verdict != TrustVerdict.BLOCKED:
                verdict = TrustVerdict.CAUTION
            caveats.append("Continuity is provisional")

        return ResolutionTrustVerdict(
            id=resolution_id,
            verdict=verdict,
            factors=factors,
            caveats=caveats
        )
