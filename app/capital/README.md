# Capital Governance & Deployment Ladder

## Amaç
Bu modül, trading platformunun canlı sermayeyi nasıl yönettiğini, onay mekanizmalarını, sermaye büyütme/küçültme kurallarını ve evidence-based (kanıt odaklı) kararlarını kontrol eder.

**Neden Gerekli?**
Bir trading stratejisi kağıt üzerinde (paper/testnet) iyi sonuç verse bile, anında tam kapasite canlı (live) ticarete açılması risklidir. Capital Governance katmanı, risk-stress analizleri, qualification geçmişi, cüzdan mutabakatları ve diğer evidence'lara bakarak, sermayenin kontrollü adımlarla (tier tier) büyütülmesini sağlar.

**Neden Auto Scale-up Yok?**
Sistemin hiçbir yerinde "kâr edildi, hadi limiti 2 katına çıkaralım" gibi bir otomatik işlem yoktur. Capital Ladder mekanizması, sadece "bir sonraki tier için kanıtlar yeterli" bilgisini üretir (escalation check). Karar bir insan yöneticinin onayıyla alınır. Bu faz bir bileşik getiri motoru değil, bir governance / control / compliance duvarıdır.

## Sınırlar (Ne Yapar, Ne Yapmaz)
- **Ne Yapar:** Sermaye tier'larını (canary_micro, live_caution vb.) tanımlar. Hangi profile'da ne kadar loss budget harcandığına bakar. Evidence freshness'ı ölçer. Scale-up / freeze advisory'leri verir.
- **Ne Yapmaz:** Otomatik emir büyüklüğü ayarlamaz. Kârları otomatik bileşiğe sokmaz (compounding). Otomatik risk eşiklerini ihlal etmez. Emir stratejisinin yerini almaz, ona limitler ve governance koyar.

## Temel Akış
`Tiers (Sınırlar)` -> `Budgets (Limitler)` -> `Posture (Durum Özeti)` -> `Escalation/Reduction (Artırma/Azaltma Onay Durumları)`
