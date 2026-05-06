from typing import Dict, List
import uuid
from app.reliability.enums import ReliabilityDomain, SLOClass
from app.reliability.models import SLODefinition, SLOTarget, SLOWindow
from app.reliability.exceptions import InvalidSLODefinition, ReliabilityTowerError


class SLORegistry:
    def __init__(self):
        self._slos: Dict[str, SLODefinition] = {}
        self._initialize_predefined_slos()

    def _initialize_predefined_slos(self):
        # Sample SLOs
        predefined = [
            SLODefinition(
                slo_id="slo_market_truth_freshness",
                domain=ReliabilityDomain.MARKET_TRUTH,
                slo_class=SLOClass.CRITICAL,
                name="Market Truth Freshness",
                description="Market data freshness should be under 500ms for 99% of requests.",
                target=SLOTarget(target_value=500.0, is_upper_bound=True, unit="ms"),
                windows=[
                    SLOWindow(window_id="w_short", duration_seconds=3600),
                    SLOWindow(window_id="w_long", duration_seconds=86400),
                ],
            ),
            SLODefinition(
                slo_id="slo_sequence_integrity",
                domain=ReliabilityDomain.MARKET_TRUTH,
                slo_class=SLOClass.CRITICAL,
                name="Sequence Integrity",
                description="No more than 0.1% sequence gaps per hour.",
                target=SLOTarget(
                    target_value=0.1, is_upper_bound=True, unit="percentage"
                ),
                windows=[SLOWindow(window_id="w_short", duration_seconds=3600)],
            ),
            SLODefinition(
                slo_id="slo_shadow_cleanliness",
                domain=ReliabilityDomain.SHADOW_TRUTHFULNESS,
                slo_class=SLOClass.HIGH,
                name="Shadow Cleanliness",
                description="Unresolved critical drift age should be less than 60 minutes.",
                target=SLOTarget(
                    target_value=60.0, is_upper_bound=True, unit="minutes"
                ),
                windows=[SLOWindow(window_id="w_long", duration_seconds=86400)],
            ),
        ]
        for s in predefined:
            self.register(s)

    def register(self, slo: SLODefinition):
        if slo.slo_id in self._slos:
            raise InvalidSLODefinition(f"SLO {slo.slo_id} already registered.")
        if slo.target.target_value < 0:
            raise InvalidSLODefinition(
                f"SLO {slo.slo_id} target value cannot be negative."
            )
        self._slos[slo.slo_id] = slo

    def get(self, slo_id: str) -> SLODefinition:
        if slo_id not in self._slos:
            raise ReliabilityTowerError(f"SLO {slo_id} not found.")
        return self._slos[slo_id]

    def list_all(self) -> List[SLODefinition]:
        return list(self._slos.values())

    def get_by_domain(self, domain: ReliabilityDomain) -> List[SLODefinition]:
        return [slo for slo in self._slos.values() if slo.domain == domain]


slo_registry = SLORegistry()
