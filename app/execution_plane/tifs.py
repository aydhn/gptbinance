from app.execution_plane.enums import TIFClass, OrderType


class TIFPolicyEngine:
    """Enforces Time-In-Force rules based on venue and order type."""

    @staticmethod
    def get_allowed_tifs(order_type: OrderType, is_post_only: bool) -> list[TIFClass]:
        if order_type == OrderType.MARKET:
            return [TIFClass.IOC, TIFClass.FOK]  # Market usually implies immediate
        elif is_post_only:
            return [TIFClass.GTX]
        else:
            return [TIFClass.GTC, TIFClass.IOC, TIFClass.FOK]

    @staticmethod
    def is_valid(tif: TIFClass, order_type: OrderType, is_post_only: bool) -> bool:
        return tif in TIFPolicyEngine.get_allowed_tifs(order_type, is_post_only)
