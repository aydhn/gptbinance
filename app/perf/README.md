# Performance and Capacity Engineering

This module provides a local-first, zero-budget, and deterministic framework for evaluating the performance and capacity of the trading platform.

## Key Principles
- **No Auto-Tuning**: The framework provides visibility, budgets, and cautions. It does not magically alter runtime configurations to "speed things up".
- **Workload Based**: Performance is meaningless without context. Measurements are tied to specific workload profiles (e.g., `PAPER_RUNTIME_CYCLE`, `ANALYTICS_BATCH`).
- **Host Classes**: Defines target deployment topologies (e.g., `LOCAL_AVERAGE`) to evaluate if the current workloads can run safely without starving resources.
- **Budgets and Bottlenecks**: Explicit resource and latency budgets define the operating envelope. Breaches trigger clear evidence-backed bottleneck hypotheses.
- **Regression Tracking**: Compares current runs against baselines to catch performance degradation locally before a release.

## CLI Usage (Examples)
- `python -m app.main --run-perf-profile --perf-workload PAPER_RUNTIME_CYCLE --perf-host-class LOCAL_AVERAGE`
- `python -m app.main --show-perf-summary --run-id <run_id>`
- `python -m app.main --show-bottleneck-report --run-id <run_id>`
- `python -m app.main --run-perf-regression-check --baseline-run <run_id_1> --target-run <run_id_2>`
- `python -m app.main --show-capacity-report --run-id <run_id>`
