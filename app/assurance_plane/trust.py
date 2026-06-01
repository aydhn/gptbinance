from app.assurance_plane.models import AssuranceTrustVerdict, AssuranceRecord
from app.assurance_plane.enums import TrustVerdict
from app.assurance_plane.quality import check_quality

def evaluate_trust(verdict_id: str, record: AssuranceRecord) -> AssuranceTrustVerdict:
    warnings = check_quality(record)
    verdict = TrustVerdict.TRUSTED

    if warnings:
        if "stale_certificate_warning" in "".join(warnings):
            verdict = TrustVerdict.DEGRADED
        elif "false_assurance_warning" in "".join(warnings):
            verdict = TrustVerdict.BLOCKED
        else:
            verdict = TrustVerdict.CAUTION

    breakdown = {
        "warnings": warnings,
        "cases_count": len(record.cases),
        "certifications_count": len(record.certifications),
        "surveillance_cycles_count": len(record.surveillance)
    }

    return AssuranceTrustVerdict(
        verdict_id=verdict_id,
        assurance_id=record.assurance_obj.assurance_id,
        verdict=verdict,
        breakdown=breakdown
    )
