# Binance Connector Mimarisi (Phase 03)

## Amaç
Bu doküman, uygulamanın Binance ile iletişim kurduğu ilk ciddi altyapı katmanı olan Connector modülünün tasarım felsefesini açıklar.

## Mimari Sınırlar (Boundaries)
Connector katmanı, uygulamanın geri kalanı için bir "Anti-Corruption Layer" (Bozulma Önleyici Katman) görevi görür.
- Uygulamanın diğer hiçbir kısmı `requests` kütüphanesini doğrudan import etmez.
- Uygulamanın diğer hiçbir kısmı Binance'in döndürdüğü ham JSON objeleri ile uğraşmaz.
- Tüm veriler (zaman, exchange kuralları, sembol listesi), `pydantic` kullanılarak sıkı tipli alanlara (domain models) dönüştürüldükten sonra dışarı verilir.

## Neden Ham Cevap Dönülmüyor?
Eğer strateji veya risk motorumuz Binance'in `status: "TRADING"` stringine doğrudan bağımlı kalırsa, Binance yarın bu formatı değiştirdiğinde (veya farklı bir borsa eklediğimizde) kodun her yerinde kırılmalar yaşanır. Bunu önlemek için Enum ve strict model dönüşümü yapıyoruz.

## Phase 03: Salt-Okunur
Bu fazda güvenlik gereği emir gönderimi, account detayı okuma veya WebSocket dinleme **bilinçli olarak** yapılmamıştır. Yalnızca public endpoint'lere (`/time`, `/exchangeInfo`) salt-okunur istek atılmaktadır.

## Gelecekteki Genişleme
Bu yapı, ileride `BinanceAuthenticatedClient`, `BinanceOrderService` ve `BinanceWebsocketClient` gibi bileşenlerin eklenebilmesi için modüler olarak tasarlanmıştır. `ClientFactory` yapısı sayesinde dev/paper/live ortamlarına göre farklı client türleri güvenle üretilebilir.
