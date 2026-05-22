from typing import Dict, Any

class TradeoffLinkage:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "metric_gaming_incentives": context.get("metric_gaming_incentives", []),
            "burden_hiding_via_optimization": context.get("burden_hiding_via_optimization", "unknown"),
            "local_optimum_manipulation": context.get("local_optimum_manipulation", "unknown"),
            "tradeoff_proof_notes": "No tradeoff-safe claim without anti-gaming posture",
            "sacrifice_notes": []
        }
