# Migration Plane / State Evolution Governance

Bu modül, sistemdeki şema, veri, manifesto ve durum (state) değişikliklerinin güvenli, geriye dönük izlenebilir ve denetlenebilir bir şekilde yönetilmesini sağlayan Migration Plane (Taşıma Düzlemi) yapısını içerir.

## Ana Prensipler
- **Migrations -> Compatibility -> Prechecks -> Cutover -> Verification -> Debt Akışı:** Her migration belirli bir yaşam döngüsünden geçer.
- **Dry-Run != Cutover:** Dry-run sadece potansiyel etkileri gösterir, asıl taşıma işlemi Cutover ile başlar.
- **No Hidden Rewrite:** Verilerde gizli, logsuz değişiklik yapılamaz. Her değişiklik kayıt altına alınmalıdır.
- **Migration Governance:** Süreçler otomatikleştirilmiş kurallarla (policy) denetlenir ve "compatibility shim" gibi geçici çözümlerin ne kadar süre kalacağı izlenir.

## Dosya Yapısı
- `models.py`: Pydantic modelleri.
- `enums.py`: Numaralandırmalar (Class tipleri).
- `exceptions.py`: Özel hata sınıfları.
- `registry.py`: Geçerli migration işlemlerinin merkezi kaydı.
- Ve diğer alt bileşenler (prechecks, dry_runs, vb.).
