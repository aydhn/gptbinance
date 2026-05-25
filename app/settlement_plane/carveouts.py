from app.settlement_plane.models import CarveOutRecord, CarveOutClass
from app.settlement_plane.exceptions import InvalidCarveOutError

def evaluate_carveout(carveout: CarveOutRecord):
    if not carveout.details:
        raise InvalidCarveOutError(f"Carve-out {carveout.id} missing details")
    return {"status": "valid", "carveout_id": carveout.id, "class": carveout.carveout_class.value}
