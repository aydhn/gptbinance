from typing import Dict, List
from app.allocation.models import SleeveDefinition
from app.allocation.enums import SleeveClass
from app.allocation.exceptions import InvalidSleeveDefinition


class SleeveRegistry:
    def __init__(self):
        self._sleeves: Dict[str, SleeveDefinition] = {}
        self._initialize_defaults()

    def _initialize_defaults(self):
        self.register(
            SleeveDefinition(
                sleeve_id="primary_alpha_01",
                sleeve_class=SleeveClass.PRIMARY_ALPHA,
                allowed_instruments=["SPOT", "FUTURES"],
                max_capital_share=0.4,
                conflict_priority=100,
                owner_domain="alpha_squad",
            )
        )
        self.register(
            SleeveDefinition(
                sleeve_id="hedge_overlay_01",
                sleeve_class=SleeveClass.HEDGE_OVERLAY,
                allowed_instruments=["FUTURES"],
                max_capital_share=0.2,
                conflict_priority=200,
                owner_domain="risk_squad",
            )
        )

    def register(self, sleeve: SleeveDefinition):
        if sleeve.max_capital_share <= 0 or sleeve.max_capital_share > 1.0:
            raise InvalidSleeveDefinition("max_capital_share must be > 0 and <= 1.0")
        self._sleeves[sleeve.sleeve_id] = sleeve

    def get_sleeve(self, sleeve_id: str) -> SleeveDefinition:
        if sleeve_id not in self._sleeves:
            raise InvalidSleeveDefinition(f"Sleeve {sleeve_id} not found")
        return self._sleeves[sleeve_id]

    def list_all(self) -> List[SleeveDefinition]:
        return list(self._sleeves.values())
