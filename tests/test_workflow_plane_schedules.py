from app.workflow_plane.schedules import ScheduleRegistry
from app.workflow_plane.models import ScheduleDefinition
from app.workflow_plane.enums import ScheduleClass

def test_schedule_registry():
    reg = ScheduleRegistry()
    sd = ScheduleDefinition(schedule_id="s1", schedule_class=ScheduleClass.ROLLING, cadence="1m", description="t")
    reg.register(sd)
    assert reg._schedules["s1"].cadence == "1m"
