import uuid
from typing import List, Dict, Any
from datetime import datetime, timezone
from app.events.base import EventOverlayEngineBase
from app.events.models import EventRecord, EventRiskOverlay
from app.events.enums import EventGateVerdict, EventSeverity
from app.events.windows import calculate_window, merge_windows
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict


class DefaultOverlayEngine(EventOverlayEngineBase):
    def generate_overlay(
        self, events: List[EventRecord], profile_id: str
    ) -> EventRiskOverlay:
        now = datetime.now(timezone.utc)
        windows = [calculate_window(e) for e in events]
        merged_windows = merge_windows(windows)

        active_windows = [
            w for w in merged_windows if w.start_time <= now <= w.end_time
        ]

        verdict = EventGateVerdict.ALLOW
        reasons = []

        for w in active_windows:
            if w.max_severity == EventSeverity.CRITICAL:
                verdict = EventGateVerdict.BLOCK
                reasons.append("Critical event window active")
            elif (
                w.max_severity == EventSeverity.HIGH
                and verdict != EventGateVerdict.BLOCK
            ):
                verdict = EventGateVerdict.REDUCE_ONLY
                reasons.append("High severity event window active")

        crossbook_fake_hedge_reasons = []  # mock
        if crossbook_fake_hedge_reasons:
            reasons.extend(crossbook_fake_hedge_reasons)

        if not reasons:
            reasons.append("No active critical/high events")

        return EventRiskOverlay(
            overlay_id=str(uuid.uuid4()),
            timestamp=now,
            active_windows=active_windows,
            verdict=verdict,
            reasons=reasons,
        )

    def get_policy_domain_outputs(self, overlay: EventRiskOverlay) -> Dict[str, Any]:
        """Expose Event Overlay outputs for Policy Kernel Domain format"""
        verdict = PolicyVerdict.ALLOW
        if overlay.verdict == EventGateVerdict.BLOCK:
            verdict = PolicyVerdict.BLOCK
        elif overlay.verdict == EventGateVerdict.HALT:
            verdict = PolicyVerdict.HARD_BLOCK
        elif overlay.verdict == EventGateVerdict.REDUCE_ONLY:
            verdict = PolicyVerdict.CAUTION

        return {
            "domain": PolicyDomain.EVENT_RISK,
            "reasons": overlay.reasons,
            "verdict": verdict,
        }
