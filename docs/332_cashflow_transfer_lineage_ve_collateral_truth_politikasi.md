# Cashflow, Transfer Lineage ve Collateral Truth Politikası

## Cashflows
Trade, funding, fee ve transfer işlemleri ayrı cashflow sınıflarına sahiptir. Yönleri (in/out) ve asset bilgileri typed olarak kaydedilir.

## Transfer Lineage
Internal transferler, cross-wallet hareketler "chain" olarak izlenir. Lineage olmadan hiçbir para hareketi geçerli sayılmaz, broken chain durumunda alert verilir.

## Collateral Truth
Collateral unusable/locked ve usable/cross/isolated gibi bucket'larda değerlendirilir.
Sistem kesinlikle explicit olmayan (implicit) capital hareketlerine izin vermez.
