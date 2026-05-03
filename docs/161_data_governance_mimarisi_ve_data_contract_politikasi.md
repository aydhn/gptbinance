# Data Governance Mimarisi ve Data Contract Politikası

## Neden Data Governance?
Trading sistemi ne kadar iyi olursa olsun, veri kaynağı, şema, zaman damgası, canonical kimlik ve dönüşüm zinciri kontrolsüzse; backtest, ML, analytics, governance ve live runtime aynı gerçekliği konuşmaz.

## Data Contracts
Data contracts; raw, normalized, feature, ML dataset ve analytics summary veri yapıları için gereksinimleri (required fields, nullable, uniqueness vb.) açıkça belirler.

## Zincir:
Raw -> Normalized -> Features -> ML -> Bundles

## Kurallar
Sessiz schema mutation kesinlikle yasaktır. Her değişim şema evrim kurallarına tabi olmalıdır.
