import pytest
from app.release.rollback import RollbackPlanner
from app.release.manifest import ManifestGenerator


def test_rollback_planner():
    planner = RollbackPlanner()
    plan = planner.create_plan(ManifestGenerator().create_manifest())
    assert plan.verdict is not None
    res = planner.run_dry_run(plan)
    assert res.success == True
