# Migration Plane ve State Evolution Governance Mimarisi

## Amaç
Bu doküman, sistemdeki şema, yapılandırma, manifest ve çalışma zamanı durum (state) değişikliklerinin güvenli, geriye dönük izlenebilir ve audit edilebilir bir şekilde taşınmasını sağlayan mimariyi açıklar.

## Mimari Prensipler
1.  **Migrations -> Compatibility -> Prechecks -> Cutover -> Verification -> Debt Akışı:**
    Her göç (migration) işlemi bu adımlardan sırayla geçmelidir.
2.  **Dry-Run != Cutover:**
    Dry-run sadece simülasyon ve blast radius (etki alanı) analizi içindir. Gerçek taşıma işlemi her zaman açık ve izlenebilir bir cutover (kesin geçiş) kaydı gerektirir.
3.  **No Hidden Rewrite:**
    Geçmişe dönük veri veya manifest değişiklikleri sessizce (kayıt bırakmadan) yapılamaz.
4.  **No Permanent Shims:**
    Geçici uyumluluk sağlayan yapılar (shims), mutlaka bir TTL (yaşam süresi) ve temizlik planı ile oluşturulmalı, migration borcu (debt) olarak kaydedilmelidir.

## Dosya Yapısı
-   `registry.py`: Merkezi migration tanımları.
-   `transitions.py` ve `versions.py`: Sürüm ve taşıma sözleşmeleri (contracts).
-   `prechecks.py`, `dry_runs.py`, `cutovers.py`, `verification.py`: İşlem adımlarının yöneticileri.
