from app.autonomy_plane.quality import quality_evaluator
from app.autonomy_plane.models import AutonomyObject
from app.autonomy_plane.enums import AutonomyClass

def test_quality_evaluation():
    obj = AutonomyObject(
        autonomy_id="test_id",
        agent_id="test_agent",
        autonomy_class=AutonomyClass.BOUNDED,
        owner="test_owner"
    )
    warnings = quality_evaluator.evaluate(obj)
    assert "Stale delegation warning" in warnings
    assert "Self-approval warning" in warnings
