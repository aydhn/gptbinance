import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file("docs/579_remedy_plane_ve_cure_mitigation_containment_restitution_compensation_governance_mimarisi.md", """
# Remedy Plane Governance

## Neden Remedy Plane?
Fix !== Remedy.
Bir sorunu teknik olarak çözmek (rollback, patch), ortaya çıkan zararın (harm) geri alındığı (cure/restoration) veya telafi edildiği (compensation) anlamına gelmez.

## Akış
Harms -> Triggers -> Cure/Restoration/Compensation -> Residual/Recourse -> Trust

## Neden Rollback Theater Engellenmeli?
Rollback bir containment (sınırlama) eylemidir. Müşterinin yaşadığı kesintiyi gidermez veya eksik/bozuk verisini onarmaz. Rollback'i full cure gibi göstermek "Rollback Theater" olarak adlandırılır.
""")

write_file("docs/580_harm_breach_impact_cure_restoration_restitution_compensation_ve_residual_harm_politikasi.md", """
# Harms and Redress Policies

1. Harms
2. Breach Harms
3. Impacts
4. Cures
5. Restorations
6. Restitutions
7. Compensations
8. Residual Harms

Compensation (Ödünç/Tazminat) != Full Cure (Tam İyileştirme).
""")

write_file("docs/581_sufficiency_proportionality_timeliness_exhaustion_recourse_ve_under_remediation_politikasi.md", """
# Sufficiency and Proportionality

1. Sufficiency
2. Proportionality
3. Timeliness
4. Exhaustion
5. Recourse
6. Under-remediation

Completed action != adequate remedy.
""")

write_file("docs/582_remedy_integrity_readiness_commitment_finality_incident_contract_entegrasyonu_politikasi.md", """
# Integrations

1. Remedy Integrity Domain
2. Commitment, Finality, Incident, Contract, Compliance integrations.
""")

write_file("docs/583_phase_114_definition_of_done.md", """
# Definition of Done Phase 114

- Remedy plane framework implemented.
- Harm, cure, compensation, trust models in place.
- CLI created.
- Tests passing.
""")
