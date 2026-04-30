from typing import Dict
from app.products.enums import ProductType, PositionMode
from app.products.registry import ProductRegistry
from .exceptions import InvalidMarginModeTransition # Reusing exception type conceptually or create a new one if preferred

class PositionModeManager:
    def __init__(self, registry: ProductRegistry):
        self.registry = registry
        self._state: Dict[str, PositionMode] = {} # product_type -> position_mode

    def get_mode(self, product_type: ProductType) -> PositionMode:
        return self._state.get(product_type.value, PositionMode.ONE_WAY)

    def set_mode(self, product_type: ProductType, requested_mode: PositionMode) -> PositionMode:
        desc = self.registry.get_descriptor(product_type)

        if requested_mode not in desc.capabilities.supported_position_modes:
            raise InvalidMarginModeTransition(f"Position mode {requested_mode} is not supported for {product_type}")

        self._state[product_type.value] = requested_mode
        return requested_mode
