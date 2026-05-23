import pytest
from datetime import datetime
from app.interpretation_plane.registry import CanonicalInterpretationRegistry
from app.interpretation_plane.models import (
    InterpretationObject, TextRecord, AmbiguityRecord, ReadingRecord,
    CanonicalMeaningRecord, ClarificationRecord,
    TextUnitClass, InterpretationClass, AmbiguityClass, ReadingClass, ClarificationClass
)
from app.interpretation_plane.exceptions import (
    AmbiguityLaunderingViolation, BeneficiaryErasingConstructionViolation
)
from app.interpretation_plane.ambiguities import resolve_ambiguity
from app.interpretation_plane.beneficiary_safe import enforce_beneficiary_safety

def test_registry_registration():
    registry = CanonicalInterpretationRegistry()
    obj = InterpretationObject("i_01", InterpretationClass.POLICY_RULE)
    registry.register(obj)
    assert registry.get("i_01") is not None

def test_ambiguity_laundering_prevention():
    obj = InterpretationObject("i_02", InterpretationClass.CONTRACT_CLAUSE)
    obj.ambiguities["amb_1"] = AmbiguityRecord("amb_1", "txt_1", AmbiguityClass.SCOPE, "Unclear scope")
    canon = CanonicalMeaningRecord("can_1", "txt_1", "read_1", "Narrow meaning", datetime.now())

    with pytest.raises(AmbiguityLaunderingViolation):
        resolve_ambiguity(obj, "amb_1", canon)

    obj.clarifications["clar_1"] = ClarificationRecord("clar_1", "amb_1", ClarificationClass.SCOPE, "Narrow scope confirmed")
    resolve_ambiguity(obj, "amb_1", canon)
    assert obj.ambiguities["amb_1"].is_resolved

def test_beneficiary_erasing_prevention():
    obj = InterpretationObject("i_03", InterpretationClass.RIGHTS_TEXT)
    safe_reading = ReadingRecord("r_safe", "txt_1", ReadingClass.EXPANSIVE, "Broad rights", "context", is_beneficiary_safe=True)
    unsafe_reading = ReadingRecord("r_unsafe", "txt_1", ReadingClass.RESTRICTIVE, "No rights", "context", is_beneficiary_safe=False)

    obj.readings["r_safe"] = safe_reading
    obj.readings["r_unsafe"] = unsafe_reading

    with pytest.raises(BeneficiaryErasingConstructionViolation):
        enforce_beneficiary_safety(obj, unsafe_reading)

def test_trust_verdict():
    obj = InterpretationObject("i_04", InterpretationClass.LIABILITY_CLAUSE)
    obj.ambiguities["amb_1"] = AmbiguityRecord("amb_1", "txt_1", AmbiguityClass.TEXTUAL, "Unclear liability limit")

    report = obj.get_trust_report()
    assert report.verdict.name == 'BLOCKED'
    assert "Unresolved Material Ambiguity" in report.blockers
