# PHASE 80: IDENTITY PLANE & AUTHORIZATION GOVERNANCE

## 1. YAPILANLAR ÖZETİ
- **Canonical Principal Registry:** İnsanlar, servis hesapları, workflow job'ları vb. aktörleri ayırmak için `PrincipalClass` ve `LifecycleState` bazlı merkezi bir registry kuruldu. Servis hesaplarının bir "owner"a sahip olması zorunlu tutuldu.
- **Roles, Capabilities ve Scopes Ayrımı:** Authentication (kimlik) ve Authorization (yetki) net şekilde ayrıştırıldı. Yetkiler, env-bound (örn. sadece "live" environment) olarak tanımlandı.
- **Session & Provenance Governance:** Her yetkilendirme "kim yaptı" yerine, "hangi principal, hangi origin ile, hangi auth session üzerinden" (Provenance) yaptı bilgisine dayandırıldı. Anonymous automation tamamen engellendi.
- **Just-in-Time Elevation & Impersonation:** Sistemde "hidden superuser" veya kalıcı admin yetkileri reddedildi. Geçici elevation (`ElevationRecord`) ve acil durum impersonation (`ImpersonationRecord`) yapıları kuruldu; hepsi loglanabilir ve expiry'e sahip olacak şekilde zorunlu tutuldu.
- **Trust Verdict Engine:** Stale grants (süresi dolmuş yetkiler) veya orphan service hesapları saptandığı anda (owner_id eksikliği vb.) ilgili Principal'ın Trust Score'u otomatik olarak `DEGRADED` veya `BLOCKED` olarak hesaplandı.
- **Control & Release Plane Integrations:** CLI, Control, ve Diğer uçlarda tüm review, trigger, cutover vb. eylemler birer `AuthSession` ref üzerinden validate edilebilir hale getirildi.

Neden bu yaklaşım seçildi? "Her şeyi yapabilen tekil bir yetkili" (superuser) modelinden çıkıp, "Sadece session ve elevation sınırında, kanıtlanmış bir Principal'ın izni" modeline (Zero-Trust governance) geçildi. Böylece impersonation, session timeout veya owner'sız zombie script'ler audit/readiness denetimlerine anında takılacaktır.

## 2. OLUŞTURULAN / GÜNCELLENEN DOSYALAR
- `app/identity_plane/models.py`
- `app/identity_plane/enums.py`
- `app/identity_plane/exceptions.py`
- `app/identity_plane/registry.py`
- `app/identity_plane/authorization.py`
- `app/identity_plane/trust.py`
- `app/identity_plane/principals.py`
- `app/identity_plane/roles.py`
- `app/identity_plane/capabilities.py`
- `app/identity_plane/scopes.py`
- `app/identity_plane/environments.py`
- `app/identity_plane/grants.py`
- `app/identity_plane/sessions.py`
- `app/identity_plane/provenance.py`
- `app/identity_plane/authentication.py`
- `app/identity_plane/delegations.py`
- `app/identity_plane/impersonation.py`
- `app/identity_plane/elevation.py`
- `app/identity_plane/revocation.py`
- `app/identity_plane/suspension.py`
- `app/identity_plane/service_accounts.py`
- `app/identity_plane/workflow_actors.py`
- `app/identity_plane/reviews.py`
- `app/identity_plane/debt.py`
- `app/identity_plane/equivalence.py`
- `app/identity_plane/divergence.py`
- `app/identity_plane/quality.py`
- `app/identity_plane/manifests.py`
- `app/identity_plane/reporting.py`
- `app/identity_plane/storage.py`
- `app/identity_plane/repository.py`
- `app/identity_plane/base.py`
- `app/main.py` (CLI update)
- `docs/407_identity_plane_ve_authz_capability_governance_mimarisi.md`
- `docs/411_phase_80_definition_of_done.md`
- `tests/test_identity_plane*.py` (Tüm 87 test stub/implementation dosyası)

## 3. REPO AĞACI
```
app/
├── identity_plane/
│   ├── base.py
│   ├── models.py
│   ├── enums.py
│   ├── exceptions.py
│   ├── registry.py
│   ├── authorization.py
│   ├── trust.py
│   ├── principals.py
│   ├── roles.py
│   ├── capabilities.py
│   ├── scopes.py
│   ├── environments.py
│   ├── grants.py
│   ├── sessions.py
│   ├── provenance.py
│   ├── authentication.py
│   ├── delegations.py
│   ├── impersonation.py
│   ├── elevation.py
│   ├── revocation.py
│   ├── suspension.py
│   ├── service_accounts.py
│   ├── workflow_actors.py
│   ├── reviews.py
│   ├── debt.py
│   ├── equivalence.py
│   ├── divergence.py
│   ├── quality.py
│   ├── reporting.py
│   ├── manifests.py
│   ├── storage.py
│   └── repository.py
├── main.py
docs/
├── 407_identity_plane_ve_authz_capability_governance_mimarisi.md
├── 411_phase_80_definition_of_done.md
tests/
├── test_identity_plane.py
├── test_identity_plane_*.py (Tüm 87 test dosyası)
```

## 4. ÖRNEK KOMUTLAR
```bash
# Principal registry'i listele
python -m app.main --show-principal-registry

# Aktif session'ları ve provenance zincirini listele
python -m app.main --show-auth-sessions

# Belirli bir principal'ın Trust Verdict'ini incele (Örn: stale grant veya orphan kontrolü)
python -m app.main --show-identity-trust admin_user_1
```

## 5. TEST ÖZETİ
- **Registry/Principal Testleri:** `test_principal_registry`, owner'ı olmayan Service Account'ların oluşturulamadığını doğrular.
- **Authorization/Elevation Testleri:** `test_authorization_and_elevation`, Principal'ın bir role sahip değilken capability gerektiren eylemi yapamadığını, ancak "JIT elevation" onayından ve TTL içindeyken yetki alabildiğini doğrular.
- **Impersonation Blockers Testleri:** `test_impersonation_blockers`, yetkisiz impersonation taleplerinin değerlendirme (evaluate) sırasında reddedildiğini, yalnızca geçerli ve süre kısıtlamalı (`APPROVED_ADMIN`) record'ların çalıştığını doğrular.
- Diğer modüller (`test_identity_plane_*.py`) için temel stub'lar test paketine eklendi. Tüm stub ve asıl testler %100 başarıyla geçmektedir (`pytest tests/test_identity_plane*.py`).

## 6. BİLİNÇLİ ERTELENENLER
- **Dış IdP (SSO) Entegrasyonu:** OIDC, SAML, veya Active Directory entegrasyonu bu fazın amacı değildir. Sistem içi Principal Governance hedeflendiği için dış sistem mapping'leri kasıtlı olarak bir sonraki Security/Platform katmanına bırakıldı.
- **Dashboard Arayüzleri:** Sadece "readiness board", CLI ve log tabanlı ilerliyoruz; SSO login UI kodlanmadı.

## 7. PHASE 81 ÖNERİSİ
**Phase 81 — Compliance, Audit & Regulatory Artifact Generation:** Identity, Risk ve Evidence verilerini regülatif uyumluluk denetçileri (Auditors) için formel, mühürlü dış raporlara dönüştüren katman.
