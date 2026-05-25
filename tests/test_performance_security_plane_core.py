import pytest
from datetime import timezone, datetime
from app.performance_security_plane.models import PerformanceSecurityObject
from app.performance_security_plane.enums import SecurityClass, SecuredObligationClass, CollateralClass, GuaranteeClass, FundingClass, DrawClass, ReleaseClass, ImpairmentClass, PriorityClass, ExhaustionClass, SecurityEquivalenceVerdict, SecurityTrustVerdict
from app.performance_security_plane.registry import PerformanceSecurityRegistry
from app.performance_security_plane.exceptions import InvalidSecurityObjectError

def test_performance_security_object_creation():
    obj = PerformanceSecurityObject(
        security_id="SEC-001",
        class_type=SecurityClass.ESCROW,
        owner="Alice",
        scope="Settlement X",
        secured_obligation_posture="fully_secured",
        draw_release_posture="conditional"
    )
    assert obj.security_id == "SEC-001"
    assert obj.class_type == SecurityClass.ESCROW
    assert obj.owner == "Alice"
    assert obj.scope == "Settlement X"

def test_registry_registration():
    registry = PerformanceSecurityRegistry()
    obj = PerformanceSecurityObject(
        security_id="SEC-001",
        class_type=SecurityClass.ESCROW,
        owner="Alice",
        scope="Settlement X",
        secured_obligation_posture="fully_secured",
        draw_release_posture="conditional"
    )
    registry.register_security(obj)

    fetched = registry.get_security("SEC-001")
    assert fetched == obj

def test_registry_duplicate_registration():
    registry = PerformanceSecurityRegistry()
    obj = PerformanceSecurityObject(
        security_id="SEC-001",
        class_type=SecurityClass.ESCROW,
        owner="Alice",
        scope="Settlement X",
        secured_obligation_posture="fully_secured",
        draw_release_posture="conditional"
    )
    registry.register_security(obj)
    with pytest.raises(InvalidSecurityObjectError):
        registry.register_security(obj)

from app.performance_security_plane.securities import SecurityManager
def test_create_security_record():
    manager = SecurityManager()
    record = manager.create_security_record("SEC-002", "active", "Verification clear")
    assert record.security_id == "SEC-002"
    assert record.state == "active"
    assert len(record.lineage_refs) > 0

from app.performance_security_plane.secured_obligations import SecuredObligationManager
def test_create_secured_obligation():
    manager = SecuredObligationManager()
    record = manager.create_secured_obligation("OBL-001", ["SEC-001"], SecuredObligationClass.FULLY_SECURED)
    assert record.posture == SecuredObligationClass.FULLY_SECURED

from app.performance_security_plane.escrow import EscrowManager
def test_create_escrow():
    manager = EscrowManager()
    record = manager.create_escrow("ESC-001", "SEC-001", "funded")
    assert record.escrow_id == "ESC-001"
    assert record.type == "funded"

from app.performance_security_plane.reserves import ReserveManager
def test_create_reserve():
    manager = ReserveManager()
    record = manager.create_reserve("RES-001", "SEC-001", "segregated")
    assert record.type == "segregated"

from app.performance_security_plane.holdbacks import HoldbackManager
def test_create_holdback():
    manager = HoldbackManager()
    record = manager.create_holdback("HLD-001", "SEC-001", "payment")
    assert record.type == "payment"

from app.performance_security_plane.collateral import CollateralManager
def test_create_collateral():
    manager = CollateralManager()
    record = manager.create_collateral("COL-001", "SEC-001", CollateralClass.PLEDGED)
    assert record.type == CollateralClass.PLEDGED

from app.performance_security_plane.pools import CollateralPoolManager
def test_create_pool():
    manager = CollateralPoolManager()
    record = manager.create_pool("POL-001", "ring_fenced")
    assert record.type == "ring_fenced"

from app.performance_security_plane.pledged_assets import PledgedAssetManager
def test_create_pledged_asset():
    manager = PledgedAssetManager()
    record = manager.create_pledged_asset("AST-001", "SEC-001", "eligible")
    assert record.type == "eligible"

from app.performance_security_plane.guarantees import GuaranteeManager
def test_create_guarantee():
    manager = GuaranteeManager()
    record = manager.create_guarantee("GAR-001", "SEC-001", GuaranteeClass.CAPPED)
    assert record.type == GuaranteeClass.CAPPED

from app.performance_security_plane.support import SupportUndertakingManager
def test_create_support_undertaking():
    manager = SupportUndertakingManager()
    record = manager.create_support_undertaking("SUP-001", "SEC-001", "standby")
    assert record.type == "standby"

from app.performance_security_plane.beneficiaries import BeneficiaryManager
def test_create_beneficiary():
    manager = BeneficiaryManager()
    record = manager.create_beneficiary("BEN-001", "SEC-001", "primary")
    assert record.type == "primary"

from app.performance_security_plane.priorities import PriorityManager
def test_create_priority():
    manager = PriorityManager()
    record = manager.create_priority("SEC-001", "BEN-001", PriorityClass.FIRST)
    assert record.type == PriorityClass.FIRST

from app.performance_security_plane.funding import FundingManager
def test_create_funding_status():
    manager = FundingManager()
    record = manager.create_funding_status("SEC-001", FundingClass.FULLY_FUNDED)
    assert record.status == FundingClass.FULLY_FUNDED

from app.performance_security_plane.segregation import SegregationManager
def test_create_segregation():
    manager = SegregationManager()
    record = manager.create_segregation("SEC-001", "segregated")
    assert record.status == "segregated"

from app.performance_security_plane.valuation import ValuationManager
def test_create_valuation():
    manager = ValuationManager()
    record = manager.create_valuation("SEC-001", "current", 1000.0, "fresh")
    assert record.value == 1000.0

from app.performance_security_plane.impairment import ImpairmentManager
def test_create_impairment():
    manager = ImpairmentManager()
    record = manager.create_impairment("SEC-001", ImpairmentClass.COLLATERAL_IMPAIRMENT)
    assert record.type == ImpairmentClass.COLLATERAL_IMPAIRMENT

from app.performance_security_plane.draws import DrawManager
def test_create_draw_right():
    manager = DrawManager()
    record = manager.create_draw_right("DRW-001", "SEC-001", DrawClass.IMMEDIATE)
    assert record.type == DrawClass.IMMEDIATE

from app.performance_security_plane.draw_events import DrawEventManager
def test_create_draw_event():
    manager = DrawEventManager()
    record = manager.create_draw_event("EVT-001", "SEC-001", "valid", 500.0)
    assert record.type == "valid"

from app.performance_security_plane.release_triggers import ReleaseTriggerManager
def test_create_release_trigger():
    manager = ReleaseTriggerManager()
    record = manager.create_release_trigger("TRG-001", "SEC-001", "milestone")
    assert record.type == "milestone"

from app.performance_security_plane.releases import ReleaseManager
def test_create_release():
    manager = ReleaseManager()
    record = manager.create_release("REL-001", "SEC-001", ReleaseClass.PARTIAL)
    assert record.type == ReleaseClass.PARTIAL

from app.performance_security_plane.replenishment import ReplenishmentManager
def test_create_replenishment_duty():
    manager = ReplenishmentManager()
    record = manager.create_replenishment_duty("DTY-001", "SEC-001", "mandatory")
    assert record.type == "mandatory"

from app.performance_security_plane.substitution import SubstitutionManager
def test_create_substitute_collateral():
    manager = SubstitutionManager()
    record = manager.create_substitute_collateral("SUB-001", "SEC-001", "SEC-002", "valid")
    assert record.type == "valid"

from app.performance_security_plane.exhaustion import ExhaustionManager
def test_create_exhaustion():
    manager = ExhaustionManager()
    record = manager.create_exhaustion("SEC-001", ExhaustionClass.FULLY_EXHAUSTED)
    assert record.type == ExhaustionClass.FULLY_EXHAUSTED

from app.performance_security_plane.residuals import ResidualsManager
def test_create_residual_undersecurity():
    manager = ResidualsManager()
    record = manager.create_residual_undersecurity("SEC-001", "unsecured_remainder", 500.0)
    assert record.type == "unsecured_remainder"

from app.performance_security_plane.comparisons import ComparisonsManager
def test_create_comparison():
    manager = ComparisonsManager()
    record = manager.create_comparison("CMP-001", "SEC-001", "SEC-002", "escrow_vs_reserve", "match")
    assert record.verdict == "match"

from app.performance_security_plane.forecasting import ForecastingManager
def test_create_forecast():
    manager = ForecastingManager()
    record = manager.create_forecast("FCT-001", "SEC-001", "depletion_risk", "high")
    assert record.uncertainty_class == "high"

from app.performance_security_plane.debt import DebtManager
def test_create_debt_record():
    manager = DebtManager()
    record = manager.create_debt_record("DBT-001", "SEC-001", "phantom_collateral", "critical")
    assert record.type == "phantom_collateral"

from app.performance_security_plane.readiness import ReadinessManager
def test_assess_readiness():
    manager = ReadinessManager()
    record = manager.assess_readiness("SEC-001")
    assert record["scope_clarity"] == "clear"

from app.performance_security_plane.equivalence import EquivalenceManager
def test_assess_equivalence():
    manager = EquivalenceManager()
    record = manager.assess_equivalence("RPT-001", "SEC-001", SecurityEquivalenceVerdict.EQUIVALENT, [])
    assert record.verdict == SecurityEquivalenceVerdict.EQUIVALENT

from app.performance_security_plane.divergence import DivergenceManager
def test_assess_divergence():
    manager = DivergenceManager()
    record = manager.assess_divergence("RPT-002", "SEC-001", [{"issue": "valuation_diff"}])
    assert len(record.divergences) == 1

from app.performance_security_plane.quality import QualityManager
def test_evaluate_quality():
    manager = QualityManager()
    record = manager.evaluate_quality("SEC-001")
    assert record["quality_verdict"] == "high"

from app.performance_security_plane.trust import TrustedPerformanceSecurityVerdictEngine
def test_evaluate_trust():
    engine = TrustedPerformanceSecurityVerdictEngine()
    record = engine.evaluate_trust("SEC-001")
    assert record.verdict == SecurityTrustVerdict.TRUSTED

from app.performance_security_plane.manifests import ManifestBuilder
def test_build_manifest():
    builder = ManifestBuilder()
    record = builder.build_manifest("MNF-001", ["SEC-001"], "hash")
    assert record.hash == "hash"

from app.performance_security_plane.storage import StorageManager
from app.performance_security_plane.repository import PerformanceSecurityRepository
def test_storage_manager():
    registry = PerformanceSecurityRegistry()
    repo = PerformanceSecurityRepository(registry)
    manager = StorageManager(repo)
    assert manager.repository is not None
