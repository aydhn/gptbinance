# Supply Chain Integrity & Trusted Build Governance

Bu katman sistemin "çalıştırdığımız kodun gerçekten inşa ettiğimiz kod olduğundan emin olmasını" sağlar.
Otomatik deploy yapmaz, sadece provenance (köken) zincirini kurar ve doğrular.

## Neden?
- Source -> Deps -> Build -> Release -> Activation -> Runtime zinciri kopuksa karar mantığı güvenilmezdir.
- Dependency kaymaları, lockfile drift, hash mismatch riskleri önlenmelidir.
- Sadece provenance, attestation ve reproducibility check olan build'ler trusted sayılabilir.

## Sınırlar
- Paid CI/CD servisi kurmaz.
- Historical artefact'ları mutate etmez (immutable registry).
- Unattested build'leri silently pass yapmaz.
