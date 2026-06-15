from app.indemnity_plane.models import BasketRecord
def evaluate_baskets(indemnity_id: str, has_basket: bool) -> BasketRecord:
    return BasketRecord(indemnity_id=indemnity_id, has_basket=has_basket)
