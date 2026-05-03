from typing import List
from app.perf.enums import WorkloadType, HostClass
from app.perf.models import PerfRecommendation


class AdmissionController:
    @staticmethod
    def get_cautions(
        workloads: List[WorkloadType], host_class: HostClass
    ) -> List[PerfRecommendation]:
        recs = []

        has_heavy_analytics = WorkloadType.ANALYTICS_BATCH in workloads
        has_deep_refresh = WorkloadType.GOVERNANCE_REFRESH in workloads
        has_paper = WorkloadType.PAPER_RUNTIME_CYCLE in workloads
        has_testnet = WorkloadType.TESTNET_EXECUTION_SMOKE in workloads

        if host_class == HostClass.LOCAL_MINIMAL:
            if has_paper and has_heavy_analytics:
                recs.append(
                    PerfRecommendation(
                        workload=WorkloadType.ANALYTICS_BATCH,
                        caution_message="Running Analytics Batch with Paper Runtime on LOCAL_MINIMAL may cause execution latency.",
                    )
                )

        if has_testnet and has_deep_refresh:
            recs.append(
                PerfRecommendation(
                    workload=WorkloadType.GOVERNANCE_REFRESH,
                    caution_message="Running Governance Deep Refresh during Testnet Execution Smoke is not recommended due to possible state lock contention.",
                )
            )

        # Add more admission heuristics here based on combinations
        return recs
