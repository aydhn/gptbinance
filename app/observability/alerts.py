class AlertRules:
    @staticmethod
    def get_performance_alerts() -> list:
        return [
            "performance_trust_degraded",
            "benchmark_integrity_broken",
            "unexplained_pnl_component_elevated",
            "performance_equivalence_broken",
            "attribution_review_required",
            "opportunity_surface_caution_elevated",
        ]
