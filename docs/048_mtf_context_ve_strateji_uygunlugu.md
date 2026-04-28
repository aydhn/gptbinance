# MTF Context ve Strateji Uygunluğu

Çoklu zaman dilimi (Multi-Timeframe - MTF) analizi, lokal gürültüleri filtrelemek ve makro yönü anlamak için şarttır.

## MTF Mantığı
- **Execution Context (Örn. 15m)**: İşleme girilecek spesifik zaman dilimi.
- **Bias Context (Örn. 1h)**: Orta vadeli eğilim.
- **Macro Context (Örn. 4h)**: Piyasanın genel yönü.

Sistem bu üç zaman dilimindeki rejimleri birleştirerek (`MultiTimeframeRegimeContext`) tutarlılığı ölçer.

## Alignment (Hizalama) ve Consistency (Tutarlılık)
Alt ve üst zaman dilimleri çelişiyorsa (örn. 15m Uptrend, 4h Downtrend), `consistency_score` düşer ve strateji uygunluğu bu durumdan etkilenir. Sızıntı (leakage) oluşmaması için her zaman dilimi kendi kapalı mum verisi üzerinden bağımsız değerlendirilir.
