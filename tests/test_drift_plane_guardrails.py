import pytest
from app.drift_plane.guardrails import GuardrailManager
from app.drift_plane.enums import GuardrailClass

def test_guardrail_deviation_creation():
    manager = GuardrailManager()
    manager.add_deviation("dev-1", GuardrailClass.WEAKENED, "guardrail-1")

    deviation = manager.get_deviation("dev-1")
    assert deviation is not None
    assert deviation.deviation_id == "dev-1"
    assert deviation.class_type == GuardrailClass.WEAKENED
    assert deviation.guardrail_id == "guardrail-1"
