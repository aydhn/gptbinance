# Runtime Bootstrap ve Profilleri

Bu döküman, uygulamanın nasıl ayağa kalktığını, hangi profillerin desteklendiğini ve güvenlik kapılarının nasıl çalıştığını açıklar.

## Desteklenen Profiller

1. **DEV (`dev`)**
   - **Amaç:** Geliştirme ve lokal test ortamı.
   - **Davranış:** En esnek profildir. Eksik API anahtarlarına tolerans gösterebilir. Canlı işlem yapılamaz. Varsayılan profildir.

2. **PAPER (`paper`)**
   - **Amaç:** Gerçek veriyle sahte işlem (paper trading).
   - **Davranış:** Gerçek piyasa verisi okunur, ancak işlemler sanal olarak simüle edilir veya testnet'e gönderilir. Gerçek fon riski yoktur.

3. **TESTNET (`testnet`)**
   - **Amaç:** Borsa testnet ağlarında gerçek (ama testnet) emir gönderme.
   - **Davranış:** API anahtarları zorunludur ancak `use_testnet=True` olmalıdır.

4. **LIVE (`live`)**
   - **Amaç:** Gerçek fonlarla canlı piyasada işlem.
   - **Davranış:** En katı profildir. Çok katmanlı güvenlik kapılarından (Live Guard) geçmek zorundadır.

## Bootstrap Akışı

Uygulama `python -m app.main` ile başlatıldığında şu adımlar izlenir:

1. **CLI Argümanları Okunur:** `--profile`, `--check-only` vb. bayraklar işlenir.
2. **Dizinler Oluşturulur:** `storage/logs`, `storage/raw` gibi gerekli klasörler var edilir.
3. **Konfigürasyon Yüklenir:** Çevre değişkenleri (.env) ve varsayılanlar birleştirilir.
4. **Validasyon ve Güvenlik:**
   - Seçili profile göre temel kurallar doğrulanır (`validators.py`).
   - Eğer profil `live` ise, katı `Live Guard` devreye girer (`runtime_guards.py`).
5. **Run Context ve Logging:** Her çalışma için eşsiz bir `run_id` üretilir. Loglama sistemi, secret redaction (gizleme) filtresiyle birlikte kurulur.
6. **Başlangıç:** Hazırlıklar tamamsa uygulama ana akışına geçer veya `--check-only` modundaysa başarılı şekilde kapanır.

## Güvenlik Felsefesi
Sistem **Fail-Fast** prensibiyle çalışır. Herhangi bir konfigürasyon eksiği veya profil uyumsuzluğu, uygulamanın hatalı bir şekilde çalışmasına izin vermeden en başta (`bootstrap` aşamasında) durdurulur.
