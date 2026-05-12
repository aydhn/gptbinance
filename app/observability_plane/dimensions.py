from typing import Dict, List, Optional
from .models import DimensionDefinition
from .exceptions import InvalidDimensionOrTagError

class DimensionRegistry:
    def __init__(self):
        self._dimensions: Dict[str, DimensionDefinition] = {}

    def register_dimension(self, dim: DimensionDefinition) -> None:
        if not dim.scope:
            raise InvalidDimensionOrTagError("Dimension must declare an explicit scope.")
        self._dimensions[dim.dimension_id] = dim

    def get_dimension(self, dimension_id: str) -> Optional[DimensionDefinition]:
        return self._dimensions.get(dimension_id)

    def list_dimensions(self) -> List[DimensionDefinition]:
        return list(self._dimensions.values())
