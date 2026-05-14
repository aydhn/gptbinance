# Capacity Plane and Resource/Quota/Rate-Limit Governance Architecture

The Capacity Plane governs the reality of "Capacity Truth" across the trading platform. It establishes a canonical registry for resources, quotas, reservations, allocations, usage, and saturation.

## Flow of Capacity Truth
1. **Resources**: Compute (CPU/GPU), Storage (IOPS/Bytes), Network Bandwidth, Queues, Concurrency slots, External Quotas, Exchange Rate Limits.
2. **Quotas & Reservations**: Hard/Soft limits and guarantees on resource usage. Reservation implies a verified claim; it doesn't guarantee immediate access if underlying saturation occurs without isolation.
3. **Allocations & Usage**: Actual mapped usage to actors and workloads. Usage != Reservation. You can reserve without using, and use without reserving (best-effort).
4. **Saturation & Backpressure**: When demand exceeds supply. This isn't just an alert; it's a governance signal. Backpressure implies queue growth or consumer lag.
5. **Throttling & Shedding**: Direct response to saturation. Shedding drops load based on priority. Throttling slows it down.
6. **Trust Verdict**: Derived from hygiene of the above. Are we hiding starvation? Are we doing autoscaling theater (where scaling compute doesn't help because the bottleneck is a vendor quota)?

## Core Principles
* **Usage != Reservation != Saturation**: Having a reservation doesn't mean you're using it. High usage doesn't always mean saturation (if burstable).
* **No Autoscaling Theater**: Don't scale horizontally if the bottleneck is an external API quota. The capacity plane maps the true constraints.
* **Strict Governance**: Capacity isn't a free-for-all. Live trading has strict priority over research or backfill tasks.
