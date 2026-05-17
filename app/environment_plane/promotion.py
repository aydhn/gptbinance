from app.environment_plane.models import PromotionPathRecord
from app.environment_plane.enums import PromotionClass

def define_promotion_path(promotion_class: PromotionClass, proof_notes: str) -> PromotionPathRecord:
    return PromotionPathRecord(promotion_class=promotion_class, proof_notes=proof_notes)
