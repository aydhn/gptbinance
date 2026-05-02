# Phase 28: Human-in-the-Loop Control & Sensitive Action Policy

## Neden Approval / Control Katmanı Gerekiyor?
Teknik olarak sistem tüm safety, risk ve ops gate'lerine sahip olsa da, tek bir geliştiricinin veya operatörün tek komutla canlı sistemi derinden etkileyecek (live session başlatma, flatten, upgrade apply, restore apply vb.) aksiyonları alabilmesi operasyonel ve finansal açıdan büyük bir risktir. Bu katman, "kim, hangi yetkiyle, ne zaman, neden talep etti ve kim onayladı" sorularının yanıtını veren, audit-heavy, insan-onaylı bir güvenlik bariyeri sağlar.

## Sensitive Action Sınıfları
Aksiyonlar, kritiklik düzeylerine (LOW, MEDIUM, HIGH, CRITICAL) ve gerektirdiği operatör rollerine (OPS, RISK, SECURITY, RELEASE, ADMIN) göre sınıflandırılmıştır.
Örnek Hassas Aksiyonlar:
- `START_LIVE_SESSION` (HIGH, 2 Onay, TTL: 1 saat)
- `FLATTEN_LIVE_SESSION` (CRITICAL, 2 Onay, TTL: 30 dk)
- `APPLY_RESTORE` (CRITICAL, 2 Onay, TTL: 1 saat, Break-glass yasak)

## Request -> Approval -> Authorization Zinciri
Sistem onay ve çalıştırma yetkisini açıkça ayırır:
1. **Action Request**: Operatör eylemi talep eder.
2. **Approval Decision**: Yetkili kişiler (four-eyes kuralı ile) talebi değerlendirip onaylar veya reddeder.
3. **Authorization Result**: Çalıştırma anında, onayın süresinin geçip geçmediği (stale context) ve hedeflenen run/bundle ID'lerinin değişip değişmediği kontrol edilerek kesin yetki verilir.

## Neden Execution-Time Revalidation Zorunludur?
Onay verildikten sonra (örneğin 3 saat boyunca), piyasa koşulları, incident durumu veya aktif release bundle değişmiş olabilir. Authorization anında (execution-time) bağlamın ve TTL'in (Time-To-Live) tekrar doğrulanması, onaylanmış ancak bağlamını yitirmiş (stale) komutların kazara çalıştırılmasını engeller.

## Neden Approvals Gate'leri Bypass Etmez?
İnsan onayı, sistemin risk, safety ve health gate'lerinin yerine geçmez. Bir live session başlatılması için "four-eyes" onayı alınmış olsa dahi, eğer "Mainnet Disarmed" veya "Reconciliation Failed" durumu varsa, sistem işlemi reddetmeye devam eder. İnsan denetimi ek bir filtredir, override yetkisi değildir (Break-glass hariç).
