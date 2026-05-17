import pytest
from app.environment_plane.divergence_intent import define_intended_divergence
from app.environment_plane.enums import DivergenceClass

def test_define_intended_divergence():
    divergence = define_intended_divergence(DivergenceClass.INTENDED_BUDGET, "Cost savings")
    assert divergence.divergence_class == DivergenceClass.INTENDED_BUDGET
    assert divergence.justification_notes == "Cost savings"
