from pydantic import BaseModel
from typing import Dict, Optional
from app.products.enums import ProductType
from app.products.registry import ProductRegistry
from .exceptions import InvalidLeverageChange


class LeverageState(BaseModel):
    product_type: ProductType
    symbol: str
    current_leverage: int


class LeverageManager:
    def __init__(self, registry: ProductRegistry):
        self.registry = registry
        self._state: Dict[str, Dict[str, int]] = (
            {}
        )  # product_type -> symbol -> leverage

    def get_leverage(self, product_type: ProductType, symbol: str) -> int:
        return self._state.get(product_type.value, {}).get(symbol, 1)  # Default 1x

    def set_leverage(
        self, product_type: ProductType, symbol: str, requested_leverage: int
    ) -> int:
        desc = self.registry.get_descriptor(product_type)
        if not desc.capabilities.supports_leverage:
            raise InvalidLeverageChange(
                f"Product {product_type} does not support leverage."
            )

        max_allowed = desc.capabilities.max_leverage
        if requested_leverage > max_allowed:
            raise InvalidLeverageChange(
                f"Requested leverage {requested_leverage}x exceeds max allowed {max_allowed}x for {product_type}"
            )

        if requested_leverage < 1:
            raise InvalidLeverageChange("Leverage must be at least 1x.")

        if product_type.value not in self._state:
            self._state[product_type.value] = {}

        self._state[product_type.value][symbol] = requested_leverage
        return requested_leverage
