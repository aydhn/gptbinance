from app.ops.models import ShadowModeConfig


class ShadowModeController:
    def __init__(self, config: ShadowModeConfig):
        self.config = config

    def is_active(self) -> bool:
        return self.config.enabled

    def get_paper_symbols(self) -> list[str]:
        return self.config.paper_symbols

    def route_order(self, order_intent: dict) -> None:
        if not self.is_active():
            raise RuntimeError("Shadow mode is not active.")
        print(f"[SHADOW SINK] Simulated execution for order: {order_intent}")
