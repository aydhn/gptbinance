from typing import Dict, Any, List

class QualityEvaluator:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        warnings = []
        if context.get("suspicion_theater", False):
            warnings.append("suspicion_theater_warning")
        if context.get("metric_gaming", False):
            warnings.append("metric_gaming_warning")
        if context.get("approval_laundering", False):
            warnings.append("approval_laundering_warning")
        if context.get("evidence_poisoning", False):
            warnings.append("evidence_poisoning_warning")
        if context.get("exploit_normalization", False):
            warnings.append("exploit_normalization_warning")
        if context.get("control_comfort", False):
            warnings.append("control_comfort_warning")

        verdict = "pass" if not warnings else "degraded"
        return {
            "warnings": warnings,
            "quality_verdict": verdict
        }
