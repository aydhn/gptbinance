from typing import Dict, Any
from app.products.enums import ProductType
from .leverage import LeverageManager
from .margin_modes import MarginModeManager
from .position_modes import PositionModeManager


class DerivativeAccountSync:
    def __init__(
        self,
        leverage_mgr: LeverageManager,
        margin_mgr: MarginModeManager,
        position_mgr: PositionModeManager,
    ):
        self.leverage_mgr = leverage_mgr
        self.margin_mgr = margin_mgr
        self.position_mgr = position_mgr

    def sync_from_exchange(
        self, product_type: ProductType, exchange_data: Dict[str, Any]
    ):
        """
        Mock sync function. In live, this parses exchange API responses to update internal state.
        """
        # E.g. data = {"positions": [{"symbol": "BTCUSDT", "leverage": 3, "marginType": "isolated"}]}
        positions = exchange_data.get("positions", [])
        for pos in positions:
            sym = pos.get("symbol")
            if sym:
                lev = pos.get("leverage")
                if lev:
                    self.leverage_mgr.set_leverage(product_type, sym, lev)

                # Note: Not handling string to enum conversion fully here, keeping it conceptual
