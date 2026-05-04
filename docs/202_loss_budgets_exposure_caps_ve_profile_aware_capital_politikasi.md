# Loss Budgets, Exposure Caps ve Profile-Aware Capital Politikası

## Loss Budgets (Kayıp Bütçeleri)
Sermayenin belirli süre zarflarında maksimum ne kadar eriyebileceğini belirler:
- `INTRADAY`
- `ROLLING_24H`
- `WEEKLY`
Severity seviyeleri (Hard/Soft) ile bütçe aşımlarında sistemi durdurur (Freeze/Reduce) veya uyarır.

## Exposure Caps
- `max_deployable_capital`: Bir tier'da en fazla bağlanabilecek nakit.
- `max_concurrent_positions`: Aynı anda kaç açık pozisyon olabilir.
- `max_symbol_concentration`: Bir sembole en fazla yatırılabilecek sermaye yüzdesi.
- `max_leverage`: Kullanılabilecek azami kaldıraç.
- `correlated_cluster_exposure_cap`: Birbirine yüksek korelasyonlu ürünlere toplanan risk limiti.

## Profile Aware
Testnet, Paper, Canary veya Live Caution profilleri için farklı bütçe değerlendirmeleri yapılır. Paper'daki bütçe ihlali sadece simülasyon uyarısı verirken, Live Caution tier'daki bütçe ihlali acil `Reduce` (pozisyon azaltma) eylemini tetikler.
