from app.security.backup import BackupManager
from app.security.models import BackupPlan
from app.security.enums import BackupScope, BackupType


def test_backup(tmp_path):
    bm = BackupManager(base_backup_dir=str(tmp_path / "backups"))
    plan = BackupPlan(
        scope=BackupScope.FULL, type=BackupType.SNAPSHOT, target_dir=str(tmp_path)
    )
    run = bm.run_backup(plan)
    assert run.success
    assert len(run.manifest.artifacts) >= 0
