from app.cost_plane.guardrails import GuardrailManager
from app.cost_plane.enums import GuardrailClass

def test_guardrails():
    manager = GuardrailManager()
    rec = manager.evaluate_guardrail("b-1", GuardrailClass.MAX_BURN, 500.0, 600.0)
    assert rec.breached
