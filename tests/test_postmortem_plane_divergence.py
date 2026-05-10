import pytest
from app.postmortem_plane.divergence import PostmortemDivergenceEvaluator

def test_divergence():
    div = PostmortemDivergenceEvaluator.evaluate("D-1", ["live", "paper"], True, False)
    assert div.cause_disagreement == True
    assert div.divergence_severity == "HIGH"
