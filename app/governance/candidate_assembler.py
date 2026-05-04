from app.crossbook.overlay import CrossBookOverlay
from app.crossbook.enums import CrossBookVerdict

from app.data_governance.models import LineageNode, SchemaVersionRef, TrustVerdict
from typing import Dict, Any
from app.governance.models import (
    CandidateBundle,
    CandidateBundleSpec,
    BundleLineage,
    CandidateBundleVersion,
    BundleStageState,
)
from app.governance.enums import BundleType, BundleStage
import uuid


class CandidateAssembler:
    def assemble(
        self, refresh_run_id: str, refs: Dict[str, Any], parent_id: str = None
    ) -> CandidateBundle:
        spec = CandidateBundleSpec(
            strategy_preset_refs=refs.get("strategy_presets", []),
            model_refs=refs.get("models", []),
            feature_set_refs=refs.get("feature_sets", []),
            risk_profile_refs=refs.get("risk_profiles", []),
            portfolio_profile_refs=refs.get("portfolio_profiles", []),
        )
        lineage = BundleLineage(
            parent_bundle_id=parent_id,
            refresh_run_id=refresh_run_id,
            creation_reason="Scheduled refresh candidate",
        )
        version = CandidateBundleVersion(
            major=1, minor=0, patch=0
        )  # Logic to increment based on parent

# Cross-book integration: append policy refs
        overlay = CrossBookOverlay()
        decision = overlay.decide()
        if decision.verdict == CrossBookVerdict.BLOCK:
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"Candidate assembled but cross-book is in block state: {decision.reasons}")

        return CandidateBundle(
            bundle_id=f"bundle_{uuid.uuid4().hex[:8]}",
            bundle_type=BundleType.FULL,
            version=version,
            spec=spec,
            lineage=lineage,
            stage_state=BundleStageState(stage=BundleStage.CANDIDATE),
        )
