from app.performance_security_plane.models import CollateralPoolRecord

class CollateralPoolManager:
    def create_pool(self, pool_id: str, pool_type: str, opacity_caution: str = None) -> CollateralPoolRecord:
        return CollateralPoolRecord(
            pool_id=pool_id,
            type=pool_type,
            opacity_caution=opacity_caution,
            lineage_refs=[f"pool_{pool_id}"]
        )
