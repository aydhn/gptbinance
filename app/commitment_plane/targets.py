from app.commitment_plane.models import TargetRecord

class TargetManager:
    @staticmethod
    def create_target(target_type: str, description: str, warnings: str = "TARGET IS NOT A COMMITMENT") -> TargetRecord:
        if not description:
            raise ValueError("Target description cannot be empty")
        return TargetRecord(
            target_type=target_type,
            description=description,
            warnings=warnings,
            lineage_refs=[]
        )
