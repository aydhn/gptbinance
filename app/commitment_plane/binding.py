from app.commitment_plane.models import BindingStrengthRecord
from app.commitment_plane.enums import BindingClass

class BindingManager:
    @staticmethod
    def create_binding(binding_class: BindingClass, notes: str = None) -> BindingStrengthRecord:
        return BindingStrengthRecord(
            binding_class=binding_class,
            notes=notes,
            lineage_refs=[]
        )
