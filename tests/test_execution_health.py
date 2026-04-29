from app.execution.live.health import ExecutionHealthMonitor
from app.execution.live.enums import ExecutionHealthStatus


def test_execution_health_monitor():
    monitor = ExecutionHealthMonitor()
    snap1 = monitor.get_snapshot(1)
    assert snap1.status == ExecutionHealthStatus.HEALTHY

    for _ in range(6):
        monitor.record_reject()

    snap2 = monitor.get_snapshot(1)
    assert snap2.status == ExecutionHealthStatus.DEGRADED
