from app.release.models import ReleaseBundle, HostProbeReport, MigrationRecord, UpgradePlan, RollbackPlan, InstallPlan
import json
import os

class ReleaseStorage:
    def __init__(self, base_dir="data/release"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def save_bundle(self, bundle: ReleaseBundle):
        pass

    def load_bundle(self, version: str) -> ReleaseBundle:
        return None # Mock

    def save_host_probe(self, report: HostProbeReport):
        pass

    def save_migration_record(self, record: MigrationRecord):
        pass

    def save_upgrade_plan(self, plan: UpgradePlan):
        pass

    def save_rollback_plan(self, plan: RollbackPlan):
        pass

    def save_install_plan(self, plan: InstallPlan):
        pass
