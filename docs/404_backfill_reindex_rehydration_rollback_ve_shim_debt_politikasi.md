# Backfill, Reindex, Rehydration, Rollback ve Shim Debt Politikası

Migration işlemlerinin yan etkilerinin yönetimi bu politikanın konusudur.

## Süreçler
-   **Backfill:** Geriye dönük veri doldurma işlemleri `BackfillExecutionRecord` ile kaydedilir. Silent historical rewrite (gizli geçmiş değişimi) kesinlikle yasaktır.
-   **Reindex:** Veritabanı veya state indekslerinin yeniden oluşturulması `ReindexExecutionRecord` ile tutulur.
-   **Rehydration:** Ön bellek (cache) veya türetilmiş verilerin yeniden üretimi `RehydrationRecord` kullanılarak izlenir.
-   **Rollback / Fallback:** Her geri dönüşüm veya degrade mod planlı ve `RollbackMigrationRecord` ile kayıtlı olmalıdır.
-   **Shim Debt:** Uyumluluk katmanları `CompatibilityShim` ve `MigrationDebtRecord` nesneleri kullanılarak takip edilir; zaman aşımına (TTL) tabidirler.
