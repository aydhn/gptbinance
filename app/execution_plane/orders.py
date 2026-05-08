from app.execution_plane.models import OrderSpec
from app.execution_plane.exceptions import InvalidOrderSpecError
from app.execution_plane.enums import OrderType, TIFClass


class OrderSpecValidator:
    """Validates order specification internals."""

    @staticmethod
    def validate(spec: OrderSpec):
        if spec.qty <= 0:
            raise InvalidOrderSpecError("Order qty must be positive.")

        if spec.order_type in [
            OrderType.LIMIT,
            OrderType.STOP_LOSS_LIMIT,
            OrderType.TAKE_PROFIT_LIMIT,
        ]:
            if not spec.price:
                raise InvalidOrderSpecError(f"Price is required for limit order types.")

        if spec.order_type in [
            OrderType.STOP_LOSS_LIMIT,
            OrderType.TAKE_PROFIT_LIMIT,
            OrderType.STOP_MARKET,
            OrderType.TAKE_PROFIT_MARKET,
        ]:
            if not spec.stop_price:
                raise InvalidOrderSpecError(
                    f"Stop price is required for stop order types."
                )

        if spec.is_post_only and spec.order_type == OrderType.MARKET:
            raise InvalidOrderSpecError("Market orders cannot be post-only.")

        # Post-only usually implies GTX
        if spec.is_post_only and spec.tif != TIFClass.GTX:
            pass  # just a warning in real life, but we allow it as typed

        return True
