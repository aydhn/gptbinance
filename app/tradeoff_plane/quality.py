from typing import Dict, Any

class TradeoffQuality:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        result = {"status": "ok"}
        if context.get("hidden_burden_shift") or context.get("metric_gaming"):
            result["status"] = "caution"
            result["reason"] = "adversarial_sensitivity"
        return result
class QualityChecker:
    pass
quality_checker = QualityChecker()
