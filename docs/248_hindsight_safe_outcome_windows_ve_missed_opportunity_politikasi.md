# Phase 48: Hindsight-Safe Outcome Windows ve Missed Opportunity Politikası

Bir trade fırsatı kaçtığında (veya engellendiğinde), "keşke alınsaydı" demek, geçmişi geleceğe (hindsight bias) taşımaktır. Bu sistem, geçmiş olayların sonucunu değerlendirirken kesin yargılardan kaçınır ve hindsight-safe (sonradan-güvenli) bir değerlendirme çerçevesi kullanır.

## Hindsight-Safe Yorum İlkeleri
- Sonucu değerlendirirken strateji çalıştırıldığı anın market truth ve event bağlamı göz önüne alınır.
- Stale data varsa sonucun güvenirliği düşük (Low Confidence) kabul edilir.
- Otomatik optimizasyon yapılmaz; sadece tanı konulur.

## Outcome Windows
Gerçekleşmeyen işlemler için gelecekteki x zaman dilimindeki sonuç izlenir:
- `very_short` (Örn. 5 dakika)
- `short` (Örn. 1 saat)
- `medium` (Örn. 1 gün)
- `session_bound` (Aynı seans bitimine kadar)
- `regime_bound` (Rejim değişene kadar)

## Missed Opportunity Sınıfları
Kaçırılan fırsatların tanısal sınıfları:
- `good_block_candidate`: Bloklandı ve sonrasında da piyasa kötü gitti. (İyi ki bloklanmış)
- `missed_alpha_candidate`: Bloklandı ancak fırsat iyi sonuç verebilirdi. (Muhtemel kaçırılmış fırsat)
- `blocked_and_likely_saved_loss`: Bloklanması kesin bir kaybı önledi.
- `indeterminate`: Sonuç belirsiz (Örn: flat kaldı).
- `unsafe_to_judge`: Veri kalitesi, event kesintileri nedeniyle değerlendirme yapılması güvenli değil.

## Certainty Tehlikesi
Hiçbir zaman "bu kural yanlış, kaldıralım" yargısı sistem tarafından kesin verilmez. Tüm çıktılar confidence skoru ve evidence ile diagnostic (tanısal) bir uyarı veya rapor olarak insan gözden geçirmesine sunulur.
