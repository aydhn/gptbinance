def build_assurance_integrity_pack(assurance_record) -> dict:
    return {
        "pack_name": "assurance_integrity_pack",
        "assurance_id": assurance_record.assurance_obj.assurance_id,
        "claims_count": sum(len(c.claims) for c in assurance_record.cases),
        "evidence_packs": sum(len(c.packs) for c in assurance_record.cases)
    }

ACCOUNTABILITY_PACKS = ['accountability integrity pack', 'subject/duty review pack', 'breach/sanction review pack', 'restitution/appeal review pack']


# Incentive Plane Evidence Packs
INCENTIVE_EVIDENCE_PACKS = [
    "incentive_integrity_pack",
    "subject_target_review_pack",
    "reward_penalty_review_pack",
    "conflict_gaming_review_pack"
]
