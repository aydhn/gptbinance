from app.postmortems.actions import CAPARegistry
from app.postmortems.models import CorrectiveAction


def test_capa_registry():
    registry = CAPARegistry()
    action = CorrectiveAction(action_id="ACT-001", description="Fix issue")
    registry.register_corrective(action)
