# Backup, Restore ve Disaster Recovery Politikası

## Backup Scope
- `CONFIG_ONLY`: Sadece configler
- `STATE_ONLY`: Sadece local state (sqlite vb.)
- `FULL`: Config + State
- Backup alınırken dosyaların Hash manifestosu üretilir.

## Restore Dry-Run
- Varsayılan restore davranışı her zaman `dry_run=True` şeklindedir.
- Zararlı olabilecek veya çalışan bir runtime'ı bozabilecek değişikliklerden kaçınmak için conflict tespiti yapılır.

## DR Rehearsal
- Disaster Recovery tatbikatı (rehearsal) düzenli aralıklarla simüle edilerek sistemin bozulmaya dayanıklılığı raporlanır.
- Rehearsal gerçek dosyaların üzerine yazmaz.
