# Phase 18: Korelasyon, Overlap ve Crowded Book Politikası

Farklı fırsatlar (intents) çoğu zaman birbiriyle yüksek korelasyonlu ürünlerden veya benzer tezlerden gelebilir. (örn. ETHUSDT ile SOLUSDT).

## Correlation Clustering
PortfolioEngine, semboller arası basit korelasyon hesapları (veya mock cluster'lar) ile yüksek korelasyonlu grupları tespit eder.
- Bu cluster'lara atanan max_weight (`max_correlated_cluster_weight`) aşıldığında yeni alımlar engellenir.

## Overlap Tespiti
Birbirini tekrar eden fırsatlar (aynı yönde pozisyon büyütme veya aşırı korele sembollerde aynı yöne gitme) Overlap modülü tarafından "OverlapSeverity" skoruyla işaretlenir.
- Yüksek Overlap = Yüksek Ceza (Penalty).
- Ranking sistemi bu cezaları fırsatın puanından düşerek önceliğini düşürür.
