from enum import Enum

class SuccessionClass(str, Enum):
    OPERATOR = "operator_succession"
    POLICY_AUTHORITY = "policy_authority_succession"
    AUTONOMY_MANDATE = "autonomy_mandate_succession"
    ORCHESTRATION_OWNER = "orchestration_owner_succession"
    STEWARDSHIP_CUSTODIAN = "stewardship_custodian_succession"
    ASSURANCE_AUTHORITY = "assurance_authority_succession"
    FEDERATED_PARTNER = "federated_partner_succession"
    EMERGENCY = "emergency_succession"
    SUNSET_SUCCESSOR = "sunset_successor_or_transfer_succession"
    CROSS_PLANE_CONTINUITY = "cross_plane_continuity_succession"

class PredecessorClass(str, Enum):
    ACTIVE = "active_predecessor"
    RETIRING = "retiring_predecessor"
    RESIDUAL = "residual_predecessor"
    HIDDEN = "hidden_predecessor"

class SuccessorClass(str, Enum):
    DESIGNATED = "designated_successor"
    ACTIVE = "active_successor"
    SHADOW = "shadow_successor"
    INCOMPLETE = "incomplete_successor"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
