class ReliabilitySLOs:
    @staticmethod
    def get_slos_for_domain(domain: str) -> list:
        if domain == "performance_integrity":
            return [
                "benchmark_freshness_cleanliness_99_9",
                "attribution_completeness_99_9",
                "performance_manifest_equivalence_cleanliness_99",
                "unexplained_residual_burden_ceiling_5_pct",
                "trusted_performance_degraded_ratio_below_1_pct",
            ]
        return []
