# Freshness Budgets & Profile-Aware Truth Policy

## Canonical Market Clock
Local monotonic clock ile Binance sunucu zamanı arasında eşleşme ve drift takibi yapılır. Elevate olan durumlarda işlemler block edilir.

## Freshness Budgets
Farklı işlem modları (profil) için farklı tolerans seviyeleri bulunur:
- `paper_default`: Gevşek.
- `shadow_research`: Uyarı verir, izin verir.
- `testnet_exec`: Sıkı kurallar.
- `canary_live_caution`: Çok daha sert (örn. Max Lag 500ms).
- `derivatives_testnet`: Mark Price üzerinde ekstra duyarlılık.

Stale data geldiğinde `ALLOW` kararı alınamaz.
