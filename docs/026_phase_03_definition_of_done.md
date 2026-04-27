# Phase 03: Definition of Done

## Tamamlanma Ölçütleri

- [x] **Salt-Okunur İstemci:** Binance API'ye güvenli, rate-limit'leri izole eden ve kimlik doğrulama yapmayan bir Client factory eklendi.
- [x] **Profile Resolver:** Dev, Paper, Testnet, Live modlarına göre base_url ve yetkinlikleri belirleyen mekanizma yazıldı.
- [x] **Zaman Servisi:** Binance server time ile local time arasındaki gecikme (latency) ve kaymayı (drift) hesaplayan servis eklendi.
- [x] **Exchange Info Servisi:** Ham JSON cevaplarını okuyarak güvenli Pydantic veri modellerine (SymbolMetadata, vs.) çeviren parsing yapısı kuruldu.
- [x] **Symbol Kuralları:** `minNotional`, `tickSize`, `stepSize` için Float Precision hatalarından kaçınarak güvenli `Decimal` hesaplama ve yuvarlama fonksiyonları yazıldı.
- [x] **Health Check & Smoke Tests:** Uygulamanın ağa erişip erişemediğini ve zaman/veri parse işlemlerinin çalıştığını doğrulayan CLI komutları (`--check-binance-connectivity`, vb.) eklendi.
- [x] **Hiçbir Yan Etki Yok:** Emir gönderme veya hesap verisi çekme gibi "tehlikeli" endpointlere dokunulmadı.

## Bilinçli Ertelenenler
- Emir Gönderimi (Execution)
- Authenticated Endpoints (Bakiye kontrolü, sipariş izleme)
- Websocket Market Verisi
- Margin ve Futures endpoint destekleri. (Şimdilik yalnızca temel SPOT kuralları varsayıldı).

## Phase 04 Önerisi
Bir sonraki faz "Veri Alım ve Depolama (Data Ingestion & Storage)" olmalıdır. Borsa ile olan salt-okunur bağlantı kurulduğuna göre, Kline/Trade verisi çekilmeli ve SQLite/Parquet formatında lokal olarak depolanmalıdır.
