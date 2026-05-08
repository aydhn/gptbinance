class PaperExecutionEnv:
    """Paper execution mapping and simulation."""
    def __init__(self):
        self.paper_receipts = {}

    def simulate_fill(self, order_spec_id: str, qty: float, price: float, is_maker: bool) -> dict:
        receipt = {
            "spec_id": order_spec_id,
            "filled_qty": qty,
            "avg_price": price,
            "is_maker": is_maker,
            "simulated": True
        }
        self.paper_receipts[order_spec_id] = receipt
        return receipt
