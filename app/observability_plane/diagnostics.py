from typing import Dict, Any, List

class DiagnosticsExporter:
    @staticmethod
    def export(context: Dict[str, Any]) -> List[str]:
        diagnostics = []
        if context.get("metric_gaming"): diagnostics.append("metric_gaming")
        if context.get("approval_laundering"): diagnostics.append("approval_laundering")
        if context.get("anomaly_suppression"): diagnostics.append("anomaly_suppression")
        return diagnostics
