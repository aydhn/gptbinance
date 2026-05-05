# Migration Fabric ve State Evolution Constitution Politikası

Migration Fabric, platformun config, state, schema ve policy yüzeylerinin evrimini disiplin altına alır. Ad-hoc script'lerle yapılan gizli/sessiz değişiklikleri kesin olarak yasaklar.

## Neden Ad-Hoc Scripts Yasak?
- Denetlenebilirlik (Auditability) eksikliği.
- Dependency ve Compatibility sorunları.
- Hatalarda Rollback zorluğu ve Stale Evidence riski.

## Dry-Run Zorunluluğu
Hiçbir migration, potansiyel etkileri bir dry-run simülasyonunda görülmeden üretimde veya kritik state üzerinde apply edilemez.
