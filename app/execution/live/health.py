from app.execution.live.models import ExecutionHealthSnapshot
from app.execution.live.enums import ExecutionHealthStatus
from datetime import datetime
from typing import Dict, Any
from app.observability.metrics import registry as metric_registry
from app.observability.enums import ComponentType


class ExecutionHealthMonitor:
    def __init__(self):
        self.reject_count = 0
        self.drift_count = 0
        self.rest_latency_ms = 0.0
        self.stream_freshness_seconds = 0.0
        self.safety_gate_status = {"mainnet_armed": False}

    def record_reject(self):
        self.reject_count += 1
        try:
            metric_registry.record("live_execution_rejects", 1.0, tags={"type": "reject"})
        except Exception:
            pass

    def record_drift(self):
        self.drift_count += 1
        try:
            metric_registry.record("live_execution_drift", 1.0, tags={"type": "drift"})
        except Exception:
            pass

    def update_rest_latency(self, latency_ms: float):
        self.rest_latency_ms = latency_ms

    def update_stream_freshness(self, seconds: float):
        self.stream_freshness_seconds = seconds

    def update_gate_status(self, gate_name: str, status: bool):
        self.safety_gate_status[gate_name] = status

    def get_snapshot(self, open_orders_count: int) -> ExecutionHealthSnapshot:
        status = ExecutionHealthStatus.HEALTHY
        if (
            self.reject_count > 5
            or self.drift_count > 0
            or self.stream_freshness_seconds > 60
        ):
            status = ExecutionHealthStatus.DEGRADED

        return ExecutionHealthSnapshot(
            timestamp=datetime.utcnow(),
            status=status,
            rest_latency_ms=self.rest_latency_ms,
            stream_freshness_seconds=self.stream_freshness_seconds,
            reject_count=self.reject_count,
            drift_count=self.drift_count,
            open_orders_count=open_orders_count,
            safety_gate_status=self.safety_gate_status,
        )
