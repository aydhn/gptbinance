import uuid
from datetime import datetime, timezone
from typing import List, Dict
from app.universe.models import (
    UniverseSnapshot,
    ProductInstrument,
    InstrumentRef,
    UniverseEligibilityResult,
)
from app.workspaces.enums import ProfileType
from app.universe.enums import EligibilityVerdict


class SnapshotBuilder:
    def build(
        self, profile: ProfileType, evaluations: List[UniverseEligibilityResult]
    ) -> UniverseSnapshot:
        eligible = []
        caution = []
        blocked = []

        for eval_res in evaluations:
            if eval_res.verdict == EligibilityVerdict.ELIGIBLE:
                eligible.append(eval_res.ref)
            elif eval_res.verdict == EligibilityVerdict.CAUTION:
                caution.append(eval_res.ref)
            else:
                blocked.append(eval_res.ref)

        snapshot_id = f"snap_{uuid.uuid4().hex[:8]}"

        return UniverseSnapshot(
            snapshot_id=snapshot_id,
            profile=profile,
            created_at=datetime.now(timezone.utc),
            eligible_instruments=eligible,
            caution_instruments=caution,
            blocked_instruments=blocked,
            manifest_ref=f"manifest_{snapshot_id}",
        )
