# Paper Order Lifecycle ve Fill Varsayım Politikası

## Order Lifecycle
PaperOrder durumu `PaperOrderStatus` ile yönetilir:
- **CREATED:** Intent'ten yeni bir order oluşturuldu.
- **QUEUED:** Order book'a eklendi ve değerlendirme bekliyor.
- **ACCEPTED:** Sanal sistem order'ı kabul etti.
- **PARTIALLY_FILLED:** Henüz tam fill edilmedi.
- **FILLED:** Tamamen eşleşti ve position book'u güncelledi.
- **CANCELLED:** İptal edildi.
- **REJECTED:** Risk veya diğer kontroller sonucu reddedildi.
- **EXPIRED:** Belirtilen sürede işleme giremedi (TTL/Stale).

## Fill Varsayımları (Fill Simulator)
Canlı borsa orderbook'u taklit edilmediğinden fill varsayımları muhafazakar olmalıdır. `FillTrigger` kullanılır:
- **NEXT_TICK:** Bir sonraki fiyat güncellemesinde eşleştirme denenir.
- **NEXT_BAR:** Bir sonraki Kline kapanışında eşleştirme denenir.
- **IMMEDIATE:** Sadece test amaçlıdır; gerçekçilikten uzaktır.

## Kayma (Slippage) ve Komisyon (Fee)
- Fill price her zaman piyasa aleyhine "max_slippage_pct" oranında kaydırılır. (Buy için daha pahalı, Sell için daha ucuz).
- Her fill'de taker/maker komisyon oranları notional değere uygulanır ve equity'den düşülür.
Bu sayede paper trading sonucu her zaman "kötümser" hesaplanır; bu da canlıya geçildiğinde kötü sürprizleri azaltır.
