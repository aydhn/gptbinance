from app.perf.host_classes import HostClassRegistry
from app.perf.enums import HostClass


def test_host_class_registry():
    hc = HostClassRegistry.get(HostClass.LOCAL_AVERAGE)
    assert hc.expected_cores == 4
    assert "live" in hc.caution_modes
