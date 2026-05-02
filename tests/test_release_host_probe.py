import pytest
from app.release.host_probe import HostProbe

def test_run_probe():
    probe = HostProbe()
    res = probe.run_probe()
    assert res.python_version_ok == True
