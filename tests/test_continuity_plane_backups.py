import pytest
from app.continuity_plane.backups import BackupManager
from app.continuity_plane.models import BackupPolicy
from app.continuity_plane.enums import BackupClass
from app.continuity_plane.exceptions import InvalidBackupPolicy

def test_backup_manager():
    manager = BackupManager()
    policy = BackupPolicy(
        policy_id="pol_1",
        service_id="srv_1",
        backup_class=BackupClass.FULL,
        frequency_seconds=86400,
        retention_days=30,
        is_encrypted=True,
        requires_verification=True
    )
    manager.register_policy(policy)

    retrieved = manager.get_policy("pol_1")
    assert retrieved is not None
    assert retrieved.policy_id == "pol_1"

def test_backup_manager_invalid():
    manager = BackupManager()
    with pytest.raises(InvalidBackupPolicy):
        policy = BackupPolicy(
            policy_id="",
            service_id="srv_1",
            backup_class=BackupClass.FULL,
            frequency_seconds=86400,
            retention_days=30,
            is_encrypted=True,
            requires_verification=True
        )
        manager.register_policy(policy)
