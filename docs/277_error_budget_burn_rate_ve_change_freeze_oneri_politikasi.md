# Error Budget, Burn Rate ve Change Freeze Öneri Politikası

## Error Budget Yönetimi
SLO'lar belirlendikten sonra, bütçe tüketimi (error budget consumption) kaydedilir. Soft exhaustion ve hard exhaustion ayrımları yapılarak, bütçenin tükenme ciddiyeti belirlenir.

## Burn Rate Analytics
- **Fast Burn:** Kısa zaman diliminde bütçenin büyük kısmının (ör. >%10) tüketilmesi. Genellikle acil "Major Change Freeze" önerisini tetikler.
- **Slow Burn:** Uzun zaman diliminde istikrarlı bir şekilde bütçenin tüketilmesi. Genellikle uyarı (Caution/Degraded) tetikler.

## Change Freeze Önerileri
Burn rate ve scorecard sonuçlarına göre üretilir:
- `NO_EXPANSION_RECOMMENDED`: Yeni aktivasyon veya limit artışlarını durdurun.
- `RELEASE_HOLD_RECOMMENDED`: Prodüksiyon güncellemelerini tutun.
- `MAJOR_CHANGE_FREEZE`: Sisteme müdahale etmeyin.

Bunlar sistemin release ve governance katmanlarına bir "öneri" (recommendation) olarak sunulur. Otomatik bir "kill-switch" değillerdir.
