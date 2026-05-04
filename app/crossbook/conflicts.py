"""
conflicts.py
"""
from typing import List
from app.crossbook.base import ConflictDetectorBase
from app.crossbook.models import (
    ExposureGraphModel,
    NetExposureSnapshot,
    CrossBookConflict,
)
from app.crossbook.enums import (
    ExposureClass,
    HedgeQuality,
    OverlayReasonType,
    ConflictSeverity,
)


class ConflictDetector(ConflictDetectorBase):
    def detect(
        self, graph: ExposureGraphModel, net_exposure: NetExposureSnapshot
    ) -> List[CrossBookConflict]:
        conflicts: List[CrossBookConflict] = []

        for asset, exp in net_exposure.assets.items():
            if (
                exp.exposure_class == ExposureClass.NEUTRAL_HEDGED
                and exp.hedge_quality == HedgeQuality.POOR
            ):
                conflicts.append(
                    CrossBookConflict(
                        conflict_type=OverlayReasonType.FAKE_HEDGE_DETECTED,
                        severity=ConflictSeverity.MEDIUM,
                        asset=asset,
                        evidence=f"Hedge ratio is poor for {asset}",
                    )
                )

            # Simple leverage stacking logic mock
            longs = exp.directional.long_notional
            if longs > 10000:  # Arbitrary policy test
                conflicts.append(
                    CrossBookConflict(
                        conflict_type=OverlayReasonType.LEVERAGE_STACKING,
                        severity=ConflictSeverity.HIGH,
                        asset=asset,
                        evidence=f"High long notional exposure across books: {longs}",
                    )
                )

        return conflicts
