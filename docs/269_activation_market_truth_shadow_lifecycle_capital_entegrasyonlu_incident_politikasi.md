# Bilesen Entegrasyonu ve Incident Politikasi

## Entegrasyon Noktalari
- **Market Truth**: Veri eskimis ise 'CRITICAL_INCIDENT' (stale) firlatir.
- **Shadow State**: Drift varsa 'MAJOR_INCIDENT' firlatir.
- **Order Lifecycle**: 'Unresolved' count hizla artiyorsa 'MAJOR_INCIDENT'.
- **Capital Governance**: Beklenmedik sermaye bloklanmalarinda incident uretir.

Tum bilesenler ayni incident framework'unu kullanarak birbirini ezer durumlar yaratmaktan kacinir.