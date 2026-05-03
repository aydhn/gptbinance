import psutil
import os
from typing import Dict, List, Optional
from datetime import datetime, timezone
from app.perf.models import (
    ResourceUsageSnapshot,
    CpuProfileSummary,
    MemoryProfileSummary,
    DiskProfileSummary,
    NetworkProfileSummary,
)
from app.perf.base import ResourceSamplerBase


class ProcessResourceSampler(ResourceSamplerBase):
    def __init__(self) -> None:
        self.process = psutil.Process(os.getpid())
        # First call to cpu_percent initializes it
        self.process.cpu_percent()
        net_io = psutil.net_io_counters()
        self._last_net_rx = net_io.bytes_recv if net_io else 0
        self._last_net_tx = net_io.bytes_sent if net_io else 0

    def sample(self) -> ResourceUsageSnapshot:
        # Note: In a real environment, disk I/O per process is OS-dependent.
        # Here we try to get it if available, else 0
        try:
            io_counters = self.process.io_counters()
            disk_read_mb = io_counters.read_bytes / (1024 * 1024)
            disk_write_mb = io_counters.write_bytes / (1024 * 1024)
        except (AttributeError, psutil.AccessDenied):
            disk_read_mb = 0.0
            disk_write_mb = 0.0

        mem_info = self.process.memory_info()
        memory_mb = mem_info.rss / (1024 * 1024)

        net_io = psutil.net_io_counters()
        net_rx = net_io.bytes_recv if net_io else 0
        net_tx = net_io.bytes_sent if net_io else 0

        rx_kb = (net_rx - self._last_net_rx) / 1024
        tx_kb = (net_tx - self._last_net_tx) / 1024

        self._last_net_rx = net_rx
        self._last_net_tx = net_tx

        return ResourceUsageSnapshot(
            cpu_percent=self.process.cpu_percent(),
            memory_mb=memory_mb,
            disk_read_mb=disk_read_mb,
            disk_write_mb=disk_write_mb,
            network_rx_kb=max(0.0, rx_kb),
            network_tx_kb=max(0.0, tx_kb),
        )


class ResourceMonitor:
    def __init__(self, sampler: Optional[ResourceSamplerBase] = None):
        self.sampler = sampler or ProcessResourceSampler()
        self.snapshots: List[ResourceUsageSnapshot] = []

    def start(self) -> None:
        self.snapshots.clear()
        self.sample()

    def sample(self) -> None:
        self.snapshots.append(self.sampler.sample())

    def stop(self) -> None:
        self.sample()

    def get_cpu_summary(self) -> CpuProfileSummary:
        if not self.snapshots:
            return CpuProfileSummary(
                peak_cpu_percent=0.0, avg_cpu_percent=0.0, top_components={}
            )
        cpus = [s.cpu_percent for s in self.snapshots]
        return CpuProfileSummary(
            peak_cpu_percent=max(cpus),
            avg_cpu_percent=sum(cpus) / len(cpus),
            top_components={
                "main_process": sum(cpus) / len(cpus)
            },  # simplistic attribution
        )

    def get_memory_summary(self) -> MemoryProfileSummary:
        if not self.snapshots:
            return MemoryProfileSummary(
                peak_memory_mb=0.0, memory_growth_mb=0.0, leak_suspicion=False
            )
        mems = [s.memory_mb for s in self.snapshots]
        growth = mems[-1] - mems[0]
        # Basic leak suspicion: if growth is positive and significantly large (e.g., > 10MB)
        # Note: Needs to be tuned for realistic workloads
        leak_suspicion = growth > 10.0 and all(
            mems[i] <= mems[i + 1] for i in range(len(mems) - 1)
        )

        return MemoryProfileSummary(
            peak_memory_mb=max(mems),
            memory_growth_mb=growth,
            leak_suspicion=leak_suspicion,
        )

    def get_disk_summary(self) -> DiskProfileSummary:
        if not self.snapshots:
            return DiskProfileSummary(
                total_read_mb=0.0, total_write_mb=0.0, peak_iops=0.0
            )
        # Accumulate deltas if process I/O counters are absolute, but our sample takes snapshot absolute.
        # So we just take the difference between last and first
        read_diff = max(
            0.0, self.snapshots[-1].disk_read_mb - self.snapshots[0].disk_read_mb
        )
        write_diff = max(
            0.0, self.snapshots[-1].disk_write_mb - self.snapshots[0].disk_write_mb
        )
        return DiskProfileSummary(
            total_read_mb=read_diff,
            total_write_mb=write_diff,
            peak_iops=0.0,  # IOPS is hard to measure per-process cross-platform simply
        )

    def get_network_summary(self) -> NetworkProfileSummary:
        if not self.snapshots:
            return NetworkProfileSummary(total_rx_kb=0.0, total_tx_kb=0.0)
        # Our snapshots store incremental delta since last sample for network
        rx = sum(s.network_rx_kb for s in self.snapshots[1:])
        tx = sum(s.network_tx_kb for s in self.snapshots[1:])
        return NetworkProfileSummary(total_rx_kb=rx, total_tx_kb=tx)
