# Symbol Metadata ve Exchange Kısıtları

## Metadata'nın Önemi
Kripto para borsalarında her sembolün kendine has kuralları (precision, tick size, step size, min notional) vardır. Bu kurallar göz ardı edilirse, oluşturulan emirler Binance tarafından reddedilir (`APIError`).

## Kritik Kısıtlar (Filters)

1. **PRICE_FILTER (Tick Size)**
   Bir varlığın fiyatının artabileceği en küçük birimi belirtir.
   *Sorun:* Eğer tick size 0.01 ise ve siz 1.005 fiyatından emir yollarsanız emir reddedilir.
   *Çözüm:* `SymbolRules.round_price` metodu ile fiyatlar Decimal kullanılarak güvenli bir şekilde yuvarlanır.

2. **LOT_SIZE (Step Size & Min/Max Qty)**
   Bir varlığın miktarının artabileceği en küçük birimi belirtir.
   *Sorun:* Eğer step size 0.1 ise ve 1.15 miktarında alım girmeye çalışırsanız emir reddedilir.
   *Çözüm:* `SymbolRules.round_quantity` ve `is_valid_quantity` ile güvence altına alınır.

3. **MIN_NOTIONAL / NOTIONAL**
   Bir emrin dolar bazındaki (veya quote bazındaki) minimum toplam değerini belirtir.
   *Sorun:* Örneğin Binance'te minimum notional genellikle 5-10 USDT'dir. 2 USDT'lik emir gönderilemez.
   *Çözüm:* `SymbolRules.check_min_notional` metodu ile emir işleme konmadan önce filtrelenir.

## Gelecek Fazlarda Kullanımı
Bu metadata, `Execution Katmanı` oluşturulurken emri borsaya yollamadan önce (Pre-Trade Validation) çalıştırılacaktır. Bu sayede, hatalı veya "Exchange'den red yiyeceği garanti olan" emirler daha API limitleri harcanmadan sistemde reject edilecektir.
