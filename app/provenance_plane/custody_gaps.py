from typing import Dict, Any

class CustodyGaps:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        result = {"status": "ok"}
        if context.get("manual_edit") or context.get("hidden_lineage"):
            result["status"] = "caution"
            result["reason"] = "custody_gap_under_exploit_incentive"
        return result
