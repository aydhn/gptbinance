# Phase 19 - Definition of Done

Bu fazın başarılı sayılabilmesi için aşağıdaki kriterler karşılanmıştır:

## Tamamlananlar:
- [x] `app/products/` altında Spot/Margin/Futures ayrımı ve Capability modellemesi.
- [x] `app/execution/derivatives/` içerisinde Leverage, Margin/Position Modes, Reduce-only kuralları.
- [x] Liquidation (Yaklaşık Mesafe) ve Maintenance Margin görünürlüğü sağlayan approx model.
- [x] Funding ve Borrow muhasebe temel modeli ve Backtest/Paper runtime entegrasyonu.
- [x] Risk engine güncellemesi (Leverage Cap, Liquidation Veto).
- [x] Ops Go-live gates ve Product-Aware portfolio allocations.
- [x] Telegram uyarı şablonları (Liquidation, Leverage Cap, Funding).
- [x] CLI üzerinden komutlar (`--set-leverage`, `--show-liquidation-risk`, vb.).
- [x] Test coverage (Registry, Modes, Reduce-Only, Liquidation, vb.).

## Bilinçli Olarak Ertelenenler (Out of Scope):
- Tam (Birebir) Liquidation Engine Reverse Engineering (Borsanın tüm özel formüllerini kopyalamak çok karmaşıktır).
- Sınırsız / karmaşık Hedging (Multi-leg basis arbitrage).
- Mainnet Futures Auto-Trading (Şu an Testnet-First / Paper-Only gating aktif).
- Otomatik Leverage Optimizasyonu (Kullanıcı manuel `--set-leverage` komutu ile test eder).

## Phase 20 Önerisi:
**PHASE 20: DYNAMIC DERIVATIVES STRATEGY ADAPTATION VE CROSS-MARGIN YÖNETİMİ**
Amacı: Bu fazda kurulan omurga üzerine, volatiliteye göre otomatik kaldıraç düşüren, funding rate alpha kovalayan strateji uzantıları eklemek ve cross-margin hesap senkronizasyonunu kusursuzlaştırmaktır.
