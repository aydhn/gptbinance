from .models import CrossBookOverlayDecision
from .enums import CrossBookVerdict

class CrossBookOverlay:
    def decide(self) -> CrossBookOverlayDecision:
        return CrossBookOverlayDecision(verdict=CrossBookVerdict.ALLOW, reasons=["No conflicts"])
