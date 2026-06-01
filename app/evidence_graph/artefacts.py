def create_assurance_artefact(assurance_record) -> dict:
    return {
        "artefact_type": "assurance_record",
        "id": assurance_record.assurance_obj.assurance_id,
        "relations": ["assured_by", "evidenced_by", "certified_under", "attested_by", "surveilled_by", "downgraded_by", "diverged_assurance_from"]
    }
