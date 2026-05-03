# State, Artifact, Secret Boundary ve Contamination Politikası

Farklı profiller arasında veri ve yapılandırma sızıntısını önlemek için her Profile kendi **ScopedPathSet**'ine sahiptir.

## Kapsamlar (Scoped Paths)
- Config, state, artifact, log, evidence, backup, metrik ve replay kök dizinleri her profil için tektir.

## Çapraz Kirlenme (Cross-Profile Contamination) Riski
- `ContaminationChecker` aktif olarak paylaşılan dizinleri tarar.
- `BoundaryChecker` live profillerin test dizinlerine, test profillerinin live dizinlerine erişmesini engeller (Blocker üretir).
