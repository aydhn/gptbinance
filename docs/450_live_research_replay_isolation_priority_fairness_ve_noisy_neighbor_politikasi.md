# Live vs Research vs Replay Isolation, Priority, Fairness, and Noisy Neighbor Policy

This policy dictates how different workloads interact when sharing or attempting to share resources.

## Workload Isolation
* **Live Trading**: Must be strictly isolated. Dedicated queue lanes, dedicated CPU/GPU pools where possible.
* **Research & Replay**: Best-effort or scheduled reservations. Cannot preempt live trading under any circumstance.
* **Shared Resources**: Where isolation is impossible (e.g., a specific vendor API endpoint), strict rate-limiting and shedding policies apply to non-live workloads.

## Priority Classes
* `EMERGENCY_OVERRIDE`: Break-glass actions.
* `CRITICAL`: Live trading path.
* `HIGH`, `NORMAL`, `BEST_EFFORT`, `BACKGROUND`.

## Fairness and Noisy Neighbors
* **Fairness**: A workload dominating a shared resource and starving others will be flagged.
* **Noisy Neighbors**: Burst collisions and cross-workload interference are tracked. If a research job spikes and causes latency in a seemingly isolated live path (due to hypervisor or network switch saturation), this is recorded as a divergence/quality breach and lowers Capacity Trust.
* **No Hidden Priority Override**: A user cannot simply tag a batch job as "CRITICAL" to bypass shedding.
