from app.replay.decision_path import DummyDecisionPathBuilder


def test_decision_path_builder():
    builder = DummyDecisionPathBuilder()
    path = builder.build_dummy_path()
    assert len(path) == 2
    assert path[0].stage == "signal"
    assert path[1].stage == "risk"
