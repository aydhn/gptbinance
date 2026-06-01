from typing import Dict, Any
from app.adaptation_plane.models import AdaptationTrustVerdict
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.enums import TrustVerdict, SideEffectClass
from app.adaptation_plane.exceptions import AdaptationPlaneError
import uuid

class TrustManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def generate_verdict(self, adaptation_id: str) -> AdaptationTrustVerdict:
        """Generate a trust verdict for an adaptation based on its integrity."""
        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise AdaptationPlaneError(f"Adaptation {adaptation_id} not found.")

        breakdown = {}
        status = TrustVerdict.TRUSTED

        # 1. Trigger Clarity
        if not adaptation.trigger:
            breakdown["trigger_clarity"] = "missing"
            status = TrustVerdict.DEGRADED
        else:
            breakdown["trigger_clarity"] = "present"

        # 2. Hypothesis Rigor
        if not adaptation.hypothesis:
            breakdown["hypothesis_rigor"] = "missing"
            status = TrustVerdict.DEGRADED
        else:
            breakdown["hypothesis_rigor"] = "present"

        # 3. Corrective Sufficiency
        if not adaptation.corrective_package:
            breakdown["corrective_sufficiency"] = "missing"
            status = TrustVerdict.DEGRADED
        else:
            breakdown["corrective_sufficiency"] = "present"

        # 4. Verification Maturity
        if not adaptation.verification:
            breakdown["verification_maturity"] = "missing"
            status = TrustVerdict.DEGRADED
        else:
            breakdown["verification_maturity"] = "present"

        # 5. Side-Effect Visibility
        if any(se.visibility == SideEffectClass.MATERIAL for se in adaptation.side_effects):
            breakdown["side_effect_visibility"] = "material_side_effects_detected"
            if status != TrustVerdict.DEGRADED:
                status = TrustVerdict.CAUTION
        else:
            breakdown["side_effect_visibility"] = "acceptable"

        # 6. Fitness Restoration
        if not adaptation.fitness and adaptation.status == "verified":
             breakdown["fitness_restoration"] = "missing_despite_verified_status"
             status = TrustVerdict.REVIEW_REQUIRED
        elif adaptation.fitness:
             breakdown["fitness_restoration"] = "present"

        # Patch Theater Detection
        if adaptation.status == "deployed" and not adaptation.verification and not adaptation.corrective_package:
            status = TrustVerdict.BLOCKED
            breakdown["patch_theater"] = "detected: deployed without package or verification"

        return AdaptationTrustVerdict(
            verdict_id=f"VERDICT-{uuid.uuid4().hex[:8].upper()}",
            adaptation_id=adaptation_id,
            status=status,
            breakdown=breakdown
        )

    def evaluate(self, *args, **kwargs):
        return "evaluated"
