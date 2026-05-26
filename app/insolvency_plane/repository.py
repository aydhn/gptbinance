# repository.py
from app.insolvency_plane.registry import InsolvencyRegistry
from app.insolvency_plane.insolvencies import InsolvencyManager
from app.insolvency_plane.triggers import DistressTriggerManager
from app.insolvency_plane.estate import EstateManager
from app.insolvency_plane.estate_assets import EstateAssetManager
from app.insolvency_plane.estate_scope import EstateScopeManager
from app.insolvency_plane.claims import ClaimManager
from app.insolvency_plane.admission import ClaimAdmissionManager
from app.insolvency_plane.objections import ClaimObjectionManager
from app.insolvency_plane.secured_claims import SecuredClaimManager
from app.insolvency_plane.unsecured_claims import UnsecuredClaimManager
from app.insolvency_plane.priority_claims import PriorityClaimManager
from app.insolvency_plane.subordination import SubordinationManager
from app.insolvency_plane.administrative import AdministrativeClaimManager
from app.insolvency_plane.stays import StayManager
from app.insolvency_plane.stay_scope import StayScopeManager
from app.insolvency_plane.moratoria import MoratoriumManager
from app.insolvency_plane.avoidance import AvoidanceManager
from app.insolvency_plane.preferences import PreferenceRiskManager
from app.insolvency_plane.fraud_transfers import FraudTransferManager
from app.insolvency_plane.dip import DIPSupportManager
from app.insolvency_plane.plans import PlanManager
from app.insolvency_plane.plan_classes import PlanClassManager
from app.insolvency_plane.plan_support import PlanSupportManager
from app.insolvency_plane.confirmation import ConfirmationManager
from app.insolvency_plane.cures import CureManager
from app.insolvency_plane.haircuts import HaircutManager
from app.insolvency_plane.assumption_rejection import AssumptionRejectionManager
from app.insolvency_plane.liquidation import LiquidationManager
from app.insolvency_plane.going_concern import GoingConcernManager
from app.insolvency_plane.distribution_loss import DistributionLossManager
from app.insolvency_plane.post_confirmation import PostConfirmationManager
from app.insolvency_plane.residual_deficits import ResidualDeficitManager
from app.insolvency_plane.comparisons import InsolvencyComparisonManager
from app.insolvency_plane.forecasting import InsolvencyForecastManager
from app.insolvency_plane.debt import InsolvencyDebtManager
from app.insolvency_plane.readiness import InsolvencyReadinessManager
from app.insolvency_plane.equivalence import InsolvencyEquivalenceManager
from app.insolvency_plane.divergence import InsolvencyDivergenceManager
from app.insolvency_plane.quality import InsolvencyQualityManager
from app.insolvency_plane.trust import InsolvencyTrustManager
from app.insolvency_plane.manifests import InsolvencyManifestManager

class InsolvencyRepository:
    def __init__(self):
        self.registry = InsolvencyRegistry()
        self.insolvency_manager = InsolvencyManager()
        self.trigger_manager = DistressTriggerManager()
        self.estate_manager = EstateManager()
        self.estate_asset_manager = EstateAssetManager()
        self.estate_scope_manager = EstateScopeManager()
        self.claim_manager = ClaimManager()
        self.admission_manager = ClaimAdmissionManager()
        self.objection_manager = ClaimObjectionManager()
        self.secured_claim_manager = SecuredClaimManager()
        self.unsecured_claim_manager = UnsecuredClaimManager()
        self.priority_claim_manager = PriorityClaimManager()
        self.subordination_manager = SubordinationManager()
        self.administrative_claim_manager = AdministrativeClaimManager()
        self.stay_manager = StayManager()
        self.stay_scope_manager = StayScopeManager()
        self.moratorium_manager = MoratoriumManager()
        self.avoidance_manager = AvoidanceManager()
        self.preference_risk_manager = PreferenceRiskManager()
        self.fraud_transfer_manager = FraudTransferManager()
        self.dip_support_manager = DIPSupportManager()
        self.plan_manager = PlanManager()
        self.plan_class_manager = PlanClassManager()
        self.plan_support_manager = PlanSupportManager()
        self.confirmation_manager = ConfirmationManager()
        self.cure_manager = CureManager()
        self.haircut_manager = HaircutManager()
        self.assumption_rejection_manager = AssumptionRejectionManager()
        self.liquidation_manager = LiquidationManager()
        self.going_concern_manager = GoingConcernManager()
        self.distribution_loss_manager = DistributionLossManager()
        self.post_confirmation_manager = PostConfirmationManager()
        self.residual_deficit_manager = ResidualDeficitManager()
        self.comparison_manager = InsolvencyComparisonManager()
        self.forecast_manager = InsolvencyForecastManager()
        self.debt_manager = InsolvencyDebtManager()
        self.readiness_manager = InsolvencyReadinessManager()
        self.equivalence_manager = InsolvencyEquivalenceManager()
        self.divergence_manager = InsolvencyDivergenceManager()
        self.quality_manager = InsolvencyQualityManager()
        self.trust_manager = InsolvencyTrustManager()
        self.manifest_manager = InsolvencyManifestManager()
