# Ledger Plane ve Balance Truth Mimarisi

## Genel Bakış
Position truth ve PnL truth tek başına yeterli değildir. Asıl operasyonel hatalar cashflow ve balance truth kısmında gerçekleşir.
Sistem fills, fees, funding ve transfers hareketlerini typed ledger entry'lere çevirir, bunları reduce ederek cashflow ve balance statelerini oluşturur.

## Akış
`fills/pnl/transfers -> entries -> balances -> collateral -> equity`

## Kritik Ayrımlar
- **Balance != Available != Collateral**: Bunlar birbirinin yerine kullanılamaz. Gerçek accounting discipline için bunlar bucket'lara ayrılmalıdır.
- **No Opaque Treasury Truth**: Sistem hiçbir zaman "equity" adı altında tekil, opaque bir sayı üretmez, her zaman pnl/collateral adjust edilmiş alt bileşenlere sahip detaylı veri sağlar.

## Sınırlar
Bu faz custody/withdrawal motoru kurmaz. Tek başına venue balance'ı authoritative saymaz, ancak diverge olup olmadığını kanıtlayabilir.
