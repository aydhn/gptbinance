class ReferencePriceEngine:
    """Determines reference price based on market truth context."""

    @staticmethod
    def get_reference_price(market_data: dict, routing_urgency: str) -> float:
        # Example logic: for passive, try to fetch mid or best bid/ask
        # For aggressive, might take opposite side book price

        # Simplified:
        best_bid = market_data.get("best_bid", 0.0)
        best_ask = market_data.get("best_ask", 0.0)

        if not best_bid or not best_ask:
             return market_data.get("last_price", 0.0)

        mid = (best_bid + best_ask) / 2.0
        return mid
