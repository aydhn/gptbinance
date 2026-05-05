"""
overlay.py
"""
from datetime import datetime, timezone
from typing import List

from app.crossbook.models import (
    CrossBookOverlayDecision,
    CrossBookConflict,
    NetExposureSnapshot,
    CollateralPressureReport,
    BorrowDependencyReport,
    FundingBurdenOverlay,
)
from app.crossbook.enums import (
    CrossBookVerdict,
    OverlayReasonType,
    ConflictSeverity,
    FundingBurdenClass,
    BorrowDependencyClass,
)
from app.crossbook.policies import CrossBookPolicyManager


class CrossBookOverlayEngine:
    def __init__(self, policy: CrossBookPolicyManager):
        self.policy = policy

    def evaluate(
        self,
        conflicts: List[CrossBookConflict],
        net_exp: NetExposureSnapshot,
        col_rep: CollateralPressureReport,
        bor_rep: BorrowDependencyReport,
        fun_rep: FundingBurdenOverlay,
    ) -> CrossBookOverlayDecision:
        reasons: List[str] = []
        verdict = CrossBookVerdict.ALLOW

        for c in conflicts:
            if c.conflict_type == OverlayReasonType.FAKE_HEDGE_DETECTED:
                if c.severity in [ConflictSeverity.HIGH, ConflictSeverity.CRITICAL]:
                    verdict = CrossBookVerdict.BLOCK
                    reasons.append(f"Blocked due to severe fake hedge in {c.asset}")
                elif verdict != CrossBookVerdict.BLOCK:
                    verdict = CrossBookVerdict.CAUTION
                    reasons.append(f"Caution due to fake hedge in {c.asset}")

            if c.conflict_type == OverlayReasonType.LEVERAGE_STACKING:
                if c.severity in [ConflictSeverity.HIGH, ConflictSeverity.CRITICAL]:
                    verdict = CrossBookVerdict.REDUCE
                    reasons.append(
                        f"Reduce exposure due to leverage stacking in {c.asset}"
                    )

        if col_rep.pressure_ratio > 0.8:
            verdict = CrossBookVerdict.REDUCE
            reasons.append("High collateral pressure detected")

        if bor_rep.dependency_class == BorrowDependencyClass.HIGH:
            verdict = max(
                verdict,
                CrossBookVerdict.CAUTION,
                key=lambda x: [
                    CrossBookVerdict.ALLOW,
                    CrossBookVerdict.CAUTION,
                    CrossBookVerdict.DEFER,
                    CrossBookVerdict.REDUCE,
                    CrossBookVerdict.BLOCK,
                ].index(x),
            )
            reasons.append("Elevated borrow dependency detected")

        if fun_rep.burden_class == FundingBurdenClass.SEVERE:
            verdict = max(
                verdict,
                CrossBookVerdict.CAUTION,
                key=lambda x: [
                    CrossBookVerdict.ALLOW,
                    CrossBookVerdict.CAUTION,
                    CrossBookVerdict.DEFER,
                    CrossBookVerdict.REDUCE,
                    CrossBookVerdict.BLOCK,
                ].index(x),
            )
            reasons.append("Severe funding burden detected")

        if net_exp.total_net_notional > self.policy.get_max_combined_exposure():
            verdict = CrossBookVerdict.BLOCK
            reasons.append(
                f"Max combined exposure breached for profile {self.policy.profile}"
            )

        if not reasons:
            reasons.append("No cross-book issues detected")

        return CrossBookOverlayDecision(
            verdict=verdict,
            reasons=reasons,
            conflicts=conflicts,
            timestamp=datetime.now(timezone.utc),
        )


# Phase 43
def shadow_position_posture_overlay(self):
    pass
