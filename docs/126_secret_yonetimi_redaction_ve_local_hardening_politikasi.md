# Secret Yönetimi, Redaction ve Local Hardening Politikası

Bu belge sistemdeki sırların yönetimini, maskeleme (redaction) stratejisini ve lokal dosya izinleri hijyenini tanımlar.

## Sır Kaynakları (Secret Sources)
- Öncelikli olarak `env_var` (çevre değişkenleri) kullanılır.
- `.env` gibi dosyalar disk üzerinde bulunur ve güvenlik kontrolüne tabidir.
- Her secret bir referans (`SecretRef`) üzerinden taşınır, doğrudan değerler loglanmaz.

## Redaction Kuralları
- Sınıflandırılmış anahtarlar (`API_KEY`, `SECRET`, `PASSWORD` vb.) loglar, raporlar ve audit izlerinde otomatik olarak maskelenir (`***REDACTED***`).
- Nested JSON yapıları rekürsif olarak maskelenir.

## Local File Hygiene
- `.env` veya diğer config dosyalarının `077` (grup veya diğer kullanıcılar tarafından okunabilir/yazılabilir) izinleri güvenlik kontrolü aşamasında uyarılır (`FAIL` veya `WARN`).

## Sınırlar
Bu yapı tam teşekküllü bir KMS veya Vault çözümü değildir. Local-first ve sıfır bütçeli bağımsız bir sistem için tasarlanmıştır.
