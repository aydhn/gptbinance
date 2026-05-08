# Performance Equivalence, Benchmark Integrity ve Cohort Analysis Politikası

## Equivalence (Replay vs Live)
Aynı sinyal, replay, paper, runtime ve live ortamlarda *aynı* PnL'yi üretiyor mu?
EquivalenceChecker: İki PerformanceManifest alır, hash ve window check yapar. Divergence (örn. minor divergence, material divergence, not comparable) raporu döner.

## Benchmark Integrity
Benchmark'ların güncel kalması (freshness_ttl) ve hedeflenen sembol/baz para birimi ile uygunluğu (comparability_requirements) sürekli kontrol edilir. Stale veya mismatch durumlarında Trust Verdict düşer.

## Cohort Analysis
Sembol, Sleeve, Strategy, Model veya Regime bazında katkılar.
Kural: Yanlış scope'ta toplama (aggregation) yapılamaz. Sembol PnL'si stratejiden bağımsız olarak değerlendirilemez.

## Trust Verdict
- TRUSTED
- CAUTION
- DEGRADED
- BLOCKED
- REVIEW_REQUIRED
Bu verdict, readiness board veya evidence court tarafından kullanılabilir.
