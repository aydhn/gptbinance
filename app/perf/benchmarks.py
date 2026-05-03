import time
from typing import Callable, Any
from app.perf.models import WorkloadResult
from app.perf.base import BenchmarkRunnerBase


class DeterministicBenchmarkRunner(BenchmarkRunnerBase):
    def run(
        self,
        workload_name: str,
        iterations: int = 3,
        func: Callable[..., Any] = lambda: None,
    ) -> WorkloadResult:
        # Simple runner that repeats a function
        durations = []

        # Warmup
        try:
            func()
        except Exception:
            pass

        for i in range(iterations):
            start = time.perf_counter()
            try:
                func()
                end = time.perf_counter()
                durations.append(end - start)
            except Exception as e:
                return WorkloadResult(
                    run_id=f"bench_{workload_name}_{int(time.time())}",
                    success=False,
                    data={"error": str(e), "iteration": i},
                )

        if durations:
            avg_duration = sum(durations) / len(durations)
        else:
            avg_duration = 0.0

        return WorkloadResult(
            run_id=f"bench_{workload_name}_{int(time.time())}",
            success=True,
            data={
                "iterations": iterations,
                "durations": durations,
                "avg_duration": avg_duration,
            },
        )
