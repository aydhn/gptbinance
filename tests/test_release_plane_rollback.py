import pytest
from app.release_plane.rollback import RollbackManager
from app.release_plane.exceptions import RollbackViolation

def test_rollback_package_creation():
    manager = RollbackManager()
    pkg = manager.create_package("rel-1", ["entry-1"], ["dependency-1"])
    assert pkg.target_release_ref.release_id == "rel-1"

def test_fake_rollback_rejection():
    manager = RollbackManager()
    with pytest.raises(RollbackViolation):
         manager.create_package("rel-1", [], [])

def test_rollback_execution():
    manager = RollbackManager()
    pkg = manager.create_package("rel-1", ["entry-1"], [])
    exec_rec = manager.execute_rollback(pkg.package_id)
    assert exec_rec.package_id == pkg.package_id
