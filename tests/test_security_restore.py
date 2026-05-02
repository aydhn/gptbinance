from app.security.restore import RestoreManager
from app.security.models import RestorePlan
from app.security.enums import RestoreVerdict

def test_restore_dry_run():
    rm = RestoreManager()
    plan = RestorePlan(source_manifest_path="dummy.json", target_dir="dummy", dry_run=True)
    res = rm.run_restore(plan)
    # Manifest not found
    assert res.verdict == RestoreVerdict.UNSAFE
