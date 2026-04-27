# Phase 02: Definition of Done

Bu fazın amacı, projeyi fikir aşamasından çıkartıp çalıştırılabilir, güvenli ve test edilebilir bir çekirdek altyapı haline getirmektir.

## Tamamlanma Ölçütleri (DoD)

- [x] **Ortam Profilleri:** `dev`, `paper`, `testnet`, `live` profilleri enum olarak tanımlandı ve akışa entegre edildi.
- [x] **Konfigürasyon Sistemi:** Pydantic tabanlı, tipli, hiyerarşik ve .env destekli config yapısı kuruldu. Maskelenmiş (redacted) config çıktısı alınabiliyor.
- [x] **Güvenli Bootstrap:** Uygulamanın `python -m app.main` ile başlatılma akışı (dizinlerin açılması, config yüklenmesi, validasyonlar) oluşturuldu. Check-only ve print-effective-config CLI argümanları çalışıyor.
- [x] **Yapılandırılmış Loglama:** JSON tabanlı, secret redaction özellikli, run_id içeren logging mekanizması kuruldu.
- [x] **Live Guard:** Canlı modun kazara açılmasını engelleyen çok katmanlı savunma hattı yazıldı.
- [x] **Telegram İskeleti:** Arayüz (BaseNotifier) ve konfigürasyon yapısı hazırlandı. Henüz gerçek HTTP çağrısı yapılmıyor (no-op mantığı var).
- [x] **Testler:** Config, guard, logging ve bootstrap için gerçek testler yazıldı.

## Bilinçli Olarak Ertelenenler
Bu fazda proje kapsamı dışında tutulan ve kasıtlı olarak uygulanmayan özellikler:
- Gerçek borsa (Binance) bağlantısı ve emir gönderimi.
- Websocket veya REST üzerinden piyasa verisi indirme/dinleme.
- Herhangi bir trading stratejisi (hareketli ortalamalar vb.) veya hesaplama mantığı.
- Veritabanı (SQLite) tablo şemaları ve veri yazma/okuma işlemleri.
- Telegram üzerinden mesaj göndermek için `requests` veya `httpx` kullanımı.

## Sonraki Faza (Phase 03) Hazırlık Durumu
Sistem şu an güvenle başlatılıp kapatılabilir, konfigürasyonu doğrulanabilir ve mantıksal çalışma profilleri uygulanabilir durumdadır. Bir sonraki fazda "Borsa Entegrasyonu ve Veri İndirme (Data Ingestion)" katmanı, bu sağlam altyapının üzerine inşa edilecektir.
