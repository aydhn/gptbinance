from typing import Dict, List
from app.semantic_plane.models import UnitRecord
from app.semantic_plane.exceptions import InvalidUnitMappingError

class UnitManager:
    def __init__(self, registry):
        self.registry = registry
        self.units: Dict[str, UnitRecord] = {}

    def register_unit(self, unit: UnitRecord):
        if not unit.semantic_id or not unit.unit_id:
            raise InvalidUnitMappingError("Unit must have unit_id and semantic_id")
        self.units[unit.unit_id] = unit

    def get_units_with_caveats(self) -> List[UnitRecord]:
        return [u for u in self.units.values() if u.conversion_caveats]
