from app.commitment_plane.models import PromiseRecord
from app.commitment_plane.enums import PromiseClass

class PromiseManager:
    @staticmethod
    def create_promise(promise_class: PromiseClass, description: str, caveats: str = None) -> PromiseRecord:
        if not description:
            raise ValueError("Promise description cannot be empty")
        return PromiseRecord(
            promise_class=promise_class,
            description=description,
            caveats=caveats,
            lineage_refs=[]
        )
