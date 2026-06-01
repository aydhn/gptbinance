# Drift Plane / Post-Normal Stability Governance

## Neden Drift Plane?
Kurumsal sistemlerde kriz sonrası en sinsi risk, sistemin normal görünüp yavaşça yeniden bozulmasıdır. Normalization verilmiş olabilir, limits kısmen açılmış olabilir, recap tamamlanmış olabilir; fakat capability yavaşça düşüyor, guardrails sessizce emekli oluyor, beneficiary impact tekrar büyüyor, control drift başlıyor, compliance disiplinleri gevşiyor olabilir. Eğer baseline/signal/regression/recurrence semantics typed değilse sistem yeniden krize yürürken bunu ancak geç fark eder.

Bu yüzden **baselines/signals/domains -> breaches/restrictions/recurrence -> scars/re-normalization/trust** zinciri ayrı bir governance katmanı gerektirir.

## Mimari Prensipler
- **baselines/signals -> breaches/restrictions -> scars/renormalization -> trust akışı** zorunludur.
- **Monitored != Controlled != Stable**. Bir metriğin izlenmesi, onun kontrol altında olduğu veya stabil olduğu anlamına gelmez.
- **No Hidden Drift**. Local drift hidden by global aggregation, slow-burn de-normalization ve cosmetic stability yasaktır.
- **No Recurrence Theater**. Scar reactivation ve recurrence triggers açıkça yönetilmelidir.

## Bu Fazın Sınırları
Bu faz bir "metric dashboard" fazı değildir. "Alarm sayacı" veya "grafikte küçük oynama" fazı da değildir. "Green ise sorun yok" yaklaşımını yıkarak drift'i typed bir governance nesnesine dönüştürür.
