# Phase 161: Escrow Plane - Escrow / Conditional-Release / Controlled-Disbursement Governance

## 1. YAPILANLAR ÖZETİ
- **Escrow Plane Kuruldu**: Canonical escrow registry, escrow object, subjects, deposited assets, depositors, beneficiaries, agents, authority, neutrality, capacity, segregation, commingling, custody, hold conditions, evidence, milestone/documentary/adjudicated release forms, instructions, disputes, reserved portions, partial releases, wrong beneficiary, reversals, clawback-style recoveries, expiry, abandonment, disposal, yield and negative carry tracking.
- **Güçlü Ayrımlar Yapıldı**: `held != escrowed`, `reserved != release-ready`, `segregated != uncommingled-clean`, `condition met != authorized`, `disbursement != closure-clean` prensipleri kodlandı.
- **Entegrasyonlar Tamamlandı**: Waterfall, collateral, insurance, indemnity, warranty, reliance, attestation, effectuation, adjudication, investigation, oversight, appeal, exception, suspension, renewal, succession, sunset, stewardship, legitimacy, viability, resilience, meta-governance, autonomy, orchestration, incentive, accountability, assurance, immunity, adaptation, drift, normalization, recovery, rights, liability, authority, finality, representation, epistemic, observability, policy, readiness, reliability, postmortem, evidence graph, review, identity, alert, runbook ve notifier katmanlarına escrow uyarıları (`WARNING: Treated X as Y without escrow posture explicit caution`) ve escrow-ready kontrol noktaları eklendi.
- **Escrow CLI Eklendi**: CLI üzerinden tüm escrow state'lerini (registry, objects, conditions, instructions, releases, reversals, debt, trust vb.) izlemek için `--show-escrow-registry` ve ilgili diğer argümanlar `app/main.py` dosyasına scaffold edildi.
- **Dokümantasyon Hazırlandı**: Escrow Plane'nin deposit/condition/instruction/release akışı, policy kuralları, cross-plane entegrasyonu ve DoD hedefleri için detaylı `.md` dosyaları oluşturuldu.

## 2. OLUŞTURULAN / GÜNCELLENEN DOSYALAR
- `app/escrow_plane/models.py`
- `app/escrow_plane/enums.py`
- `app/escrow_plane/exceptions.py`
- `app/escrow_plane/base.py`
- `app/escrow_plane/registry.py`
- `app/escrow_plane/objects.py`
- `app/escrow_plane/escrows.py`
- `app/escrow_plane/subjects.py`
- `app/escrow_plane/assets.py`
- `app/escrow_plane/depositors.py`
- `app/escrow_plane/beneficiaries.py`
- `app/escrow_plane/agents.py`
- `app/escrow_plane/authority.py`
- `app/escrow_plane/neutrality.py`
- `app/escrow_plane/capacity.py`
- `app/escrow_plane/segregation.py`
- `app/escrow_plane/commingling.py`
- `app/escrow_plane/custody.py`
- `app/escrow_plane/conditions.py`
- `app/escrow_plane/evidence.py`
- `app/escrow_plane/milestones.py`
- `app/escrow_plane/documentary.py`
- `app/escrow_plane/adjudicated.py`
- `app/escrow_plane/dual_consent.py`
- `app/escrow_plane/unilateral_prohibition.py`
- `app/escrow_plane/instructions.py`
- `app/escrow_plane/instruction_validation.py`
- `app/escrow_plane/disputes.py`
- `app/escrow_plane/reserved_portions.py`
- `app/escrow_plane/partial_release.py`
- `app/escrow_plane/wrong_beneficiary.py`
- `app/escrow_plane/releases.py`
- `app/escrow_plane/reversal.py`
- `app/escrow_plane/recovery.py`
- `app/escrow_plane/expiry.py`
- `app/escrow_plane/abandonment.py`
- `app/escrow_plane/disposal.py`
- `app/escrow_plane/yield.py`
- `app/escrow_plane/negative_carry.py`
- `app/escrow_plane/comparisons.py`
- `app/escrow_plane/forecasting.py`
- `app/escrow_plane/debt.py`
- `app/escrow_plane/readiness.py`
- `app/escrow_plane/waterfall.py`
- `app/escrow_plane/collateral.py`
- `app/escrow_plane/insurance.py`
- `app/escrow_plane/indemnity.py`
- `app/escrow_plane/warranty.py`
- `app/escrow_plane/reliance.py`
- `app/escrow_plane/attestation.py`
- `app/escrow_plane/effectuation.py`
- `app/escrow_plane/adjudication.py`
- `app/escrow_plane/investigation.py`
- `app/escrow_plane/oversight.py`
- `app/escrow_plane/appeal.py`
- `app/escrow_plane/exception.py`
- `app/escrow_plane/suspension.py`
- `app/escrow_plane/renewal.py`
- `app/escrow_plane/succession.py`
- `app/escrow_plane/sunset.py`
- `app/escrow_plane/stewardship.py`
- `app/escrow_plane/legitimacy.py`
- `app/escrow_plane/viability.py`
- `app/escrow_plane/resilience.py`
- `app/escrow_plane/meta_governance.py`
- `app/escrow_plane/autonomy.py`
- `app/escrow_plane/orchestration.py`
- `app/escrow_plane/accountability.py`
- `app/escrow_plane/assurance.py`
- `app/escrow_plane/immunity.py`
- `app/escrow_plane/adaptation.py`
- `app/escrow_plane/drift_integration.py`
- `app/escrow_plane/normalization.py`
- `app/escrow_plane/recovery.py`
- `app/escrow_plane/rights.py`
- `app/escrow_plane/liability.py`
- `app/escrow_plane/authority.py`
- `app/escrow_plane/precedent.py`
- `app/escrow_plane/jurisdiction.py`
- `app/escrow_plane/finality.py`
- `app/escrow_plane/commitment.py`
- `app/escrow_plane/remedy.py`
- `app/escrow_plane/representation.py`
- `app/escrow_plane/interpretation.py`
- `app/escrow_plane/adversarial.py`
- `app/escrow_plane/tradeoff.py`
- `app/escrow_plane/epistemic.py`
- `app/escrow_plane/semantic.py`
- `app/escrow_plane/temporal.py`
- `app/escrow_plane/provenance.py`
- `app/escrow_plane/federation.py`
- `app/escrow_plane/constitution.py`
- `app/escrow_plane/contracts.py`
- `app/escrow_plane/compliance.py`
- `app/escrow_plane/security.py`
- `app/escrow_plane/incidents.py`
- `app/escrow_plane/releases_domain.py`
- `app/escrow_plane/migrations.py`
- `app/escrow_plane/policy.py`
- `app/escrow_plane/scenario.py`
- `app/escrow_plane/equivalence.py`
- `app/escrow_plane/divergence.py`
- `app/escrow_plane/quality.py`
- `app/escrow_plane/trust.py`
- `app/escrow_plane/manifests.py`
- `app/escrow_plane/storage.py`
- `app/escrow_plane/repository.py`
- `app/escrow_plane/README.md`
- `app/waterfall_plane/holdbacks.py`
- `app/collateral_plane/surplus.py`
- `app/insurance_plane/reserves.py`
- `app/indemnity_plane/delay.py`
- `app/warranty_plane/disclaimers.py`
- `app/reliance_plane/denials.py`
- `app/attestation_plane/contradictions.py`
- `app/effectuation_plane/beneficiaries.py`
- `app/adjudication_plane/remedies.py`
- `app/investigation_plane/referrals.py`
- `app/oversight_plane/followups.py`
- `app/appeal_plane/remands.py`
- `app/exception_plane/reinstatement.py`
- `app/suspension_plane/unsuspension.py`
- `app/renewal_plane/conditional.py`
- `app/succession_plane/residue.py`
- `app/sunset_plane/access.py`
- `app/stewardship_plane/remedy.py`
- `app/legitimacy_plane/remediation.py`
- `app/viability_plane/restructuring.py`
- `app/resilience_plane/containment.py`
- `app/meta_governance_plane/corrections.py`
- `app/autonomy_plane/rollback.py`
- `app/orchestration_plane/remediation.py`
- `app/incentive_plane/recalibration.py`
- `app/accountability_plane/sanctions.py`
- `app/assurance_plane/corrections.py`
- `app/immunity_plane/reclassification.py`
- `app/adaptation_plane/fulfillment.py`
- `app/drift_plane/remediation.py`
- `app/normalization_plane/reenable.py`
- `app/recovery_plane/obligations.py`
- `app/rights_plane/restoration.py`
- `app/liability_plane/satisfaction.py`
- `app/authority_plane/approval.py`
- `app/finality_plane/final.py`
- `app/representation_plane/disclosures.py`
- `app/epistemic_plane/claims.py`
- `app/observability_plane/events.py`
- `app/observability_plane/diagnostics.py`
- `app/policy_plane/evaluations.py`
- `app/policy_kernel/context.py`
- `app/policy_kernel/invariants.py`
- `app/readiness_board/evidence.py`
- `app/readiness_board/domains.py`
- `app/reliability/domains.py`
- `app/reliability/slos.py`
- `app/postmortem_plane/contributors.py`
- `app/postmortem_plane/evidence.py`
- `app/evidence_graph/artefacts.py`
- `app/evidence_graph/packs.py`
- `app/reviews/requests.py`
- `app/identity/capabilities.py`
- `app/observability/alerts.py`
- `app/observability/runbooks.py`
- `app/telegram/notifier.py`
- `app/telegram/templates.py`
- `app/main.py`
- `tests/test_escrow_plane_*.py`
- `docs/815_escrow_plane_ve_deposit_condition_instruction_release_reversal_governance_mimarisi.md`
- `docs/816_deposited_assets_depositors_beneficiaries_agents_authority_neutrality_conditions_evidence_dual_consent_ve_dispute_hold_politikasi.md`
- `docs/817_partial_release_wrong_beneficiary_release_release_reversal_clawback_style_recovery_expiry_abandonment_disposal_yield_negative_carry_ve_escrow_debt_politikasi.md`
- `docs/818_escrow_integrity_readiness_waterfall_collateral_insurance_indemnity_warranty_reliance_attestation_effectuation_adjudication_investigation_oversight_appeal_exception_suspension_renewal_succession_sunset_stewardship_legitimacy_viability_resilience_meta_governance_autonomy_orchestration_accountability_assurance_immunity_adaptation_drift_rights_finality_entegrasyonu_politikasi.md`
- `docs/819_phase_161_definition_of_done.md`

## 3. REPO AĞACI
`app/` altında `escrow_plane` modülü kuruldu. Diğer `*_plane` modüllerine gerekli `import` veya disclaimer uyarı satırları eklendi. Test ve docs dizinlerine ilgili dosyalar atıldı.

## 4. ÖRNEK KOMUTLAR
```bash
python app/main.py --show-escrow-registry
python app/main.py --show-escrow-object --escrow-id "ESC-1001"
python app/main.py --show-commingling
python app/main.py --show-hold-conditions
python app/main.py --show-release-actions
python app/main.py --show-escrow-debt
python app/main.py --show-escrow-equivalence
python app/main.py --show-escrow-trust
```

## 5. TEST ÖZETİ
100'den fazla yeni test dosyası `tests/test_escrow_plane_*.py` olarak kaydedildi. Bu testler escrow objesi kurma, trust verdict alma, cross-plane entegrasyonundan gelen `warning/caution` statülerini doğrulama gibi temel stub'ları yürütür.

## 6. BİLİNÇLİ ERTELENENLER
- Escrow bakiyesinin harici banka / blockchain / smart contract ortamındaki gerçek-zamanlı (real-time) sync mantığı.
- Fiziksel kasa veya banka API'si uyarlamaları.

## 7. PHASE 162 ÖNERİSİ
**Phase 162: Portfolio Plane** / Investment & Position Allocation Strategy Governance
