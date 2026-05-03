from typing import Dict, Optional
from app.perf.enums import WorkloadType, ProfileScope
from app.perf.models import WorkloadDefinition
from app.perf.exceptions import InvalidWorkloadDefinitionError


class WorkloadRegistry:
    _workloads: Dict[WorkloadType, WorkloadDefinition] = {}

    @classmethod
    def register(cls, workload: WorkloadDefinition) -> None:
        if workload.workload_type in cls._workloads:
            raise InvalidWorkloadDefinitionError(
                f"Workload {workload.workload_type} is already registered."
            )
        cls._workloads[workload.workload_type] = workload

    @classmethod
    def get(cls, workload_type: WorkloadType) -> Optional[WorkloadDefinition]:
        return cls._workloads.get(workload_type)

    @classmethod
    def get_all(cls) -> Dict[WorkloadType, WorkloadDefinition]:
        return cls._workloads.copy()


# Built-in workload definitions
_builtin_workloads = [
    WorkloadDefinition(
        workload_type=WorkloadType.FEATURE_BUILD,
        target_components=["FeatureEngine", "DataProvider"],
        expected_inputs={"symbols": ["BTCUSDT", "ETHUSDT"], "timeframes": ["1m", "5m"]},
        measurement_scope=ProfileScope.WORKFLOW,
        representative_concurrency=1,
        safe_modes=["dev", "paper", "testnet", "live"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.GOVERNANCE_REFRESH,
        target_components=["GovernanceManager", "PolicyStore"],
        expected_inputs={"deep_refresh": True},
        measurement_scope=ProfileScope.WORKFLOW,
        representative_concurrency=1,
        safe_modes=["dev", "paper", "testnet"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.ANALYTICS_BATCH,
        target_components=["AnalyticsEngine", "DataStore"],
        expected_inputs={"batch_size": 1000, "historical_days": 7},
        measurement_scope=ProfileScope.WORKFLOW,
        representative_concurrency=2,
        safe_modes=["dev", "paper"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.STRATEGY_EVAL,
        target_components=["StrategyEvaluator", "SignalGenerator"],
        expected_inputs={"active_strategies": 5, "features": 20},
        measurement_scope=ProfileScope.COMPONENT,
        representative_concurrency=4,
        safe_modes=["dev", "paper", "testnet", "live"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.REGIME_EVAL,
        target_components=["RegimeDetector", "MarketData"],
        expected_inputs={"lookback_windows": [14, 28, 60]},
        measurement_scope=ProfileScope.COMPONENT,
        representative_concurrency=1,
        safe_modes=["dev", "paper", "testnet", "live"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.RISK_PORTFOLIO,
        target_components=["RiskManager", "PortfolioOptimizer"],
        expected_inputs={"positions": 10, "exposure_limit": 1000},
        measurement_scope=ProfileScope.COMPONENT,
        representative_concurrency=1,
        safe_modes=["dev", "paper", "testnet", "live"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.ML_INFERENCE_BATCH,
        target_components=["MLEngine", "ModelRegistry"],
        expected_inputs={"batch_size": 500, "models": ["rf_v1", "gbdt_v2"]},
        measurement_scope=ProfileScope.WORKFLOW,
        representative_concurrency=1,
        safe_modes=["dev", "paper", "testnet"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.PAPER_RUNTIME_CYCLE,
        target_components=["RuntimeOrchestrator", "PaperExchange"],
        expected_inputs={"ticks_per_cycle": 100},
        measurement_scope=ProfileScope.END_TO_END,
        representative_concurrency=1,
        safe_modes=["dev", "paper"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.TESTNET_EXECUTION_SMOKE,
        target_components=["ExecutionGateway", "TestnetClient"],
        expected_inputs={"orders": 5, "type": "LIMIT"},
        measurement_scope=ProfileScope.END_TO_END,
        representative_concurrency=1,
        safe_modes=["testnet"],
    ),
    WorkloadDefinition(
        workload_type=WorkloadType.RELEASE_VERIFY,
        target_components=["ReleaseManager", "SmokeTester"],
        expected_inputs={"full_suite": True},
        measurement_scope=ProfileScope.END_TO_END,
        representative_concurrency=1,
        safe_modes=["dev", "paper"],
    ),
]

for w in _builtin_workloads:
    WorkloadRegistry.register(w)
