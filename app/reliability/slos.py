class AllocationIntegritySLOs:
    def get_slos(self) -> dict:
        return {
            "runtime_equivalence_cleanliness": 0.999,
            "budget_integrity_cleanliness": 1.0,
            "concentration_breach_near_miss_rate": 0.05
        }
