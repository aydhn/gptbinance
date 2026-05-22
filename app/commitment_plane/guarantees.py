from app.commitment_plane.models import GuaranteeRecord
from app.commitment_plane.enums import GuaranteeClass

class GuaranteeManager:
    @staticmethod
    def create_guarantee(guarantee_class: GuaranteeClass, description: str, caveats: str = None) -> GuaranteeRecord:
        if not description:
            raise ValueError("Guarantee description cannot be empty")
        return GuaranteeRecord(
            guarantee_class=guarantee_class,
            description=description,
            caveats=caveats,
            lineage_refs=[]
        )
