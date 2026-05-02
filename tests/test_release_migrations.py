import pytest
from app.release.migrations import MigrationExecutor
from app.release.enums import MigrationDirection

def test_migration_execution():
    executor = MigrationExecutor()
    plan = executor.create_plan("v1", "v2", MigrationDirection.UPGRADE)
    res = executor.execute(plan)
    assert len(res) == 1
    assert res[0].success == True
