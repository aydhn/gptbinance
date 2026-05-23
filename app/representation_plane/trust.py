from app.representation_plane.models import RepresentationObject, TrustVerdict
from app.representation_plane.enums import TrustVerdictEnum, MaterialityClass

class TrustedRepresentationVerdictEngine:
    @staticmethod
    def evaluate(rep: RepresentationObject, caveats: list, disclaimers: list, corrections: list) -> TrustVerdict:
        verdict = TrustVerdictEnum.TRUSTED
        blockers = []
        warnings = []
        factors = {
            "audience_clarity": "high",
            "materiality_rigor": "high",
            "caveat_discipline": "high"
        }

        # Check for material omissions
        if rep.materiality == MaterialityClass.OMITTED_MATERIAL:
            verdict = TrustVerdictEnum.BLOCKED
            blockers.append("Material omission detected. Representation is untrustworthy.")
            factors["materiality_rigor"] = "failed"

        # Check for caveat burial
        for cav in caveats:
            if cav.is_material and cav.is_buried:
                if verdict != TrustVerdictEnum.BLOCKED:
                    verdict = TrustVerdictEnum.CAUTION
                warnings.append("Material caveat is buried, reducing reliance safety.")
                factors["caveat_discipline"] = "degraded"

        # Check for disclaimer laundering
        for disc in disclaimers:
            if disc.is_laundering_attempt:
                verdict = TrustVerdictEnum.BLOCKED
                blockers.append("Disclaimer laundering detected. Cannot use disclaimer to cure material misrepresentation.")

        # Check for unpropagated corrections
        unpropagated = [c for c in corrections if not c.propagated_downstream]
        if unpropagated:
            if verdict == TrustVerdictEnum.TRUSTED:
                verdict = TrustVerdictEnum.DEGRADED
            warnings.append("Corrections exist but have not propagated downstream.")

        return TrustVerdict(
            representation_id=rep.representation_id,
            verdict=verdict,
            factors=factors,
            blockers=blockers,
            warnings=warnings
        )
