import asyncio
import logging
from typing import Dict, Any
from app.resilience.base import BaseStressGenerator
from app.resilience.models import StressSpec

logger = logging.getLogger(__name__)


class StressGenerator(BaseStressGenerator):
    def __init__(self):
        self.active_stress: Dict[str, Dict[str, Any]] = {}
        self.tasks: list = []

    async def apply_stress(self, spec: StressSpec, run_id: str) -> None:
        stress_key = f"{run_id}_{spec.target.component.value}_{spec.stress_type.value}"
        logger.warning(
            f"[RESILIENCE] Applying stress: {spec.stress_type.value} on {spec.target.component.value} for {spec.duration_ms}ms (Run: {run_id})"
        )

        self.active_stress[stress_key] = {"spec": spec, "status": "active"}

        task = asyncio.create_task(self._auto_cleanup(spec, run_id, stress_key))
        self.tasks.append(task)

    async def _auto_cleanup(self, spec: StressSpec, run_id: str, stress_key: str):
        try:
            await asyncio.sleep(spec.duration_ms / 1000.0)
            if stress_key in self.active_stress:
                await self.remove_stress(spec, run_id)
        except asyncio.CancelledError:
            pass

    async def remove_stress(self, spec: StressSpec, run_id: str) -> None:
        stress_key = f"{run_id}_{spec.target.component.value}_{spec.stress_type.value}"
        if stress_key in self.active_stress:
            logger.info(
                f"[RESILIENCE] Removing stress: {spec.stress_type.value} on {spec.target.component.value} (Run: {run_id})"
            )
            del self.active_stress[stress_key]

    async def close(self):
        for task in self.tasks:
            task.cancel()
        if self.tasks:
            await asyncio.gather(*self.tasks, return_exceptions=True)
