# Migration Integrity, Readiness, Activation ve Release Workflow Entegrasyonu Politikası

Bu politika, Migration Plane'in diğer sistem düzlemleriyle (Release, Activation, Workflow) nasıl entegre olacağını açıklar.

## Entegrasyon Noktaları
-   **Readiness Board:** Migration durumları `migration_integrity` domain'i altında değerlendirilir.
-   **Release Workflow:** Açık veya tamamlanmamış cutover borçları (debt) veya shim'ler yeni bir release'i engelleyebilir (blocker).
-   **Activation:** Migration doğrulama (verification) aşaması başarısız olursa, bir sonraki stage'e geçiş durdurulur.
