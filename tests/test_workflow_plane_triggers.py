from app.workflow_plane.triggers import TriggerRegistry
from app.workflow_plane.models import TriggerDefinition
from app.workflow_plane.enums import TriggerClass

def test_trigger_registry():
    reg = TriggerRegistry()
    td = TriggerDefinition(trigger_class=TriggerClass.SCHEDULE, description="t")
    reg.register(td)
    assert reg._triggers[TriggerClass.SCHEDULE].description == "t"
