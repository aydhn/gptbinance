# Phase 07: Hypothesis Strateji Aileleri ve Sınırlar

Bu fazda, sadece niyet üreten (intent-generating), kural tabanlı strateji hipotez sınıfları oluşturulur.

## Trend Follow (Trend Takibi)
- **Amaç:** Mevcut trendin devamı hipotezi.
- **Kullanımı:** Eğim (slope), MA ilişkisi, volatility gate, structure confirmation.
- **Sınırlar:** Yalnızca Entry/Exit intent candidate üretir. Pozisyon açmaz.

## Mean Reversion (Ortalamaya Dönüş)
- **Amaç:** Fiyattaki aşırılık (stretch) sonrası geri dönüş hipotezi.
- **Kullanımı:** Osilatörler (RSI vb.), fiyatın ortalamadan uzaklaşması, revert tendency.
- **Sınırlar:** Yalnızca intent üretir, execution yapmaz.

## Breakout (Kırılım)
- **Amaç:** Range kırılımı ve volatility expansion (genişleme) mantığı.
- **Kullanımı:** Belirli seviyelerin kırılması ve hacim/momentum onayı (false breakout azaltıcı).
- **Sınırlar:** Kural bazlı niyet üretimi.

## Structure / Divergence (Yapı / Uyumsuzluk)
- **Amaç:** Piyasa yapısı (pivotlar) ve göstergeler (osilatörler) arası uyumsuzluk yakalama.
- **Kullanımı:** Pattern tabanlı intent onayı.
- **Sınırlar:** Saf bir analiz ve niyet onayı üretir.

## Neden Bunlar Henüz Execution-Ready Değil?
Bu sınıflar (families), karar motorunun (framework) çalışmasını test eden hipotezlerdir. Hiçbiri risk katmanının süzgecinden geçmiş bir pozisyon yönetimi içermediğinden doğrudan "live trade" yeteneğine sahip değildir.
