class CanonicalReviewClass:
    PERFORMANCE_INTEGRITY_REVIEW = "performance_integrity_review"
    BENCHMARK_REVIEW = "benchmark_review"
    ATTRIBUTION_REVIEW = "attribution_review"
    OPPORTUNITY_SURFACE_REVIEW = "opportunity_surface_review"
    PERFORMANCE_EQUIVALENCE_REVIEW = "performance_equivalence_review"
    UNEXPLAINED_PNL_REVIEW = "unexplained_pnl_review"


class ReviewRequestMetadataBuilder:
    @staticmethod
    def build_performance_metadata(manifest_id: str, trust_verdict: str) -> dict:
        return {
            "performance_manifest_id": manifest_id,
            "performance_trust_verdict": trust_verdict,
        }
