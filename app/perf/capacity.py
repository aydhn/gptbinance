from typing import List, Dict
from app.perf.models import CapacityReport
from app.perf.enums import HostClass, WorkloadType
from app.perf.host_classes import HostClassRegistry


class CapacityAnalyzer:
    @staticmethod
    def evaluate(
        host_class: HostClass, active_workloads: List[WorkloadType]
    ) -> CapacityReport:
        hc_def = HostClassRegistry.get(host_class)

        cautions = []
        unsupported = []

        # Simple heuristics for workload overlaps
        has_heavy_batch = (
            WorkloadType.ANALYTICS_BATCH in active_workloads
            or WorkloadType.ML_INFERENCE_BATCH in active_workloads
        )
        has_live = (
            WorkloadType.TESTNET_EXECUTION_SMOKE in active_workloads
            or "live" in active_workloads
        )  # simplistic check

        if hc_def.expected_cores <= 4 and has_heavy_batch and has_live:
            cautions.append(
                "Running heavy batch workloads alongside execution workloads on a low-core machine risks latency jitter."
            )

        if hc_def.host_class == HostClass.LOCAL_MINIMAL and len(active_workloads) > 2:
            unsupported.append(
                "LOCAL_MINIMAL does not support more than 2 concurrent workloads safely."
            )

        headroom = 100.0
        # Estimate headroom (very rough proxy)
        headroom -= len(active_workloads) * 15.0
        if has_heavy_batch:
            headroom -= 30.0

        headroom = max(0.0, min(100.0, headroom))

        return CapacityReport(
            host_class=host_class,
            available_headroom_percent=headroom,
            concurrency_cautions=cautions,
            reserve_capacity_recommendation="Maintain at least 20% CPU and 1GB RAM reserve for OS spikes.",
            unsupported_combinations=unsupported,
        )
