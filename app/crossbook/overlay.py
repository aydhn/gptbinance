class CrossbookOverlay:
    def check_stability(self) -> bool:
        # Cross-book posture and fake hedge risks input for allocation netting
        return True

class CrossbookExecutionOverlay:
    @staticmethod
    def get_hedge_cautions(symbol: str) -> list:
        return [] # No fake hedge warnings by default
