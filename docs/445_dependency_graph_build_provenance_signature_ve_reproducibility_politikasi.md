# Dependency, Build ve Reproducibility Politikası

- Dependency Trees tam ve acyclic olmalıdır.
- Build Recipes şeffaf ve tercihen deterministik (reproducible) olmalıdır.
- Provenance zinciri kopuk olamaz (Source -> Build -> Package -> Release).
- Tüm kritik artifact'lar imzalı olmalıdır (Signatures).
