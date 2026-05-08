class RunbookRefs:
    @staticmethod
    def get_performance_runbooks() -> dict:
        return {
            "performance_trust_degraded": "runbooks/performance_integrity_review.md",
            "benchmark_integrity_broken": "runbooks/benchmark_integrity_review.md",
            "unexplained_pnl_component_elevated": "runbooks/unexplained_pnl_analysis.md",
            "performance_equivalence_broken": "runbooks/performance_equivalence_review.md",
            "attribution_review_required": "runbooks/attribution_gap_investigation.md",
            "opportunity_surface_caution_elevated": "runbooks/opportunity_surface_caveat_review.md",
        }
