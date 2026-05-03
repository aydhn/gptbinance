# 192. Exchange Filters, Tick/Step/Min Notional ve Tradability Politikası

Bir sembolün trade edilebilir olması için borsanın belirlediği filtrelere tam uyum sağlaması zorunludur.

## Filter Metadata ve Validation
Sistem her siparişi veya strateji hesabını göndermeden önce şu filtreleri doğrular:
- **Tick Size**: Fiyatın geçerli bir adımla yuvarlandığını doğrular.
- **Step Size**: Miktarın geçerli bir adımla yuvarlandığını doğrular.
- **Min Notional**: İşlem hacminin minimum gereksinimi karşıladığını doğrular.

## Missing Filters ve Tradability
Bir sembol için gerekli filtre bilgileri eksikse veya okunamıyorsa, o sembolün trade edilebilirliği (Tradability) güvenilir değildir. Bu tür semboller otomatik olarak engellenir (Blocked) veya dikkatli yaklaşım (Caution) ile işaretlenir.

## Tradability Gating
Tradability sınıflandırması, filtre geçerliliği, sembol durumu (status) ve piyasa likiditesi/spread verilerinin birleşimiyle hesaplanır. Yalnızca eksiksiz filtre bilgisine sahip, durumu "TRADING" olan semboller Tradability değerlendirmesinden geçebilir.
