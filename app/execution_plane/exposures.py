class ExposureDeltaEngine:
    @staticmethod
    def calculate_delta(fill_qty: float, price: float, side: str) -> dict:
         sign = 1 if side.lower() == "buy" else -1
         realized_notional = fill_qty * price * sign
         return {
             "qty_delta": fill_qty * sign,
             "notional_delta": realized_notional
         }
