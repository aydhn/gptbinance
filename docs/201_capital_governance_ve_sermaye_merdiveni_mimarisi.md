# Capital Governance ve Sermaye Merdiveni Mimarisi

## Capital Tier
Her bir profil için ayrı ayrı seviyelendirilmiş sermaye dilimleridir. Bunlar:
- `paper_zero`: Risk yok, simülasyon.
- `testnet_zero`: Exchange testnet'leri.
- `canary_micro`: Çok küçük gerçek sermaye (ör. $50). Canlı ortam hatalarını görmek için.
- `canary_small`: Biraz daha büyük, istatistiksel geçerlilik aranan tier (ör. $200).
- `live_caution_tier_1/2`: Güvenilen stratejilerin canlıda scale edildiği ama halen çok ihtiyatlı olunan alan.
- `restricted_derivatives_micro`: Vadeli işlemler için çok küçük limitli ayrı tier.

## Tranche
Tier limitlerinin tamamı bir anda verilmez. Limitleri parça parça aktifleştirmeyi sağlayan birimlere Tranche (dilim) denir. Kademeli sermaye aktarımı sağlar.

## Neden Auto Scale-up Yok?
Sermayeyi büyütmek, trade stratejisinin "başarı oranından" çok daha büyük bir operasyonel karardır:
1. Reconciliations (Defter eşleşmeleri) kusursuz mu?
2. Observability / Alert history temiz mi?
3. Stress ve Qualification raporları güncel mi (stale değil mi)?
Tüm bu sorulara otomatize karar verilip aniden fonların borsaya sürülmesi engellenmiştir. Escalation Engine, bu verileri toplayarak bir "Advisory / Readiness" (Tavsiye / Hazırlık) raporu oluşturur. Geçiş ancak Approval (İnsan Onayı) ile yapılır.

## Escalation, Reduction ve Freeze
- **Escalation (Scale-up):** Bir üst Tier'a geçiş durumunda ladder kontrolü yapılır, approval istenir.
- **Reduction (Scale-down):** Günlük bütçe ihlali veya stress durumu olduğunda bir alt Tier'a geçilmesi veya pozisyonların azaltılması istenir.
- **Freeze:** Olası ledger hataları veya ciddi alert durumunda sistem dondurulur (Thaw - çözülene kadar).
