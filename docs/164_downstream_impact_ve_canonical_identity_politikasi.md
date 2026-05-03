# Downstream Impact ve Canonical Identity Politikası

## Downstream Impact
Bir dataset veya şema bozulduğunda ML models, backtests ve runtime snapshot'lar etkilenir. ImpactAnalyzer ile risk severity hesaplanır.

## Canonical Entity Mapping
- BTCUSDT ve BTC-USDT aynı canonical_id'ye çözümlenmelidir.
- Aksi halde joins ve aggregation'lar güvensizleşir (Ambiguous mapping).
