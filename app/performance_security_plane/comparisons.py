from app.performance_security_plane.models import SecurityComparisonRecord

class ComparisonsManager:
    def create_comparison(self, comparison_id: str, target_a_id: str, target_b_id: str, comp_type: str, verdict: str) -> SecurityComparisonRecord:
        return SecurityComparisonRecord(
            comparison_id=comparison_id,
            target_a_id=target_a_id,
            target_b_id=target_b_id,
            type=comp_type,
            verdict=verdict
        )
