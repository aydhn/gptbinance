from app.replay.scoring import DummyScorer
from app.replay.enums import ReplayVerdict


def test_scoring():
    scorer = DummyScorer()
    score = scorer.score()
    assert score.overall_score == 1.0
    assert score.verdict == ReplayVerdict.TRUSTED
