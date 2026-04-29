# Paper Runtime Mimarisi ve Canlı Prova Akışı

## Amaç
Paper runtime, backtest ve walk-forward analizlerinden sonra, sistemin canlı piyasa verileri (WebSocket üzerinden) kullanılarak "sanki gerçek para ile işlem yapıyormuş" gibi çalışmasını sağlayan prova (rehearsal) katmanıdır.
Gerçek emir gönderimi (order placement) ve borsa etkileşimi HARİÇ, sistemin diğer tüm bileşenleri (feature generation, strategy, regime, risk, queue, fill simulation, PnL ve state yönetimi) gerçek zamanlı olarak işletilir.

## Mimari Akış
1. **Canlı Veri (Live Stream):** Binance WebSocket üzerinden Ticker/Kline verileri gelir.
2. **Event Processing:** Veri bufferlanır, feature cache'i güncellenir ve Paper Session callback'i tetiklenir.
3. **Intent Generation:** Strategy engine sinyal üretir; Risk engine bu sinyali denetler. Onaylanırsa `PaperOrderIntent` olarak intent kuyruğuna (IntentQueue) atılır.
4. **Order Lifecycle:** Intent, PaperOrder'a dönüşür ve OrderBook'a eklenir. Durumu takip edilir (Created -> Accepted -> Filled vb.).
5. **Fill Simulation:** Market koşulları ve varsayılan slippage, fee oranları hesaba katılarak, order'lar sanal olarak eşleştirilir (fill edilir).
6. **Position ve PnL (Mark-to-Market):** Kapanan ve açık olan pozisyonlar güncellenir. Realize edilmiş ve edilmemiş PnL sürekli hesaplanır. Equity snapshot alınır.
7. **Health ve Telemetry:** İşlem gecikmeleri (stream freshness, feature lag), hata sayıları ve drawdown oranları izlenerek `SessionHealth` belirlenir.
8. **Notification:** Telegram entegrasyonu üzerinden kritik olaylar (Kill switch, büyük drawdown, fill özetleri) rate-limit'li olarak operatöre iletilir.
9. **Persistence (Artifact Storage):** Emirler, fill bilgileri, equity snapshot'ları ve session manifest bilgileri SQLite'a kaydedilir.

Bu katman, live execution'a geçmeden önceki son ve en kritik eşiktir. Deterministik kurallarla çalışır.
