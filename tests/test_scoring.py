from app.strategies.scoring import ScoreBuilder


def test_score_builder():
    builder = ScoreBuilder(base_score=10.0)
    builder.add_component("pass_test", 20.0, "reason 1")
    builder.add_component("fail_test", -5.0, "reason 2", is_penalty=True)

    score = builder.build(confidence=0.8, quality=0.9)

    assert score.value == 25.0
    assert score.confidence == 0.8
    assert score.quality == 0.9
    assert score.components["pass_test"] == 20.0
    assert len(builder.rationales) == 2
