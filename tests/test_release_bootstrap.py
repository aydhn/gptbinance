import pytest
from app.release.bootstrap import Bootstrapper
from app.release.models import InstallPlan
from app.release.enums import InstallVerdict
from app.release.manifest import ManifestGenerator
from app.release.host_probe import HostProbe

def test_bootstrap():
    b = Bootstrapper()
    plan = InstallPlan(
        target_release=ManifestGenerator().create_manifest(),
        host_probe=HostProbe().run_probe(),
        verdict=InstallVerdict.PASS,
        warnings=[]
    )
    res = b.bootstrap(plan)
    assert res.success == True
