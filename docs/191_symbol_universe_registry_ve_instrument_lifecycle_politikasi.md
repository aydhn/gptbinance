# 191. Symbol Universe Registry ve Instrument Lifecycle Politikası

Bu politika, sistemin trade ettiği sembollerin nasıl tanımlandığını, saklandığını ve yaşam döngülerinin nasıl yönetildiğini belirler.

## Instrument Registry
Sistem, her sembolü ürün tipi (Spot, Margin, Futures) ile birlikte eşsiz bir şekilde tanımlayan bir Instrument Registry kullanır. Bu registry:
- Yalnızca resmi borsa API'lerinden (örn. Binance Exchange Info) beslenir.
- HTML scraping veya gayri resmi veri kaynaklarının kullanımını kesinlikle yasaklar.
- Sembollerin tick size, step size, min notional gibi kritik metadata bilgilerini içerir.

## Product-Aware Symbol Modeling
Aynı sembol adı (örn. BTCUSDT), farklı ürün tiplerinde farklı kurallara tabi olabilir. Bu nedenle, semboller her zaman ürün tipi ile birlikte değerlendirilir. Spot BTCUSDT ile Futures BTCUSDT aynı varlık değildir ve farklı filtre, durum ve uygunluk değerlendirmelerinden geçerler.

## Lifecycle Management
Sembollerin yaşam döngüsü (Listing, Delisting, Halted, Maintenance) yakından takip edilir.
- Durumu değişen semboller anında tespit edilir ve sistem uyarılır.
- "Delisted" veya "Maintenance" durumundaki semboller otomatik olarak engellenir (blocked).

## Discretionary Mutation Yasağı
Sisteme manuel, keyfi ("bu coin popüler oldu, ekleyelim") sembol ekleme veya çıkarma yapılamaz. Sembollerin trade edilebilirliği tamamen veri destekli (liquidity, spread, filter geçerliliği) ve profillere özgü yapılandırmalarla belirlenir.
