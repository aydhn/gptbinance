from app.settlement_plane.models import ConsiderationRecord, ConsiderationClass
from app.settlement_plane.exceptions import InvalidConsiderationError

def evaluate_consideration(consideration: ConsiderationRecord):
    if consideration.consideration_class == ConsiderationClass.INSUFFICIENT:
        raise InvalidConsiderationError(f"Consideration {consideration.id} is insufficient")
    if not consideration.value:
        raise InvalidConsiderationError(f"Consideration {consideration.id} missing value")
    return {"status": "valid", "consideration_id": consideration.id, "class": consideration.consideration_class.value}
