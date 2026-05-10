import pytest
from app.postmortem_plane.effectiveness import EffectivenessEvaluator
from app.postmortem_plane.models import ActionVerificationRecord
from app.postmortem_plane.enums import VerificationClass, EffectivenessClass

def test_effectiveness_evaluator():
    v = ActionVerificationRecord(verification_id="V-1", verification_class=VerificationClass.EFFECTIVENESS, proof_notes="verified", effectiveness=EffectivenessClass.OBSERVED_IMPROVEMENT)
    eff = EffectivenessEvaluator.evaluate(v)
    assert eff == EffectivenessClass.OBSERVED_IMPROVEMENT
