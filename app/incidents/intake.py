from typing import Dict, Any, List


class IncidentIntake:
    @staticmethod
    def register_signal(
        signal_type: str, severity: str, details: Dict[str, Any]
    ) -> dict:
        performance_signals = [
            "benchmark_integrity_broken",
            "attribution_chain_missing_critical",
            "performance_equivalence_broken",
            "unexplained_pnl_component_cluster",
            "opportunity_surface_misclassification",
            "runtime_performance_manifest_missing",
        ]

        return {
            "signal_type": signal_type,
            "severity": severity,
            "is_performance_related": signal_type in performance_signals,
            "details": details,
        }
