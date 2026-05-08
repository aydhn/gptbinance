class TelegramTemplates:
    PERFORMANCE_MANIFEST_READY = (
        "Performance Manifest [{manifest_id}] is ready for window {window_class}."
    )
    PERFORMANCE_TRUST_DEGRADED = (
        "🚨 Performance Trust Degraded for [{manifest_id}]: {blockers}"
    )
    BENCHMARK_INTEGRITY_BROKEN = (
        "⚠️ Benchmark Integrity Broken [{benchmark_id}]: {details}"
    )
    ATTRIBUTION_REVIEW_REQUIRED = (
        "🔍 Attribution Review Required for [{tree_id}]: {reasons}"
    )
    PERFORMANCE_EQUIVALENCE_BROKEN = (
        "❌ Performance Equivalence Broken: {divergence_sources}"
    )
    PERFORMANCE_SUMMARY_DIGEST = "📊 Performance Summary: Return {return_val}, Benchmark Relative {relative_val}, Trust: {trust_verdict}"
