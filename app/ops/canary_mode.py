from app.ops.models import CanaryModeConfig


class CanaryModeController:
    def __init__(self, config: CanaryModeConfig):
        self.config = config
        self.order_count = 0
        self.risk_used = 0.0

    def is_active(self) -> bool:
        return self.config.enabled

    def can_submit_order(self, risk_amount: float) -> bool:
        if not self.is_active():
            return False
        if self.order_count >= self.config.max_orders:
            print("[CANARY] Max order limit reached.")
            return False
        if self.risk_used + risk_amount > self.config.max_risk_usd:
            print("[CANARY] Max risk limit reached.")
            return False
        return True

    def record_order(self, risk_amount: float) -> None:
        self.order_count += 1
        self.risk_used += risk_amount
