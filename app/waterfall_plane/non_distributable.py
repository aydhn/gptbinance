from app.waterfall_plane.models import NonDistributableComponentRecord

def register_non_distributable(component_id: str, amount: float) -> NonDistributableComponentRecord:
    return NonDistributableComponentRecord(component_id=component_id, amount=amount)
