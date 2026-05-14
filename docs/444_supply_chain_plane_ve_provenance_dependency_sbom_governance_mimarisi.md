# Supply Chain Plane & Provenance Governance

## Mantık
Sistem governance ne kadar güçlü olursa olsun, çalışan artifact'ın gerçekten hangi kaynaktan geldiği bilinmiyorsa kritik bir boşluk kalır. Version aynı görünebilir ama transitive dependencies değişmiş olabilir, SBOM eksik olabilir, generated code görünmez olabilir.

Bu katman `components -> dependencies -> build provenance -> packages/SBOM -> release/runtime lineage -> drift/exceptions/debt` zincirini canonical bir governance katmanı ile yönetir.

## Farklar
- Version != Digest != Provenance != Runtime Match
- Hidden generated artifact kabul edilemez
- SBOM freshness ve transitive risk göz ardı edilemez
