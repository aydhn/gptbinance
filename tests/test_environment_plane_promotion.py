import pytest
from app.environment_plane.promotion import define_promotion_path
from app.environment_plane.enums import PromotionClass

def test_define_promotion_path():
    path = define_promotion_path(PromotionClass.PROBATION_TO_LIVE, "Verified")
    assert path.promotion_class == PromotionClass.PROBATION_TO_LIVE
    assert path.proof_notes == "Verified"
