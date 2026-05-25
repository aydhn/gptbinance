from app.performance_security_plane.models import CollateralRecord
from app.performance_security_plane.enums import CollateralClass

class CollateralManager:
    def create_collateral(self, collateral_id: str, security_id: str, col_type: CollateralClass) -> CollateralRecord:
        return CollateralRecord(
            collateral_id=collateral_id,
            security_id=security_id,
            type=col_type,
            lineage_refs=[f"collateral_{collateral_id}"]
        )
