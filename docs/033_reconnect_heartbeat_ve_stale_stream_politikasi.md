# Reconnect, Heartbeat ve Stale Stream Politikası

## Neden Gerekli?
Borsa websocket bağlantıları güvenilir değildir:
1. ISP veya DNS sebepli anlık düşmeler yaşanabilir.
2. Borsa her 24 saatte bir bağlantıyı kasten sonlandırabilir.
3. Sessiz kopmalar (zombi bağlantılar / stale stream) meydana gelebilir; bağlantı TCP seviyesinde açık görünür ama veri akmaz.

## Politikalar

### 1. Exponential Backoff ile Reconnect
Kopan bağlantı anında sonsuz ve agresif bir döngüde yeniden bağlanmaya çalışmamalıdır.
- `initial_backoff` (1 sn) ile başlar.
- Her başarısız denemede süre 2 katına çıkar (`max_backoff` sınırına kadar, örn: 60 saniye).
- `max_reconnect_attempts` (örn: 50) aşıldığında sistem kendini korumaya alır (kalıcı log/alert).

### 2. Stale Stream (Zombi Bağlantı) Tespiti
Bir websocket bağlantısı `is_alive=True` görünse dahi, eğer belirli bir süre (örn: `stale_threshold_seconds = 30`) hiç event gelmiyorsa bu bağlantı stale (bayat) kabul edilir.
- `ws_health.py` içindeki monitor her mesajda `last_message_time` değerini günceller.
- Background worker periyodik olarak `(now - last_message_time) > threshold` kontrolü yapar.
- Stale durum tespit edildiğinde event bus'a `StreamStatusEvent(status="degraded")` yayımlanır ve Telegram üzerinden haber verilir.

### 3. Future Risk
Zombi bağlantılar, future live trading senaryolarında stratejilerin "fiyat değişmiyor" zannedip yanlış işlem açmalarına sebep olabilir. Bu yüzden `is_stale` kontrolü trade engine tetikleyicisinden önce bir güvenlik bariyeri olacaktır (Live Guard).
