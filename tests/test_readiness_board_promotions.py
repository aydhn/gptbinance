from app.readiness_board.promotions import PromotionManager
from app.readiness_board.enums import PromotionStage


def test_promotion_manager():
    manager = PromotionManager()
    plan1 = manager.evaluate_path("c1", PromotionStage.CANDIDATE_REGISTRY)
    assert plan1.allowed is True
    assert plan1.target_stage == PromotionStage.PAPER_SHADOW

    plan2 = manager.evaluate_path("c1", PromotionStage.LIVE)
    assert plan2.allowed is False
