# Event Bus ve State Cache Sözleşmesi

## State Cache
**Rol:** Canlı verinin en son bilinen durumunu saklamak.
- Storage katmanı DEĞİLDİR. Tarihsel verileri tutmaz (buffer'lar hariç).
- Tüm veri tipleri (Kline, Ticker, Book Ticker) event bus'tan geçtikten hemen sonra buraya yazılır.
- Herhangi bir bileşen (CLI, Dashboard, Strateji), O(1) hızında en güncel piyasa durumunu (örn: son mumun close değeri) almak için bu cache'i kullanır.

## Event Bus
**Rol:** Uygulama içi asenkron ve senkron decoupled iletişim.
- Herhangi bir sınıf, belirli bir model (örn: `KlineUpdateEvent`) geldiğinde tetiklenmek üzere `subscribe()` olabilir.
- Framework benzeri karmaşık yapıları reddeder. Tip güvenli `publish(event)` üzerinden ilerler.
- İzolasyon garantisi verir: Subscriber fonksiyonu (handler) exception fırlatsa dahi, `EventBus` bunu catch edip loglar, websocket akışını veya diğer subscriber'ları etkilemez.

## Gelecekteki Bağlantılar
- **Strategy Engine:** `EventBus` üzerinden `KlineUpdateEvent` dinleyerek (is_closed=True ise) sinyal üretecektir.
- **Paper Engine:** Piyasayı taklit edebilmek için `BookTickerEvent` dinleyip virtual order dolduracaktır.
- **Data Ingestor:** `KlineUpdateEvent` dinleyip bunu SQLite/Parquet kalıcı storage katmanına yazacaktır.
