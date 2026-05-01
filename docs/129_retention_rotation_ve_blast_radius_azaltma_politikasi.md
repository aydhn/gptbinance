# Retention, Rotation ve Blast Radius Azaltma Politikası

## Retention Sınıfları
- **HOT**: Aktif kullanım, hemen silinmez.
- **WARM**: Arşivlenecek kullanım.
- **ARCHIVE**: Uzun dönem saklanıp sonra prune edilir.
- **DISPOSABLE**: Geçici, hemen silinir.
- Silme işlemleri yerine kontrollü Archive tavsiye edilir.

## Rotation Readiness
- Sistem otomatik secret rotasyonu yapmaz. Ancak bir secret değiştirildiğinde (örn: API_KEY) hangi modüllerin etkileneceği (Blast Radius) `RotationReadiness` ile raporlanır.
