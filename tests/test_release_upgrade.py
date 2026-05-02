import pytest
from app.release.upgrade import UpgradePlanner
from app.release.manifest import ManifestGenerator

def test_upgrade_planner():
    planner = UpgradePlanner()
    plan = planner.create_plan(ManifestGenerator().create_manifest())
    assert plan.verdict is not None
    res = planner.run_dry_run(plan)
    assert res.success == True
