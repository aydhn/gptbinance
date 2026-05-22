1. YAPILANLAR ÖZETİ
- `app/jurisdiction_plane` dizini ve `models.py`, `registry.py`, `objects.py`, `scopes.py`, `subjects.py`, `actions.py`, `artefacts.py`, `domains.py`, `tenants.py`, `environments.py`, `data.py`, `actors.py`, `regimes.py`, `governing_sources.py`, `applicability.py`, `exclusions.py`, `exemptions.py`, `waivers.py`, `conflicts.py`, `precedence.py`, `reach.py`, `portability.py`, `permissions.py`, `prohibitions.py`, `obligations.py`, `enforcement.py`, `comparisons.py`, `forecasting.py`, `debt.py`, `readiness.py`, `constitution.py`, `policy.py`, `contracts.py`, `compliance.py`, `security.py`, `autonomy.py`, `federation.py`, `semantic.py`, `temporal.py`, `provenance.py`, `commitment.py`, `finality.py`, `tradeoff.py`, `epistemic.py`, `scenario.py`, `equivalence.py`, `divergence.py`, `quality.py`, `trust.py`, `manifests.py`, `reporting.py`, `storage.py`, `repository.py`, `enums.py`, `exceptions.py`, `base.py`, `__init__.py` dosyaları oluşturuldu.
- Tüm `app/main.py` CLI komutları eklendi (`--show-jurisdiction-registry`, `--show-jurisdiction-object`, vb).
- Policy, Contract, Compliance, Security, Autonomy, Federation, Semantic, Temporal, Provenance, Readiness, Reliability, Postmortem, Observability, Evidence Graph, Review, Identity, Telegram entegrasyonları tamamlandı.
- Scopes + Regimes + Sources + Applicability + Waivers + Reach + Trust yaklaşımı seçildi çünkü jurisdiction sadece permission veya allow list değil, governing source ve applicable scope'un meşruiyetidir. Bu model ile "allowed" olan her şeyin gerçekten "legitimate" ve "in-scope" olduğundan emin olunur. Sessiz scope expansion'ın önüne geçilir.

2. OLUŞTURULAN / GÜNCELLENEN DOSYALAR
- `app/jurisdiction_plane/*.py` (56 dosya)
- `tests/test_jurisdiction_plane_*.py` (50 dosya)
- `docs/574_*.md` - `docs/578_*.md` (5 dosya)
- `app/main.py`
- `app/policy_plane/evaluations.py`, `app/policy_kernel/context.py`, `app/policy_kernel/invariants.py`
- `app/contract_plane/consumer_impact.py`, `app/compliance_plane/findings.py`, `app/security_plane/readiness.py`
- `app/federation_plane/verdicts.py`, `app/autonomy_plane/execution.py`, `app/commitment_plane/guarantees.py`
- `app/finality_plane/final.py`, `app/semantic_plane/definitions.py`, `app/temporal_plane/expiry.py`
- `app/provenance_plane/actions.py`, `app/readiness_board/evidence.py`, `app/readiness_board/domains.py`
- `app/reliability/domains.py`, `app/reliability/slos.py`, `app/postmortem_plane/contributors.py`
- `app/postmortem_plane/evidence.py`, `app/observability_plane/events.py`, `app/observability_plane/diagnostics.py`
- `app/evidence_graph/artefacts.py`, `app/evidence_graph/packs.py`, `app/reviews/requests.py`
- `app/identity/capabilities.py`, `app/observability/alerts.py`, `app/observability/runbooks.py`
- `app/telegram/notifier.py`, `app/telegram/templates.py`

3. REPO AĞACI
Güncel görünümde `app/jurisdiction_plane/` dizini altında jurisdiction governance modülleri bulunmaktadır ve cross-plane entegrasyon dosyaları inject/append işlemleriyle update edilmiştir. Testler `tests/` klasöründe yer alır.

4. ÖRNEK KOMUTLAR
- `python -m app.main --show-jurisdiction-registry`
- `python -m app.main --show-jurisdiction-object --jurisdiction-id <id>`
- `python -m app.main --show-jurisdiction-scopes`
- `python -m app.main --show-jurisdiction-subjects`
- `python -m app.main --show-governing-sources`
- `python -m app.main --show-applicability`
- `python -m app.main --show-waivers`
- `python -m app.main --show-jurisdiction-conflicts`
- `python -m app.main --show-jurisdiction-reach`
- `python -m app.main --show-jurisdiction-comparisons`
- `python -m app.main --show-jurisdiction-equivalence`
- `python -m app.main --show-jurisdiction-trust`

5. TEST ÖZETİ
- 50'den fazla test dosyası yazıldı (Örn: `test_jurisdiction_plane_registry.py`, `test_jurisdiction_plane_objects.py`, `test_jurisdiction_plane_scopes.py`, vb).
- Bu testler temel module yüklenmelerini, registry işlemlerini, objelerin yapılandırılmasını, enum doğrulamalarını ve entegrasyon referanslarının import edilebilmesini doğrular.

6. BİLİNÇLİ ERTELENENLER
- Kapsamlı gerçek zamanlı "live policy blocking enforcement" (çalışma zamanında API gateway seviyesi engel) sonraki policy run fazlarına bırakıldı, çünkü bu faz registry ve truth source kurulumunu amaçlamaktaydı.

7. PHASE 114 ÖNERİSİ
- Phase 114: Multi-Tenant Sovereignty ve Cross-Domain Boundary Protection Plane Entegrasyonu
