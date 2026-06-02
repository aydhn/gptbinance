# Resilience and Completion Policy

- **Retries:** Retry storms engellenir, unbounded retries yasaktır.
- **Rollback & Compensation:** Rollback edilemeyen veya kompensasyon path'i olmayan high-risk execution başlatılamaz.
- **Verified Completion:** "Done", operation fully verified edilmeden claim edilemez. Falsely complete partiallar Orchestration Debt yazar.
