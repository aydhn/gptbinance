# Benchmark ve Validation Mimarisi

Bir backtest sonucu tek başına anlamsızdır. Aynı veri üzerinde basit referans modellerle (baseline), daha az karmaşık varyantlarla (ablation) ve temel dürüstlük kontrolleriyle (honesty guards) kıyaslanmadan hiçbir strateji canlıya alınmamalıdır.

Bu katman, stratejinin ciddiyetini test eden ayrı ve güvenilir bir validation katmanı sunar.
