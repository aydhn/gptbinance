# Event Calendar Freshness, Timezone ve Source Health

Zaman, olay yönetiminde en kritik bileşendir.

## Timezone
Bütün olaylar UTC (timezone-aware) olarak kaydedilir ve yönetilir. Eski `datetime.utcnow()` fonksiyonu KESİNLİKLE kullanılmaz.

## Freshness & Source Health
Olay verilerinin güncelliği `freshness` alanı ile izlenir (FRESH/STALE). Kaynaklardan biri hata veriyorsa sağlık (health) durumu "down" veya "stale" olarak kaydedilir ve bu durum tüm operasyonlar için "CAUTION" üretebilir.
