from app.commitment_plane.models import AsymmetryRecord
from app.commitment_plane.enums import AsymmetryClass

class AsymmetryManager:
    @staticmethod
    def create_asymmetry(asymmetry_class: AsymmetryClass, description: str, burden_notes: str = None) -> AsymmetryRecord:
        return AsymmetryRecord(
            asymmetry_class=asymmetry_class,
            description=description,
            burden_notes=burden_notes,
            lineage_refs=[]
        )
