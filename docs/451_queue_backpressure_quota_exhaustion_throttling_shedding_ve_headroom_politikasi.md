# Queue, Backpressure, Quota Exhaustion, Throttling, Shedding, and Headroom Policy

## Queue Growth & Backpressure
Queue growth isn't just a metric; it's a symptom of a downstream bottleneck or an upstream flood. The capacity plane tracks oldest message age, consumer lag, and growth rate. Backpressure signals must propagate to throttling/shedding mechanisms.

## Quota Exhaustion
Reaching an external vendor limit or exchange rate limit triggers `EXHAUSTED` severity. This is treated as a hard ceiling. No autoscaling will fix this.

## Throttling and Shedding
* **Graceful vs Hard Block**: Throttling attempts to slow down traffic. Hard block rejects it.
* **Shedding**: Dropping requests entirely. Shedding must happen based on priority (drop `BEST_EFFORT` before `CRITICAL`).
* **Headroom Discipline**: We mandate maintaining a buffer (headroom). Operating near the edge continuously creates "capacity debt" and results in a `CAUTION` or `DEGRADED` trust verdict. Silent starvation is prohibited.
