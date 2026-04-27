# Phase 05: Definition of Done

## Tamamlanma Ölçütleri
- [x] Canlı websocket market veri akışı kurulabildi.
- [x] Gelen payloadlar raw string'den Pydantic event modellerine normalize edildi.
- [x] Event bus çalışıyor, subscribe/publish patterni doğru işliyor.
- [x] State cache `update_kline`, `get_latest_kline` vb. işlemlerle güncel durumu tutabiliyor.
- [x] Reconnect logic (backoff ile) ve Heartbeat/Stale stream detection yapıları kuruldu.
- [x] Kısa süreli tutulan Stream Buffer devrede.
- [x] CLI `--live-stream-smoke` vb. bayraklarla test edilebiliyor.
- [x] İlgili birim testleri (event_bus, state_cache, ws_parser vb.) eklendi ve tüm testler geçiyor.

## Bilinçli Olarak Ertelenenler
- Strateji Evaluation ve Signal Generation (Trade motoru yok).
- Order Placement (Paper / Live yok).
- Tarihsel veri entegrasyonu ve Data Ingestion (Bu faz sadece "akan" veriyi yakaladı, database'e persist etmedi).

## Sonraki Faz Önerisi (Phase 06)
**Başlık:** HISTORICAL DATA VE DATABASE İNŞASI
**Amacı:** Canlı sistemden alınan verilerin veya toplu fetch edilen verilerin SQLite (metadata) ve Parquet (kline) formatında kalıcı olarak saklanması. Böylece strateji motoru uyandığında önce geçmiş veriyi okuyup, üstüne canlı veriyi (Event Bus) ekleyebilecektir.
