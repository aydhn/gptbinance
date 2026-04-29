# Phase 13: Risk Motoru Mimarisi ve Intent-to-Risk Gate Akışı

## Amaç
Stratejilerin ürettiği alım/satım niyetlerinin (intent) canlı operasyon veya paper trading katmanlarına geçmeden önce zorunlu bir risk süzgecinden (gate) geçirilmesidir.

## Neden Ayrı Bir Katman?
Strateji üretmek ile riski yönetmek farklı disiplinlerdir. Strateji motorunun sadece alfa üretmeye odaklanması, risk motorunun ise portföy sağlığını korumaya odaklanması gerekir.
Eğer risk mantığı stratejiye gömülürse:
- Denetlenebilirlik (Auditability) kaybolur.
- Yeni stratejiler eklerken risk politikalarını kopyalamak gerekir.
- Kill-switch ve drawdown frenleri merkezi olarak yönetilemez.

## Akış
1. **Strategy Engine:** Sinyal üretir ve bunu bir `SimulatedOrderIntent` nesnesine çevirir.
2. **Context & Exposure:** Risk motoru çağrılmadan önce mevcut pozisyon büyüklükleri ve hesap bakiyesi kullanılarak `ExposureSnapshot` oluşturulur.
3. **Risk Engine:**
   - *Guards:* Basit ve hızlı kural kontrolleri (Örn: Drawdown Hard Stop aktif mi?).
   - *Policies:* Daha karmaşık risk sınırları kontrolleri (Örn: Maksimum brüt exposure aşıldı mı?).
   - *Sizing:* İstenen pozisyon boyutunun volalite ve rejim çarpanlarıyla (multiplier) ölçeklenmesi.
   - *Verdict:* Sonuç olarak `APPROVE`, `REDUCE`, `DEFER` veya `REJECT` kararı çıkar.
4. **Fill Model:** Sadece Risk Motoru tarafından onaylanmış (`is_risk_approved=True`) niyetleri kabul eder ve simüle eder.
