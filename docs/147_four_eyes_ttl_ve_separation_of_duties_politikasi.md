# Four-Eyes, TTL ve Separation of Duties Politikası

## Dual Approval (Four-Eyes)
Kritik aksiyonlar (`START_LIVE_SESSION`, `FLATTEN_LIVE_SESSION`, `APPLY_UPGRADE` vb.) her zaman en az iki farklı yetkilinin onayını gerektirir. Bu, tek bir kişinin hesabı ele geçirilse veya hata yapsa bile felaketi önlemek içindir.

## Self-Approval Blokları
Talebi oluşturan (requester) operatör, kendi oluşturduğu talebi asla onaylayamaz. Policy motoru bu durumu açıkça tespit eder ve yetkilendirmeyi düşürür.

## Approval TTL (Time-to-Live)
Hiçbir onay sonsuza kadar geçerli kalamaz. Aksiyonun kritiklik seviyesine göre (örn. CRITICAL için 30 dakika, HIGH için 1 saat) bir TTL süresi atanır.

## Stale Approvals
Süresi dolan (`EXPIRED`) veya hedeflenen `run_id` / `bundle_id` gibi bağlamları değişen onaylar "stale" (bayat) kabul edilir ve authorization motoru tarafından Execution zamanında reddedilir (`DENIED`). Sistemin güncel tutulması için yeni bir request açılması zorunludur.

## Role Separation Mantığı
Aksiyonlar, sadece işlevle ilgili roller tarafından onaylanabilir:
- Upgrade işlemleri `RELEASE` ve `OPS` onayını gerektirir.
- Restore işlemleri `SECURITY` ve `OPS` onayını gerektirir.
- Flatten işlemleri `RISK` ve `OPS` onayını gerektirir.
Bu ayrım, tek bir alanın (örneğin sadece Developer/Release ekibinin) riski ve opsiyonları göz ardı ederek canlı sistemi değiştirmesini engeller.
