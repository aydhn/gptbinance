import asyncio
import logging
from typing import Dict, Any
from app.resilience.base import BaseFaultInjector
from app.resilience.models import FaultInjectionSpec
from app.resilience.enums import FaultType

logger = logging.getLogger(__name__)


class FaultInjector(BaseFaultInjector):
    def __init__(self):
        self.active_faults: Dict[str, Dict[str, Any]] = {}
        self.tasks: list = []

    async def inject(self, spec: FaultInjectionSpec, run_id: str) -> None:
        fault_key = f"{run_id}_{spec.target.component.value}_{spec.fault_type.value}"
        logger.warning(
            f"[RESILIENCE] Injecting fault: {spec.fault_type.value} on {spec.target.component.value} for {spec.duration_ms}ms (Run: {run_id})"
        )

        self.active_faults[fault_key] = {"spec": spec, "status": "active"}

        # Simulate fault injection mechanism
        if spec.fault_type == FaultType.LATENCY_INJECTION:
            pass  # Hook into real latency injector
        elif spec.fault_type == FaultType.STALE_DATA_INJECTION:
            pass  # Hook into data stream to hold updates

        task = asyncio.create_task(self._auto_cleanup(spec, run_id, fault_key))
        self.tasks.append(task)

    async def _auto_cleanup(
        self, spec: FaultInjectionSpec, run_id: str, fault_key: str
    ):
        try:
            await asyncio.sleep(spec.duration_ms / 1000.0)
            if fault_key in self.active_faults:
                await self.cleanup(spec, run_id)
        except asyncio.CancelledError:
            pass

    async def cleanup(self, spec: FaultInjectionSpec, run_id: str) -> None:
        fault_key = f"{run_id}_{spec.target.component.value}_{spec.fault_type.value}"
        if fault_key in self.active_faults:
            logger.info(
                f"[RESILIENCE] Cleaning up fault: {spec.fault_type.value} on {spec.target.component.value} (Run: {run_id})"
            )
            del self.active_faults[fault_key]
            # Simulate real cleanup

    async def close(self):
        for task in self.tasks:
            task.cancel()
        if self.tasks:
            await asyncio.gather(*self.tasks, return_exceptions=True)
