# Fill, Latency, Slippage, Fee, Funding Assumption Politikası

Simülasyon düzlemi, gerçeğe yakın sonuçlar elde etmek ve "zero-friction fantasy" (sıfır sürtünme fantezisi) tuzaklarına düşmemek için katı varsayım politikaları uygular.

## 1. Fill Models
Touch fill, partial fill gibi modeller açıkça belirtilmelidir. Queue priority (kuyruk önceliği) göz ardı ediliyorsa bu bir caveat (uyarı) olarak eklenmelidir.

## 2. Latency Assumptions
Sıfır gecikme (zero-latency) varsayımı gerçek dışıdır ve engellenir. Karar ile emir iletimi arasındaki gecikme (decision_to_order_ms) tanımlanmalıdır.

## 3. Slippage Assumptions
Sabit (fixed bps) veya volatiliteye duyarlı slippage modelleri kullanılmalıdır. Sıfır slippage varsayımı yapılamaz.

## 4. Fee & Funding Assumptions
İşlem ücretleri (fees) ve vadeli işlemler için fonlama oranları (funding) simülasyona dahil edilmelidir. Eksikliği, beklenen getirilerin şişirilmesine yol açar.

## 5. Legality Assumptions
Borsa kısıtlamalarının (price, lot, notional filters) simülasyonda uygulanıp uygulanmadığı belirtilmelidir. Uygulanmaması durumunda uyarı üretilir.
