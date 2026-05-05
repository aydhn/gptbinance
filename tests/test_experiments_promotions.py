from app.experiments.promotions import CandidatePromotionEvaluator


def test_candidate_promotion_evaluator():
    evaluator = CandidatePromotionEvaluator()
    assert (
        evaluator.evaluate({"verdict": "improvement"}, {"overfit_suspicion": False})
        == "qualifies_for_paper_shadow"
    )
    assert (
        evaluator.evaluate({"verdict": "improvement"}, {"overfit_suspicion": True})
        == "keep_researching"
    )
    assert evaluator.evaluate({"verdict": "mixed"}, {}) == "reject"
