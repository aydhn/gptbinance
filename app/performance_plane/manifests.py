def generate_performance_manifest(perf_id: str):
    return {
        "perf_id": perf_id,
        "benchmark_relative_realized_value_ref": "br_val_1",
        "status": "business_utility_proven" # Better metrics without utility gives caution
    }
