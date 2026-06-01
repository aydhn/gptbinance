def build_assurance_integrity_pack(assurance_record) -> dict:
    return {
        "pack_name": "assurance_integrity_pack",
        "assurance_id": assurance_record.assurance_obj.assurance_id,
        "claims_count": sum(len(c.claims) for c in assurance_record.cases),
        "evidence_packs": sum(len(c.packs) for c in assurance_record.cases)
    }
