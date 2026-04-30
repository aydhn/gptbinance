from typing import Dict, List, Optional
from app.governance.models import CandidateBundle
from app.governance.enums import BundleStage
from app.governance.exceptions import StageTransitionError


class BundleRegistry:
    def __init__(self):
        self._bundles: Dict[str, CandidateBundle] = {}

    def register(self, bundle: CandidateBundle):
        self._bundles[bundle.bundle_id] = bundle

    def get(self, bundle_id: str) -> Optional[CandidateBundle]:
        return self._bundles.get(bundle_id)

    def list_all(self) -> List[CandidateBundle]:
        return list(self._bundles.values())

    def update_stage(self, bundle_id: str, new_stage: BundleStage, notes: str = ""):
        bundle = self.get(bundle_id)
        if not bundle:
            raise StageTransitionError(f"Bundle {bundle_id} not found")
        # Optional: Add strict state machine transitions here
        bundle.stage_state.stage = new_stage
        bundle.stage_state.notes = notes

    def get_active_bundle(self) -> Optional[CandidateBundle]:
        for b in self._bundles.values():
            if b.stage_state.stage == BundleStage.ACTIVE:
                return b
        return None
