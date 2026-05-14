from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.cost_plane.enums import (
    CostClass, SpendClass, FeeClass, BudgetClass, GuardrailClass,
    AllocationClass, AmortizationClass, UnitEconomicsClass, VarianceClass,
    CostEquivalenceVerdict, CostTrustVerdict
)

class CostObjectRef(BaseModel):
    cost_id: str
    class_type: CostClass
    owner: str

class CostObject(BaseModel):
    cost_id: str
    class_type: CostClass
    owner: str
    scope: str
    attribution_semantics: str
    measurement_window: str
    is_mandatory: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)

class SpendRecord(BaseModel):
    spend_id: str
    cost_id: str
    spend_class: SpendClass
    amount: float
    currency: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    proof_notes: Optional[str] = None

class FeeRecord(BaseModel):
    fee_id: str
    cost_id: str
    fee_class: FeeClass
    amount: float
    currency: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    drift_warnings: List[str] = Field(default_factory=list)

class BudgetDefinition(BaseModel):
    budget_id: str
    cost_id: str
    budget_class: BudgetClass
    owner: str
    limit: float
    currency: str
    time_window: str

class BudgetSnapshot(BaseModel):
    budget_id: str
    spent: float
    remaining: float
    exhausted: bool
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class GuardrailRecord(BaseModel):
    guardrail_id: str
    budget_id: str
    guardrail_class: GuardrailClass
    ceiling: float
    current_value: float
    breached: bool
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class AllocationPolicy(BaseModel):
    policy_id: str
    allocation_class: AllocationClass
    rules: Dict[str, Any]
    lineage_refs: List[str] = Field(default_factory=list)

class AllocationRecord(BaseModel):
    allocation_id: str
    spend_id: str
    policy_id: str
    allocated_to: str
    amount: float
    currency: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SharedCostPool(BaseModel):
    pool_id: str
    name: str
    total_amount: float
    currency: str
    allocation_policy_id: str
    subsidy_warnings: List[str] = Field(default_factory=list)

class AmortizationRecord(BaseModel):
    amortization_id: str
    cost_id: str
    amortization_class: AmortizationClass
    total_amount: float
    amortized_amount_per_period: float
    currency: str
    proof_notes: Optional[str] = None

class ReservationCostRecord(BaseModel):
    reservation_id: str
    cost_id: str
    reserved_capacity: float
    used_capacity: float
    cost_of_unused: float
    currency: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class UsageCostRecord(BaseModel):
    usage_id: str
    cost_id: str
    unit_cost: float
    units_used: float
    total_cost: float
    currency: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class VendorInvoiceRecord(BaseModel):
    invoice_id: str
    vendor_name: str
    total_amount: float
    currency: str
    reconciled: bool
    freshness_warnings: List[str] = Field(default_factory=list)

class ExchangeFeeSchedule(BaseModel):
    schedule_id: str
    exchange_name: str
    maker_fee: float
    taker_fee: float

class UnitEconomicsRecord(BaseModel):
    record_id: str
    cost_id: str
    ue_class: UnitEconomicsClass
    unit_cost: float
    currency: str
    denominator_quality_notes: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class VarianceRecord(BaseModel):
    variance_id: str
    cost_id: str
    variance_class: VarianceClass
    expected: float
    actual: float
    variance_amount: float
    is_anomaly: bool
    proof_notes: Optional[str] = None

class CostForecastReport(BaseModel):
    report_id: str
    cost_id: str
    forecast_amount: float
    currency: str
    uncertainty_class: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class OptimizationOpportunity(BaseModel):
    opportunity_id: str
    cost_id: str
    description: str
    estimated_savings: float
    currency: str
    side_effect_caveats: List[str] = Field(default_factory=list)

class CostDebtRecord(BaseModel):
    debt_id: str
    cost_id: str
    description: str
    severity: str
    amount: float
    currency: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CostEquivalenceReport(BaseModel):
    report_id: str
    workload_ref: str
    environments_compared: List[str]
    verdict: CostEquivalenceVerdict
    divergence_sources: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CostDivergenceReport(BaseModel):
    report_id: str
    source_env: str
    target_env: str
    divergence_amount: float
    currency: str
    severity: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CostTrustVerdictReport(BaseModel):
    verdict: CostTrustVerdict
    factors: Dict[str, Any]
    blockers: List[str] = Field(default_factory=list)
    caveats: List[str] = Field(default_factory=list)

class CostAuditRecord(BaseModel):
    audit_id: str
    action: str
    actor: str
    target_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CostArtifactManifest(BaseModel):
    manifest_id: str
    cost_refs: List[str] = Field(default_factory=list)
    budget_refs: List[str] = Field(default_factory=list)
    allocation_refs: List[str] = Field(default_factory=list)
    variance_refs: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
