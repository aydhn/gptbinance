# Canlı Veri Akışı Mimarisi (Live Stream Architecture)

## Hedef
Canlı websocket veri akışının güvenilir, kopmalara dayanıklı ve uygulamanın geri kalanı için temiz bir kaynak olmasını sağlamak. Strateji ve order execution katmanlarından tamamen izole bir şekilde verileri toplamak, parse etmek ve dağıtmak.

## Katmanlar ve Sorumluluklar

1. **Transport Katmanı (`ws_client.py`):**
   - Yalnızca ham websocket bağlantısını yönetir.
   - Bağlanma, mesaj alma ve backoff/reconnect mekanizmalarını işletir.
   - Gelen verinin içeriğini bilmez.

2. **Parse Katmanı (`ws_message_parser.py`):**
   - Ham JSON stringleri alır.
   - Hatalı formata sahip mesajları (örn: parse error) güvenle izole eder.
   - Pydantic domain event modellerine (`live_stream_models.py`) çevirir.
   - Uygulamanın geri kalanını "exchange API formatı" kirliliğinden korur.

3. **Event Dağıtım Katmanı (`event_bus.py`):**
   - Pydantic objelerini alır.
   - Olay türüne göre kayıtlı handler'lara (subscribers) dağıtır.
   - Handler hatalarının (örn: strateji çalışırken fırlatılan exception) websocket bağlantısını düşürmesini önler.

4. **Cache & Buffer Katmanları (`state_cache.py`, `stream_buffer.py`):**
   - State Cache: Sistemin son bilinen durumu için hızlı bir (O(1)) okuma noktası sunar. Stratejiler son fiyatı okumak için event beklemek zorunda kalmaz.
   - Buffer: Sadece kısa süreli (son N event) bir gözlemleme noktasıdır. Replay veya debug amaçlıdır, kalıcı depolama değildir.

5. **Liveness & Health Katmanı (`ws_health.py`):**
   - Akışın "gerçekten yaşıyor mu?" (Stale stream detection) kontrolünü yapar.
   - İstatistikler tutarak dış dünyaya (örn. Telegram) uyarı altyapısı sağlar.
