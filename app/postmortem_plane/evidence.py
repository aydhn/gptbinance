def export_postmortem_evidence(assurance_record) -> dict:
    return {
        "assurance_id": assurance_record.assurance_obj.assurance_id,
        "cases": [c.case_id for c in assurance_record.cases],
        "certifications": [c.certification_id for c in assurance_record.certifications]
    }

def get_postmortem_bundles_accountability():
    return {'refs': 'accountabilities, duties, breaches, sanctions'}
