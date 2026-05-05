# Stream / Snapshot Convergence & Symbol Truthfulness

## Websocket vs REST Uyum (Convergence)
Aynı sembol/fiyat bilgisinin Stream'den gelen son hali ile periyodik alınan REST snapshot'ı kıyaslanır. Eşitsizliklerde `TRANSIENT_DIVERGENCE` veya `PERSISTENT_DIVERGENCE` sinyali üretilir.

## Symbol Truthfulness
Tüm bu denetimlerin birleşimi bir 'Global Truthfulness' karnesi çıkartır:
- CLEAN
- CAUTION
- DEGRADED
- BLOCKED
- NEEDS_REVIEW

Tek bir skor dönmez, ayrıntılı sebep-sonuç ağacı (reasons breakdown) döner.
