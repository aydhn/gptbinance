from typing import Dict
from app.products.enums import ProductType, MarginMode
from app.products.registry import ProductRegistry
from .exceptions import InvalidMarginModeTransition


class MarginModeManager:
    def __init__(self, registry: ProductRegistry):
        self.registry = registry
        self._state: Dict[str, Dict[str, MarginMode]] = (
            {}
        )  # product_type -> symbol -> margin_mode

    def get_mode(self, product_type: ProductType, symbol: str) -> MarginMode:
        return self._state.get(product_type.value, {}).get(symbol, MarginMode.ISOLATED)

    def set_mode(
        self, product_type: ProductType, symbol: str, requested_mode: MarginMode
    ) -> MarginMode:
        desc = self.registry.get_descriptor(product_type)

        if requested_mode not in desc.capabilities.supported_margin_modes:
            raise InvalidMarginModeTransition(
                f"Margin mode {requested_mode} is not supported for {product_type}"
            )

        if product_type.value not in self._state:
            self._state[product_type.value] = {}

        self._state[product_type.value][symbol] = requested_mode
        return requested_mode
