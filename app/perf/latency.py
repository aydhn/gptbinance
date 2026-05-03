import time
import statistics
from typing import Dict, List, Optional, ContextManager
from contextlib import contextmanager
from app.perf.models import ComponentLatencySummary


class LatencyTracker:
    def __init__(self) -> None:
        self.measurements: Dict[str, List[float]] = {}

    def record(self, component_name: str, duration_ms: float) -> None:
        if component_name not in self.measurements:
            self.measurements[component_name] = []
        self.measurements[component_name].append(duration_ms)

    @contextmanager
    def measure(self, component_name: str):
        start = time.perf_counter()
        try:
            yield
        finally:
            end = time.perf_counter()
            duration_ms = (end - start) * 1000.0
            self.record(component_name, duration_ms)

    def get_summaries(self) -> List[ComponentLatencySummary]:
        summaries = []
        for comp, times in self.measurements.items():
            if not times:
                continue
            times_sorted = sorted(times)
            n = len(times_sorted)
            p50 = statistics.median(times_sorted)
            p95 = times_sorted[int(n * 0.95)] if n > 0 else 0.0
            p99 = times_sorted[int(n * 0.99)] if n > 0 else 0.0
            max_ms = times_sorted[-1]
            summaries.append(
                ComponentLatencySummary(
                    component_name=comp,
                    p50_ms=p50,
                    p95_ms=p95,
                    p99_ms=p99,
                    max_ms=max_ms,
                    call_count=n,
                )
            )
        return summaries
