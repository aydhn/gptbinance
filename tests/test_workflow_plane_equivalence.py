from app.workflow_plane.equivalence import EquivalenceEvaluator
from app.workflow_plane.models import RunWindow
from app.workflow_plane.enums import WindowClass, EquivalenceVerdict
from datetime import datetime, timezone

def test_equivalence_evaluation():
    evaluator = EquivalenceEvaluator()
    win = RunWindow(window_id="test", start_time=datetime.now(timezone.utc), end_time=datetime.now(timezone.utc), as_of_cut=datetime.now(timezone.utc), window_class=WindowClass.ROLLING)
    report = evaluator.evaluate("wf-1", win, ["live", "paper"])
    assert report.verdict == EquivalenceVerdict.EQUIVALENT
