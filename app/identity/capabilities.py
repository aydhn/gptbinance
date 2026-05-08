class UserCapabilities:
    @staticmethod
    def get_performance_capabilities() -> list:
        return [
            "inspect_performance_manifest",
            "review_benchmark_integrity",
            "review_performance_attribution",
            "review_opportunity_surface",
            "review_performance_equivalence",
        ]
