from app.perf.resources import ResourceMonitor, ProcessResourceSampler
from app.perf.models import ResourceUsageSnapshot


class FakeSampler(ProcessResourceSampler):
    def __init__(self):
        pass

    def sample(self):
        return ResourceUsageSnapshot(
            cpu_percent=10.0,
            memory_mb=50.0,
            disk_read_mb=5.0,
            disk_write_mb=10.0,
            network_rx_kb=100.0,
            network_tx_kb=200.0,
        )


def test_resource_monitor():
    monitor = ResourceMonitor(sampler=FakeSampler())
    monitor.start()
    monitor.sample()
    monitor.stop()
    cpu = monitor.get_cpu_summary()
    assert cpu.peak_cpu_percent == 10.0
    mem = monitor.get_memory_summary()
    assert mem.peak_memory_mb == 50.0
