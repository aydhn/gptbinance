# Identity Plane & Authorization Capability Governance

## Vizyon
Sistemde "kimin ne yaptığı" sadece bir log satırı değil; kanıtlanabilir, denetlenebilir ve yönetilebilir bir Truth (Gerçeklik) olmalıdır. Authentication (kimlik doğrulama) ile Authorization (yetkilendirme) kesin olarak ayrılmıştır.

## Temel Kurallar
1. **Hidden Impersonation Yoktur:** Her impersonation veya JIT elevation (Just-in-Time privilege escalation) kayıt altına alınır, `approved_by` ve `expires_at` değerleri taşır.
2. **Orphan Service Account Yoktur:** Tüm servis hesapları bir Human Owner'a bağlanmak zorundadır. Owner'sız hesaplar doğrudan BLOCKED verdict alır.
3. **Stale Session/Grant Tolerance Yoktur:** Süresi dolmuş yetkiler (grants) veya session'lar otomatik olarak Trust Verdict'i DEGRADED yapar.
4. **Explicit Actor Provenance:** Kontrol düzlemindeki onaylar ve eylemler string isimlerle değil, `AuthSession` ID'leri ve `PrincipalRef` objeleriyle mühürlenir.
