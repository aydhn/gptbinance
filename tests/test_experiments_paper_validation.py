from app.experiments.paper_validation import PaperValidationRecommender


def test_paper_validation_recommender():
    rec = PaperValidationRecommender()
    assert (
        rec.recommend_next_step({"verdict": "improvement"})
        == "qualifies_for_paper_shadow"
    )
    assert rec.recommend_next_step({"verdict": "mixed"}) == "keep_researching"
