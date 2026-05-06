# Lock Integrity, Dependency Lineage and Reproducibility

## Lock Integrity
Dependency snapshot'lar içindeki lockfile verileri, beklenen/committed lock hash ile karşılaştırılır. Drift varsa lock integrity bozulur ve artifact verdict "degraded" seviyesine inebilir.

## Reproducibility
İki build çıktısı (manifest) compare edilir. Hash aynıysa "deterministic", değilse "non-deterministic" sayılır. Deterministik olmayan build'ler "caution" uyarılarına neden olur.
