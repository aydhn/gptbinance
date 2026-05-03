# Phase 35: Immutable Ledger & Balance Provenance

## Nedir?
Bu katman, sistemdeki asset hareketlerinin kaynaklarını, funding/fee kesintilerini ve double-entry muhasebe mantığını yönetir.

## Neden?
- Trade sistemlerinde PnL ve cüzdan bakiyeleri arasındaki uyumsuzlukları gidermek.
- Vergi ve raporlama için net cost basis, lot takibi (FIFO) sağlamak.
- Replay ve analitik katmanları için balance provenance oluşturmak.

## Sınırlar
- Bu bir ERP değildir.
- Vergi tavsiyesi vermez.
- Geçmişi sessizce değiştirmez; düzeltmeler yeni adjustment kayıtlarıyla atılır.
