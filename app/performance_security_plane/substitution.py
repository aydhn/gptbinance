from app.performance_security_plane.models import SubstituteCollateralRecord

class SubstitutionManager:
    def create_substitute_collateral(self, substitution_id: str, original_security_id: str, new_security_id: str, sub_type: str) -> SubstituteCollateralRecord:
        return SubstituteCollateralRecord(
            substitution_id=substitution_id,
            original_security_id=original_security_id,
            new_security_id=new_security_id,
            type=sub_type,
            lineage_refs=[f"substitute_{substitution_id}"]
        )
