import pytest
from app.precedent_plane.cases import CasesManager
from app.precedent_plane.holdings import HoldingsManager
from app.precedent_plane.conflicts import ConflictsManager
from app.precedent_plane.trust import TrustManager
from app.precedent_plane.models import CaseRecord, HoldingRecord
from app.precedent_plane.enums import CaseClass, HoldingClass, ConflictClass, PrecedentTrustVerdict

def test_core_logic():
    cases = CasesManager()
    holdings = HoldingsManager()
    conflicts = ConflictsManager()
    trust = TrustManager()

    # 1. Register holding
    h1 = HoldingRecord(
        holding_id="H-01", precedent_id="P-01", holding_class=HoldingClass.CONTROLLING,
        description="Must authenticate", proof_notes="", lineage_refs=[]
    )
    holdings.register_holding(h1)

    # 2. Register case
    c1 = CaseRecord(
        case_id="C-01", precedent_id="P-01", case_class=CaseClass.OPEN,
        description="Auth issue", proof_notes="", lineage_refs=[], holdings=[h1]
    )
    cases.register_case(c1)

    # 3. Resolve case
    cases.resolve_case("C-01")
    assert cases.records[0].case_class == CaseClass.RESOLVED

    # 4. Evaluate trust without conflicts
    report = trust.evaluate_trust("P-01", [], [h1])
    assert report.verdict == PrecedentTrustVerdict.TRUSTED

    # 5. Add conflict and evaluate trust
    conflicts.register_conflict("P-01", "P-02", ConflictClass.OUTCOME, "Different outcomes")
    unresolved = conflicts.get_unresolved_conflicts()

    report2 = trust.evaluate_trust("P-01", unresolved, [h1])
    assert report2.verdict == PrecedentTrustVerdict.DEGRADED
