# Phase 21: Candidate Bundle Registry, Stage Geçişleri ve Lineage

Bu doküman aday paket (bundle) mantığını ve yaşam döngüsünü açıklar.

## Bundle (Paket) Nedir?
- Bir "Bundle", tüm strateji presetleri, model referansları, feature listeleri ve risk profillerinin değişmez (immutable) bir snapshot'ıdır.
- Versiyonludur (Major, Minor, Patch).

## Stage Geçişleri
- Candidate -> Reviewed -> Approved For Shadow/Paper/Testnet/Live_Caution -> Active -> Retired/Rejected.
- Bu yapı, hangi paketin canlıya geçmeye ne kadar hazır olduğunu yönetir.

## Lineage
- Her bundle bir ata (parent) referansına ve neden yaratıldığına (refresh_run_id) sahip olmalıdır. Bu, geriye dönük denetlenebilirliği garanti eder.
