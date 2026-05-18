from app.constitution_plane.models import DomainVerdictRecord, PrecedenceRecord
from app.constitution_plane.enums import VerdictClass, TrustVerdict
from app.constitution_plane.final_verdicts import FinalVerdictSynthesizer
from app.constitution_plane.trust import TrustedConstitutionVerdictEngine

def test_no_majority_green_theater():
    synthesizer = FinalVerdictSynthesizer()
    verdicts = [
        DomainVerdictRecord(verdict_id="1", domain="release", verdict=VerdictClass.PASS, evidence_refs=[]),
        DomainVerdictRecord(verdict_id="2", domain="state", verdict=VerdictClass.PASS, evidence_refs=[]),
        DomainVerdictRecord(verdict_id="3", domain="security", verdict=VerdictClass.BLOCKED, evidence_refs=[]), # Hard veto
    ]

    result = synthesizer.synthesize("obj_1", verdicts, [])
    # Should be BLOCKED despite majority PASS
    assert result.final_verdict == VerdictClass.BLOCKED
    assert "security" in result.active_vetoes

def test_compound_risk_accumulation():
    synthesizer = FinalVerdictSynthesizer()
    verdicts = [
        DomainVerdictRecord(verdict_id="4", domain="release", verdict=VerdictClass.PASS_WITH_CAUTION, evidence_refs=[]),
        DomainVerdictRecord(verdict_id="5", domain="contract", verdict=VerdictClass.PASS_WITH_CAUTION, evidence_refs=[]),
        DomainVerdictRecord(verdict_id="6", domain="assurance", verdict=VerdictClass.PASS_WITH_CAUTION, evidence_refs=[]),
    ]

    result = synthesizer.synthesize("obj_2", verdicts, [])
    # Should accumulate to REVIEW_REQUIRED
    assert result.final_verdict == VerdictClass.REVIEW_REQUIRED

def test_trust_engine_rejects_hidden_overrides():
    engine = TrustedConstitutionVerdictEngine()
    synthesizer = FinalVerdictSynthesizer()
    verdicts = [DomainVerdictRecord(verdict_id="7", domain="release", verdict=VerdictClass.PASS, evidence_refs=[])]
    final = synthesizer.synthesize("obj_3", verdicts, [])

    trust = engine.evaluate(final, stale_waivers=False, hidden_overrides=True)
    assert trust.trust_level == TrustVerdict.BLOCKED
    assert "overrides" in trust.breakdown

def test_trust_engine_degrades_stale_waivers():
    engine = TrustedConstitutionVerdictEngine()
    synthesizer = FinalVerdictSynthesizer()
    verdicts = [DomainVerdictRecord(verdict_id="8", domain="release", verdict=VerdictClass.PASS, evidence_refs=[])]
    final = synthesizer.synthesize("obj_4", verdicts, [])

    trust = engine.evaluate(final, stale_waivers=True, hidden_overrides=False)
    assert trust.trust_level == TrustVerdict.DEGRADED
    assert "waivers" in trust.breakdown
