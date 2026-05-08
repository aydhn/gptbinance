# Drawdown, Margin, Liquidation Proximity ve Deleverage Politikası

Risk Plane, farklı risk kayıplarını tek bir "Loss" metriğinde toplamaz. Ayrı kırılımlar üretir:

## Drawdown Classes
- **INTRADAY**: Gün içi tepe noktasından (peak_value) düşüş. Realized ve Unrealized olarak ayrılır.
- **ROLLING**: Belirli bir zaman dilimi üzerinden alınan drawdown.
Drawdowns, "Peak - Current" mantığıyla reset semantics'e ("DAILY" vb.) bağlı ölçülür.

## Margin Pressure
Kullanılabilir (usable) teminatın kilitli (locked) teminata oranı `margin_usage_ratio` ile ölçülür.
Bu oran SAFE -> ELEVATED -> PRESSURE -> CRITICAL sınıflarına oturtulur.

## Liquidation Proximity
Gerçek mark_price ile liquidation_price arası "proximity_ratio" belirlenir.
`stale_mark` (eski fiyat) varsa, conservative buffer mekanizması devreye girip proxy olarak riski **daha yüksek** gösterir (conservative tightening).

## Deleverage Intents
Bu durumlar `EMERGENCY_DELEVERAGE_INTENT` üretir. Intent üretildikten sonra ilgili domain'de cooldown başlar. Usable collateral sensitivity yüksek tutulmuştur, yani cross-margin book'larında collateral düşüşü, liquidation limit breach olarak sınıflandırılabilir.
