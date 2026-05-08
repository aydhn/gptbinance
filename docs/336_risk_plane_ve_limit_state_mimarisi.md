# Risk Plane & Limit State Mimarisi

Bu doküman Phase 66 kapsamında geliştirilen Risk Plane ve Limit State Governance mimarisini açıklar.

## Akış (Flow)

Sistem şu kanonik akışı izler:
`Positions/Ledger -> Canonical RiskState -> Evaluation -> Breaches -> Response Intents -> Cooldowns/Reentry`.

1. **RiskState Üretimi**: Position Plane ve Ledger Plane verileri alınır, `CanonicalRiskStateBuilder` tarafından snapshot'lar üretilir. Bunlar drawdowns, losses, concentration, margin, liquidation gibi surfaces'i içerir.
2. **Limit Değerlendirmesi**: `CanonicalBreachClassifier`, registry'deki limitleri kullanarak Soft/Hard/Emergency gibi tipli breach'ler üretir.
3. **Response Intents**: `ResponseIntentEngine`, oluşan breach'lere bakarak `NO_NEW_EXPOSURE`, `REDUCE_EXPOSURE`, veya `EMERGENCY_DELEVERAGE_INTENT` gibi execution'ı durduracak block intent'leri üretir.
4. **Cooldowns & Re-entry**: Breach'ler `CooldownGovernance` üzerinden sisteme belirli bir TTL block uygular. Tekrar giriş ancak `ReentryEvaluator` kapılarından geçilerek (cooldown expiration, clean limits, vb.) sağlanır.

## Neden Auto-Liquidator Yok?
Bu mimaride auto-liquidator (otomatik emir kapatıcı) **bilinçli olarak** yasaklanmıştır.
Sistem sadece "Intent" üretir. Bunun amacı:
- Risk kararının bağımsız denetlenebilmesi (Execution plane hatası ile karışmaması)
- Market condition, thin markets veya fake-hedges yüzünden oluşacak "yanlış alarm" likidasyonları önlemek
- Risk review'i zorunlu kılarak Separation of Duties'i sağlamak

## Neden Soft vs Hard Breach Ayrımı?
- Soft Breach: Operatöre Advisory bilgi verir, limit azaltmayı teşvik eder ama exposure growth'u tamamen dondurmaz.
- Hard Breach: Yeni pozisyon almayı anında durdurur (`NO_NEW_EXPOSURE`).
- Emergency Breach: Çok kritik sapmalarda Deleveraging başlatan en yüksek priority alarmdır.
Bu katmanlar sayesinde risk reaksiyonları kalibre edilmiştir.
