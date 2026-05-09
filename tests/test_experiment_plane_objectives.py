from app.experiment_plane.objectives import build_outperform_objective, build_reduce_drag_objective
from app.experiment_plane.enums import ObjectiveClass

def test_objectives_builder():
    obj1 = build_outperform_objective("return")
    assert obj1.objective_class == ObjectiveClass.OUTPERFORM_BASELINE
    assert "return" in obj1.target_metrics

    obj2 = build_reduce_drag_objective()
    assert obj2.objective_class == ObjectiveClass.REDUCE_EXECUTION_DRAG
    assert "slippage" in obj2.target_metrics
