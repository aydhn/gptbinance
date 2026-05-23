import pytest
from app.representation_plane.models import RepresentationObject, CaveatRecord, DisclaimerRecord, CorrectionRecord
from app.representation_plane.enums import RepresentationClass, AudienceClass, MaterialityClass, RelianceClass, TrustVerdictEnum
from app.representation_plane.trust import TrustedRepresentationVerdictEngine
from app.representation_plane.registry import CanonicalRepresentationRegistry
from app.representation_plane.equivalence import RepresentationEquivalenceAnalyzer

def test_representation_registry():
    registry = CanonicalRepresentationRegistry()
    rep = RepresentationObject(
        representation_id="rep_001",
        rep_class=RepresentationClass.DISCLOSURE,
        owner="compliance",
        scope="global",
        content="System is operating normally.",
        audience=AudienceClass.BENEFICIARY,
        materiality=MaterialityClass.MATERIAL,
        reliance_posture=RelianceClass.REASONABLE
    )
    registry.register(rep)
    assert registry.get("rep_001").content == "System is operating normally."

def test_trust_engine_material_omission():
    rep = RepresentationObject(
        representation_id="rep_002",
        rep_class=RepresentationClass.STATEMENT,
        owner="marketing",
        scope="public",
        content="Zero fee trading.",
        audience=AudienceClass.PUBLIC if hasattr(AudienceClass, 'PUBLIC') else AudienceClass.BENEFICIARY,
        materiality=MaterialityClass.OMITTED_MATERIAL,
        reliance_posture=RelianceClass.INDUCED
    )
    verdict = TrustedRepresentationVerdictEngine.evaluate(rep, [], [], [])
    assert verdict.verdict == TrustVerdictEnum.BLOCKED
    assert "Material omission detected" in verdict.blockers[0]

def test_trust_engine_disclaimer_laundering():
    rep = RepresentationObject(
        representation_id="rep_003",
        rep_class=RepresentationClass.DISCLOSURE,
        owner="sales",
        scope="public",
        content="100% Guaranteed Returns",
        audience=AudienceClass.BENEFICIARY,
        materiality=MaterialityClass.MATERIAL,
        reliance_posture=RelianceClass.INDUCED
    )
    disc = DisclaimerRecord(
        disclaimer_id="disc_001",
        representation_id="rep_003",
        content="Returns are not actually guaranteed.",
        limits_liability=True,
        is_laundering_attempt=True
    )
    verdict = TrustedRepresentationVerdictEngine.evaluate(rep, [], [disc], [])
    assert verdict.verdict == TrustVerdictEnum.BLOCKED
    assert "Disclaimer laundering detected" in verdict.blockers[0]

def test_trust_engine_buried_caveat():
    rep = RepresentationObject(
        representation_id="rep_004",
        rep_class=RepresentationClass.NOTICE,
        owner="ops",
        scope="system",
        content="All systems go.",
        audience=AudienceClass.INTERNAL,
        materiality=MaterialityClass.MATERIAL,
        reliance_posture=RelianceClass.REASONABLE
    )
    cav = CaveatRecord(
        caveat_id="cav_001",
        representation_id="rep_004",
        content="Except matching engine is down.",
        is_material=True,
        is_buried=True
    )
    verdict = TrustedRepresentationVerdictEngine.evaluate(rep, [cav], [], [])
    assert verdict.verdict == TrustVerdictEnum.CAUTION

def test_equivalence_analyzer():
    rep_live = RepresentationObject(
        representation_id="live_01",
        rep_class=RepresentationClass.STATEMENT,
        owner="sys",
        scope="x",
        content="Status Green",
        audience=AudienceClass.BENEFICIARY,
        materiality=MaterialityClass.MATERIAL,
        reliance_posture=RelianceClass.REASONABLE
    )
    rep_replay = rep_live.copy(update={"content": "Status Unknown"})

    result = RepresentationEquivalenceAnalyzer.compare_environments(rep_replay, rep_live, rep_live, rep_live)
    assert not result["equivalent"]
    assert "Content mismatch" in result["divergences"][0]
