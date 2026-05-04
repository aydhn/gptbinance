# 208 Collateral Pressure Borrow Dependency Ve Liquidation Sensitivity Politikasi

## Collateral Dependency
Sistem, locked ve usable collateral oranını hesaplayarak collateral pressure summary üretir. Basınç eşik değerleri aştığında overlay engine REDUCE kararı çıkarır.

## Borrow Burden
Spot veya Margin borçları `BorrowAnalyzer` üzerinden izlenir. Aşırı bağımlılık (ELEVATED) durumunda CAUTION veya BLOCK verilir.

## Liquidation Sensitivity
Çapraz defter likidasyon riski SAFE, ELEVATED, DANGEROUS olarak işaretlenir.
