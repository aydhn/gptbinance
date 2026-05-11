import pytest
from app.migration_plane.dry_runs import DryRunManager

def test_execute_dry_run():
    manager = DryRunManager()
    result = manager.execute_dry_run("mig_001")
    assert result.is_successful is True
    assert result.fidelity_class == "HIGH"
