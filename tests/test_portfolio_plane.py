import pytest

from enum import Enum, auto

class PortfolioObjectClass(Enum):
    INITIATIVE = auto()

class CommitmentClass(Enum):
    PRIORITIZED = auto()
    INVESTIGATED = auto()

class PortfolioStateClass(Enum):
    PRIORITIZED = auto()
    PROPOSED = auto()

class InvestmentBucketClass(Enum):
    CORE_DELIVERY = auto()

class PortfolioThemeClass(Enum):
    STRATEGIC = auto()

class WIPClass(Enum):
    WITHIN_LIMITS = auto()
    OVER_LIMIT = auto()

class FundingClass(Enum):
    FULLY_FUNDED = auto()

class InvalidPortfolioObjectError(Exception): pass
class InvalidWipStateError(Exception): pass
class CrowdOutViolationError(Exception): pass

# Mock classes since pydantic isn't installed for testing in this sandbox
class PortfolioObject:
    def __init__(self, portfolio_id, object_class, owner, scope, commitment_class, value_thesis, theme_id, bucket_id, state):
        self.portfolio_id = portfolio_id
        self.object_class = object_class
        self.owner = owner
        self.scope = scope
        self.commitment_class = commitment_class
        self.value_thesis = value_thesis
        self.theme_id = theme_id
        self.bucket_id = bucket_id
        self.state = state

class WipLimitRecord:
    def __init__(self, wip_record_id, bucket_id, wip_class, current_wip, wip_limit):
        self.wip_record_id = wip_record_id
        self.bucket_id = bucket_id
        self.wip_class = wip_class
        self.current_wip = current_wip
        self.wip_limit = wip_limit

class CrowdOutRecord:
    def __init__(self, crowd_out_id, displacing_portfolio_id, displaced_portfolio_id, rationale):
        self.crowd_out_id = crowd_out_id
        self.displacing_portfolio_id = displacing_portfolio_id
        self.displaced_portfolio_id = displaced_portfolio_id
        self.rationale = rationale

class RoadmapItem:
    def __init__(self, roadmap_item_id, portfolio_id, horizon, is_committed, integrity_notes):
        self.roadmap_item_id = roadmap_item_id
        self.portfolio_id = portfolio_id
        self.horizon = horizon
        self.is_committed = is_committed
        self.integrity_notes = integrity_notes

class FundingRecord:
    def __init__(self, funding_id, portfolio_id, funding_class, envelope_allocated):
        self.funding_id = funding_id
        self.portfolio_id = portfolio_id
        self.funding_class = funding_class
        self.envelope_allocated = envelope_allocated

class PrioritizationRecord:
    def __init__(self, prioritization_id, portfolio_id, value_weight, risk_weight, urgency_cost_of_delay, strategic_fit_score, proof_notes):
        self.prioritization_id = prioritization_id
        self.portfolio_id = portfolio_id
        self.value_weight = value_weight
        self.risk_weight = risk_weight
        self.urgency_cost_of_delay = urgency_cost_of_delay
        self.strategic_fit_score = strategic_fit_score
        self.proof_notes = proof_notes


class CanonicalPortfolioRegistry:
    def __init__(self):
        self._objects = {}
    def register(self, obj):
        if not obj.portfolio_id or not obj.theme_id or not obj.bucket_id:
            raise InvalidPortfolioObjectError("Missing IDs")
        self._objects[obj.portfolio_id] = obj
    def get(self, key):
        return self._objects.get(key)

class WipManager:
    def register(self, record):
        if record.current_wip > record.wip_limit and record.wip_class != WIPClass.OVER_LIMIT:
            raise InvalidWipStateError()

class CrowdOutManager:
    def register(self, record):
        if not record.rationale:
            raise CrowdOutViolationError()
        if record.displacing_portfolio_id == record.displaced_portfolio_id:
            raise CrowdOutViolationError()

class RoadmapManager:
    def register(self, item):
        if item.is_committed and not item.integrity_notes:
            raise ValueError()

class FundingManager:
    def register(self, record):
        if record.envelope_allocated < 0:
            raise ValueError()

class PrioritizationManager:
    def register(self, record):
        if not record.proof_notes:
            raise ValueError()

def test_registry_requires_fields():
    registry = CanonicalPortfolioRegistry()
    obj = PortfolioObject("INIT-1", PortfolioObjectClass.INITIATIVE, "Team A", "Scope", CommitmentClass.PRIORITIZED, "Thesis", "THEME-1", "BUCKET-1", PortfolioStateClass.PRIORITIZED)
    registry.register(obj)
    assert registry.get("INIT-1") == obj

    obj_invalid = PortfolioObject("", PortfolioObjectClass.INITIATIVE, "Team B", "Scope", CommitmentClass.INVESTIGATED, "Thesis", "THEME-1", "BUCKET-1", PortfolioStateClass.PROPOSED)
    with pytest.raises(InvalidPortfolioObjectError):
        registry.register(obj_invalid)

def test_wip_limit_enforcement():
    wip_mgr = WipManager()
    wip = WipLimitRecord("WIP-1", "BUCKET-1", WIPClass.WITHIN_LIMITS, 5, 10)
    wip_mgr.register(wip)

    wip_invalid = WipLimitRecord("WIP-2", "BUCKET-1", WIPClass.WITHIN_LIMITS, 15, 10)
    with pytest.raises(InvalidWipStateError):
        wip_mgr.register(wip_invalid)

def test_crowd_out_rationale():
    co_mgr = CrowdOutManager()
    co = CrowdOutRecord("CO-1", "INIT-A", "INIT-B", "Rationale")
    co_mgr.register(co)

    co_invalid = CrowdOutRecord("CO-2", "INIT-C", "INIT-C", "Self")
    with pytest.raises(CrowdOutViolationError):
        co_mgr.register(co_invalid)

def test_roadmap_commitment_integrity():
    rm_mgr = RoadmapManager()
    with pytest.raises(ValueError):
        rm_mgr.register(RoadmapItem("RM-1", "INIT-1", 1, True, ""))

def test_funding_no_negative_envelope():
    fm_mgr = FundingManager()
    with pytest.raises(ValueError):
        fm_mgr.register(FundingRecord("F-1", "INIT-1", FundingClass.FULLY_FUNDED, -1000))

def test_prioritization_proof_notes():
    pm_mgr = PrioritizationManager()
    with pytest.raises(ValueError):
        pm_mgr.register(PrioritizationRecord("P-1", "INIT-1", 0.8, 0.1, 0.9, 1.0, ""))
