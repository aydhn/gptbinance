from app.commitment_plane.models import CommitmentComparisonRecord

class ComparisonManager:
    @staticmethod
    def create_comparison(comparison_type: str, description: str) -> CommitmentComparisonRecord:
        valid_types = ['promised_vs_delivered', 'internal_vs_external', 'committed_vs_aspirational', 'breach_before_vs_relief_after']
        if comparison_type not in valid_types:
            raise ValueError(f"Invalid comparison type. Must be one of {valid_types}")

        return CommitmentComparisonRecord(
            comparison_type=comparison_type,
            description=description,
            lineage_refs=[]
        )
