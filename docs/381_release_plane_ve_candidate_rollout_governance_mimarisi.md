# Phase 75: Release Plane ve Candidate Rollout Governance

Bu faz, trading platformunda "canlıya çıkacak şey" kavramını formalize eder.

## Neden Release Plane Gerekli?
Doğruluk sadece mantık katmanlarında değil, bu mantığın nasıl paketlendiğinde ve çıkarıldığında da bozulabilir.
- Adaylar (Candidates), Bundle'lar ve Compatibility kontrolleri.
- Rollout states (canary, probation, live).
- Geri alma (Rollback) ve Hotfix governansı.

Candidate ile Active Release aynı şey değildir. Hiçbir deploy "sessiz bir hotfix" veya "gizli mutasyon" olamaz.
