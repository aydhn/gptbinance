# Phase 48: Decision Quality ve Signal-To-Action Funnel Mimarisi

Trading sistemlerinde PnL ve Executed Trades odaklı analiz, kararların arkasındaki gerçek bağlamı gizler. Neden bazı sinyallerin elendiği, fırsatların neden kaçırıldığı veya stratejinin ürettiği sinyallerin neden realize olmadığı görülemez.

Decision Quality ve Signal-To-Action Funnel katmanı, bir trade sinyalinin uçtan uca yolculuğunu şeffaf kılar.

## Opportunity Capture
Her anlamlı strateji sinyali, execution katmanına ulaşmadan önce bir `OpportunityCandidate` olarak kaydedilir. Bu kayıt; symbol, regime, strategy family, timeframe, signal timestamp, event context ve market truth posture gibi kritik metaverileri içerir.

## Funnel Aşamaları (Signal-To-Action)
Karar yolculuğu funnel aşamalarında takip edilir:
1. `signal_generated`
2. `regime_context_attached`
3. `risk_evaluated`
4. `portfolio_evaluated`
5. `policy_evaluated`
6. `intent_compiled`
7. `lifecycle_submitted`
8. `acknowledged`
9. `partially_filled` / `fully_filled`
10. `exited`

Bu aşamaların herhangi birinde süreç kesilebilir (`blocked`, `skipped`, `suppressed`). Bu durumda funnel, kararın nerede ve neden kesildiğini kaydeder.

## Executed, Blocked ve Skipped Ayrımı
Sistem, karar çıktılarını net sınıflara ayırır:
- **Executed:** Uçtan uca başarıyla gerçekleşmiş trade kararları. Execution friction'ları analiz edilir.
- **Blocked:** Policy, risk, capital, event veya market-truth katmanlarında sert kurallarla kesilmiş kararlar.
- **Skipped:** Stratejinin veya portfolio allocator'ın, fırsatı uygun bulmadığı ancak sert bir kural ihlali olmayan durumlar.

## Neden Sadece PnL Değil?
Sadece gerçekleşen işlemlere bakmak, "Too Restrictive" veya "Too Permissive" policy etkilerini maskeler. Sistemin kalitesi, reddedilen kararların isabetliliğine ve onaylanan kararların execution kalitesine bütünleşik bir bakış açısıyla ölçülebilir. Bu faz, auto-optimization yapmadan "tanısal bir omurga" kurar.
