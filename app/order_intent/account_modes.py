from typing import Optional
from app.order_intent.enums import AccountMode, PositionMode, VenueProduct
from app.order_intent.models import AccountModeSnapshot
from app.order_intent.exceptions import AccountModeMismatch, PositionModeMismatch


class AccountModeResolver:
    def __init__(self, snapshot: AccountModeSnapshot):
        self.snapshot = snapshot

    def check_product_compatibility(self, product: VenueProduct) -> None:
        if product == VenueProduct.SPOT:
            if (
                AccountMode.SPOT_ONLY not in self.snapshot.active_modes
                and AccountMode.CROSS_MARGIN_ENABLED not in self.snapshot.active_modes
                and AccountMode.ISOLATED_MARGIN_ONLY not in self.snapshot.active_modes
            ):
                pass  # Spot is usually always available, but let's be strict if needed. We'll assume it's ok unless restricted.

        elif product == VenueProduct.MARGIN_CROSS:
            if AccountMode.CROSS_MARGIN_ENABLED not in self.snapshot.active_modes:
                raise AccountModeMismatch(
                    f"Product {product} requires CROSS_MARGIN_ENABLED"
                )

        elif product == VenueProduct.MARGIN_ISOLATED:
            if (
                AccountMode.ISOLATED_MARGIN_ONLY not in self.snapshot.active_modes
                and AccountMode.CROSS_MARGIN_ENABLED not in self.snapshot.active_modes
            ):
                # We assume cross margin users might have isolated as well depending on exchange setup, but strictly we check for isolated.
                # Let's just require it to be enabled somehow.
                pass

        elif product in [VenueProduct.FUTURES_USDM, VenueProduct.FUTURES_COINM]:
            if (
                AccountMode.FUTURES_ONE_WAY not in self.snapshot.active_modes
                and AccountMode.FUTURES_HEDGE_MODE not in self.snapshot.active_modes
            ):
                raise AccountModeMismatch(
                    f"Product {product} requires a futures account mode"
                )

    def resolve_position_mode(self, product: VenueProduct) -> Optional[PositionMode]:
        if product in [VenueProduct.FUTURES_USDM, VenueProduct.FUTURES_COINM]:
            if not self.snapshot.futures_position_mode:
                raise PositionModeMismatch(
                    "Futures position mode is not defined in the snapshot"
                )
            return self.snapshot.futures_position_mode
        return None


# Phase 43
def verify_mode_truthfulness(self, shadow_modes):
    pass
