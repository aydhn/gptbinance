# State Integrity: Readiness, Release, Change, Activation, Migration Entegrasyonu Politikası

Bu politika, state plane'in diğer platformlarla nasıl entegre olacağını tanımlar.

## State Integrity Domain

State integrity, release, change, activation ve migration süreçleri için temel bir readiness (hazırlık) kriteridir.

## Entegrasyonlar

-   **Release Plane:** Release candidate'lerin state convergence'ı ve terminal preconditions'ı kontrol edilir.
-   **Change Plane:** Change execution'ların legal transition lineage'ı incelenir.
-   **Activation:** Stage progression'ın legal stage transitions ve effective-state convergence kurallarına uygunluğu denetlenir.
-   **Migration Plane:** Dual-run ve cutover aşamalarının legal transition prerequisites ile uyumu sağlanır.

## Policy Obligations

Yüksek riskli kararlar için state evidence obligations (durum kanıtı yükümlülükleri) üretilir. Eksik legal transition veya stale authoritative state, policy reddine neden olur.

## Evidence Graph ve Review Packs

State bütünlüğü, kanıt grafikleri (evidence graphs) ve review pack'ler aracılığıyla belgelenir.
