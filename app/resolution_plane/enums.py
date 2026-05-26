from enum import Enum

class ResolutionClass(Enum):
    BRIDGE_RESOLUTION = "bridge_resolution"
    CRITICAL_FUNCTION_RESOLUTION = "critical_function_resolution"
    CUSTOMER_ASSET_PROTECTION_RESOLUTION = "customer_asset_protection_resolution"
    PERFORMANCE_SECURITY_EXHAUSTION_RESOLUTION = "performance_security_exhaustion_resolution"
    RECOVERY_FAILURE_RESOLUTION = "recovery_failure_resolution"
    FEDERATED_PARTNER_RESOLUTION = "federated_partner_resolution"
    MIGRATION_SERVICE_RESOLUTION = "migration_service_resolution"
    RELEASE_REGRESSION_RESOLUTION = "release_regression_resolution"
    COMPLIANCE_CRITICAL_OPERATION_RESOLUTION = "compliance_critical_operation_resolution"
    LIQUIDITY_SPIRAL_RESOLUTION = "liquidity_spiral_resolution"
    CROSS_PLANE_ORDERLY_RESOLUTION = "cross_plane_orderly_resolution"
    WIND_DOWN_TRANSITION_RESOLUTION = "wind_down_transition_resolution"

class TriggerClass(Enum):
    CONTINUITY_RISK = "continuity_risk"
    INSOLVENCY_LINKED = "insolvency_linked"
    SYSTEMIC_CRITICALITY = "systemic_criticality"
    BENEFICIARY_HARM = "beneficiary_harm"

class BridgeClass(Enum):
    TEMPORARY_BRIDGE = "temporary_bridge"
    OPERATIONAL_BRIDGE = "operational_bridge"
    MISSING_FUNCTION_BRIDGE = "missing_function_bridge"
    FAILED_BRIDGE = "failed_bridge"

class TransferClass(Enum):
    INCLUSIVE_PERIMETER = "inclusive_perimeter"
    CARVED_OUT_PERIMETER = "carved_out_perimeter"
    CONTAMINATED_PERIMETER = "contaminated_perimeter"
    PARTIAL_TRANSFER = "partial_transfer"

class ContinuityClass(Enum):
    VERIFIED_CONTINUITY = "verified_continuity"
    PROVISIONAL_CONTINUITY = "provisional_continuity"
    BROKEN_CONTINUITY = "broken_continuity"

class RingFenceClass(Enum):
    VALID_RING_FENCE = "valid_ring_fence"
    PARTIAL_RING_FENCE = "partial_ring_fence"
    BREACHED_RING_FENCE = "breached_ring_fence"
    COSMETIC_RING_FENCE = "cosmetic_ring_fence"

class WriteDownClass(Enum):
    CLASS_WRITE_DOWN = "class_write_down"
    TEMPORARY_WRITE_DOWN_POSTURE = "temporary_write_down_posture"
    MISALLOCATED_WRITE_DOWN = "misallocated_write_down"
    HIDDEN_WRITE_DOWN_EFFECT = "hidden_write_down_effect"

class ConversionClass(Enum):
    CLAIM_TO_EQUITY_LIKE_CONVERSION = "claim_to_equity_like_conversion"
    PARTIAL_CONVERSION = "partial_conversion"
    UNFAIR_CONVERSION = "unfair_conversion"
    DISPUTED_CONVERSION = "disputed_conversion"

class WindDownClass(Enum):
    ORDERLY_WIND_DOWN = "orderly_wind_down"
    ACCELERATED_WIND_DOWN = "accelerated_wind_down"
    PARTIAL_WIND_DOWN = "partial_wind_down"
    WIND_DOWN_WITH_CONTINUITY_HARM = "wind_down_with_continuity_harm"

class PortabilityClass(Enum):
    PORTABLE_CONTRACT = "portable_contract"
    NON_PORTABLE_CONTRACT = "non_portable_contract"
    CONDITIONALLY_PORTABLE_CONTRACT = "conditionally_portable_contract"
    FAILED_PORTABILITY = "failed_portability"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_EQUIVALENCE = "partial_equivalence"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
