import os
import shutil
import uuid
from typing import List
from datetime import datetime, timezone
from app.security.models import BackupPlan, BackupRun, BackupManifest, BackupArtifact
from app.security.enums import BackupScope, BackupType
from app.security.integrity import IntegrityChecker

class BackupManager:
    def __init__(self, base_backup_dir: str = "data/backups"):
        self.base_backup_dir = base_backup_dir
        self.integrity_checker = IntegrityChecker()

    def run_backup(self, plan: BackupPlan) -> BackupRun:
        run_id = f"backup_{datetime.now().strftime('%Y%md_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        target_dir = os.path.join(self.base_backup_dir, run_id)
        os.makedirs(target_dir, exist_ok=True)

        artifacts: List[BackupArtifact] = []

        # Simple implementation: copy data/config

        src_dirs = ["config"]
        if plan.scope in [BackupScope.FULL, BackupScope.STATE_ONLY]:
            src_dirs.append("data")

        for d in src_dirs:
            if os.path.exists(d):
                dst = os.path.join(target_dir, d)
                if d == "data":
                    # Manually copy to avoid copying 'data/backups'
                    os.makedirs(dst, exist_ok=True)
                    for item in os.listdir(d):
                        if item == "backups":
                            continue
                        s = os.path.join(d, item)
                        d_dest = os.path.join(dst, item)
                        if os.path.isdir(s):
                            shutil.copytree(s, d_dest, dirs_exist_ok=True)
                        else:
                            shutil.copy2(s, d_dest)
                else:
                    shutil.copytree(d, dst, dirs_exist_ok=True)


        manifest_data = self.integrity_checker.generate_manifest(target_dir)
        for path, file_hash in manifest_data.items():
            size = os.path.getsize(path)
            artifacts.append(BackupArtifact(path=os.path.relpath(path, target_dir), size_bytes=size, hash_sha256=file_hash))

        manifest = BackupManifest(run_id=run_id, scope=plan.scope, artifacts=artifacts)

        with open(os.path.join(target_dir, "manifest.json"), "w") as f:
            f.write(manifest.model_dump_json(indent=2))

        return BackupRun(manifest=manifest, success=True)
