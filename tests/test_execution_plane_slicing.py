from app.execution_plane.slicing import SlicingEngine

def test_slicing_engine():
    plan = SlicingEngine.generate_plan(total_qty=100.0, min_notional=10.0, price=1.0)
    assert plan is not None
    assert plan.slice_count == 3

    plan2 = SlicingEngine.generate_plan(total_qty=15.0, min_notional=10.0, price=1.0)
    assert plan2 is None
