# PnL, Health ve Session Operasyon Politikası

## PnL ve Position State
- **Mark-to-Market:** Açık pozisyonlar anlık piyasa fiyatına (Tick veya Kline) göre değerlenir (Unrealized PnL).
- **Equity Snapshot:** Realize PnL, komisyon kesintileri ve Unrealized PnL toplamı alınarak peak_equity ile karşılaştırılır ve anlık drawdown_pct bulunur.
- Equity snapshot'ları düzenli olarak kaydedilir.

## Session Health Monitoring
`SessionHealth` durumu şu bileşenlerle hesaplanır:
- **Stream Freshness:** Gelen verilerin zaman etiketleri (event_time) ile sistem zamanı (now) karşılaştırılarak hesaplanan lag. Lag çok artarsa `DEGRADED` veya `CRITICAL` olur.
- **Drawdown:** Maksimum equity seviyesinden düşüş belirli bir eşiği (%10 gibi) aşarsa health `CRITICAL` olur ve gerekirse kill-switch devreye girer.
- **Error Count:** Sürekli exception fırlatılıyorsa health bozulur.

## Operasyon Yönetimi
- CLI üzerinden session başlatma (`--run-paper-session`), izleme (`--show-paper-summary`, vb.) işlemleri desteklenir.
- Başarısızlık durumlarında veya session durdurulduğunda SQLite veritabanına tüm durum kaydedilir.
