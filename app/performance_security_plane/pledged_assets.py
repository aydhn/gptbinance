from app.performance_security_plane.models import PledgedAssetRecord

class PledgedAssetManager:
    def create_pledged_asset(self, asset_id: str, security_id: str, asset_type: str) -> PledgedAssetRecord:
        return PledgedAssetRecord(
            asset_id=asset_id,
            security_id=security_id,
            type=asset_type,
            lineage_refs=[f"asset_{asset_id}"]
        )
