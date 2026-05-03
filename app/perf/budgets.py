from typing import List, Dict, Optional
from app.perf.enums import ResourceType, BudgetSeverity, LatencyPercentile
from app.perf.models import ResourceBudget, LatencyBudget, PerfRun


class BudgetRegistry:
    _resource_budgets: List[ResourceBudget] = []
    _latency_budgets: List[LatencyBudget] = []

    @classmethod
    def add_resource_budget(cls, budget: ResourceBudget) -> None:
        cls._resource_budgets.append(budget)

    @classmethod
    def add_latency_budget(cls, budget: LatencyBudget) -> None:
        cls._latency_budgets.append(budget)

    @classmethod
    def get_applicable_resource_budgets(cls, mode: str) -> List[ResourceBudget]:
        return [b for b in cls._resource_budgets if mode in b.applicable_modes]

    @classmethod
    def get_applicable_latency_budgets(cls, mode: str) -> List[LatencyBudget]:
        return [b for b in cls._latency_budgets if mode in b.applicable_modes]

    @classmethod
    def evaluate(cls, run: PerfRun, mode: str) -> List[Dict[str, str]]:
        breaches = []
        r_budgets = cls.get_applicable_resource_budgets(mode)
        l_budgets = cls.get_applicable_latency_budgets(mode)

        for rb in r_budgets:
            actual = 0.0
            if rb.resource_type == ResourceType.CPU:
                actual = run.cpu_summary.peak_cpu_percent
            elif rb.resource_type == ResourceType.MEMORY:
                actual = run.memory_summary.peak_memory_mb
            elif rb.resource_type == ResourceType.DISK_IO:
                actual = run.disk_summary.total_write_mb  # simplifying to write
            elif rb.resource_type == ResourceType.NETWORK:
                actual = run.network_summary.total_tx_kb  # simplifying to tx

            if actual > rb.limit_value:
                breaches.append(
                    {
                        "type": "RESOURCE",
                        "resource": rb.resource_type.value,
                        "severity": rb.severity.value,
                        "limit": str(rb.limit_value),
                        "actual": str(actual),
                    }
                )

        for lb in l_budgets:
            for lat in run.latencies:
                if lat.component_name == lb.component_name:
                    actual = 0.0
                    if lb.percentile == LatencyPercentile.P50:
                        actual = lat.p50_ms
                    elif lb.percentile == LatencyPercentile.P95:
                        actual = lat.p95_ms
                    elif lb.percentile == LatencyPercentile.P99:
                        actual = lat.p99_ms
                    elif lb.percentile == LatencyPercentile.MAX:
                        actual = lat.max_ms

                    if actual > lb.limit_ms:
                        breaches.append(
                            {
                                "type": "LATENCY",
                                "component": lb.component_name,
                                "percentile": lb.percentile.value,
                                "severity": lb.severity.value,
                                "limit": str(lb.limit_ms),
                                "actual": str(actual),
                            }
                        )

        return breaches


# Register some sensible default budgets
BudgetRegistry.add_resource_budget(
    ResourceBudget(
        resource_type=ResourceType.MEMORY,
        severity=BudgetSeverity.SOFT,
        limit_value=512.0,  # 512MB
        applicable_modes=["paper", "testnet"],
    )
)

BudgetRegistry.add_resource_budget(
    ResourceBudget(
        resource_type=ResourceType.MEMORY,
        severity=BudgetSeverity.HARD,
        limit_value=1024.0,  # 1GB
        applicable_modes=["paper", "testnet", "live"],
    )
)

BudgetRegistry.add_latency_budget(
    LatencyBudget(
        component_name="PaperExchange",
        percentile=LatencyPercentile.P95,
        severity=BudgetSeverity.SOFT,
        limit_ms=50.0,
        applicable_modes=["paper"],
    )
)
