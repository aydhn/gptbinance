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


def verify_promise_beneficiary(promise_id: str, beneficiary_id: str, rights_registry) -> str:
    if not rights_registry.is_beneficiary_recognized(beneficiary_id):
        return "explicit caution: promise fulfilled claim under unrecognized beneficiary right"
    return "trusted"
