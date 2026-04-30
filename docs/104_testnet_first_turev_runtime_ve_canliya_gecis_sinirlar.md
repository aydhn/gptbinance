# Testnet-First Türev Runtime ve Canlıya Geçiş Sınırları

Türev ürünlerin eklenmesi "Hadi yüksek kaldıraçla para kazanalım" anlamına gelmez. Bu sistemin "Sıfır Bütçe, Maksimum Güvenlik" prensibine aykırıdır.

## Testnet-First Prensibi
Şu anda `ProductRegistry` üzerinde `FUTURES_USDM` için `readiness=ProductReadiness.TESTNET_ONLY` ve `MARGIN` için `PAPER_ONLY` varsayılan olarak ayarlanmıştır.
Bu şu anlama gelir:
- `BinanceLiveExecutor` (canlı borsa tetikleyicisi) türev emirler için *mainnet api* çağrısı yapmak yerine, *testnet api* çağrısı veya *hata/engelleme* fırlatır.
- `GoLiveGates` bileşeni (opsiyonel canlı doğrulama), yüksek kaldıraç talebi veya eksik/kapalı liquidation guard varlığında canlı geçişi (`LIVE FAIL`) reddeder.

## Güvenli Sınırlar
Bu fazda:
1. Max Kaldıraç Katı sınırlanmıştır (örnek: Futures max 5x).
2. Live ortamda agresif emir akışı (spamming high leverage) engellenmiştir.
3. Testnet-first yaklaşımı zorunlu tutulmuştur (`--run-derivatives-testnet-smoke`).
Türev özellikleri sadece Paper ve Testnet ortamında kapsamlı şekilde simüle edilir ve doğrulanır.
