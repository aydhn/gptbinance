from enum import Enum

class AssuranceClass(str, Enum):
    IMMUNITY_ASSURANCE = "immunity_assurance"
    ADAPTATION_EFFECTIVENESS_ASSURANCE = "adaptation_effectiveness_assurance"
    DRIFT_STABILITY_ASSURANCE = "drift_stability_assurance"
    NORMALIZATION_LEGITIMACY_ASSURANCE = "normalization_legitimacy_assurance"
    BENEFICIARY_SAFETY_ASSURANCE = "beneficiary_safety_assurance"
    CONTROL_INTEGRITY_ASSURANCE = "control_integrity_assurance"
    COMPLIANCE_ASSURANCE = "compliance_assurance"
    SECURITY_POSTURE_ASSURANCE = "security_posture_assurance"
    RELEASE_RECOVERY_ASSURANCE = "release_recovery_assurance"
    MIGRATION_PORTABILITY_ASSURANCE = "migration_portability_assurance"
    FEDERATED_ALIGNMENT_ASSURANCE = "federated_alignment_assurance"
    CROSS_PLANE_OPERATING_LEGITIMACY_ASSURANCE = "cross_plane_operating_legitimacy_assurance"

class ClaimClass(str, Enum):
    BOUNDED_CLAIM = "bounded_claim"
    PROVISIONAL_CLAIM = "provisional_claim"
    OVERCLAIMED_ASSERTION = "overclaimed_assertion"
    UNSUPPORTED_CLAIM = "unsupported_claim"

class EvidenceClass(str, Enum):
    STRONG_EVIDENCE = "strong_evidence"
    WEAK_EVIDENCE = "weak_evidence"
    STALE_EVIDENCE = "stale_evidence"
    SELECTIVE_EVIDENCE = "selective_evidence"

class SufficiencyClass(str, Enum):
    SUFFICIENT = "sufficient"
    MARGINAL = "marginal"
    INSUFFICIENT = "insufficient"
    FALSELY_SUFFICIENT = "falsely_sufficient"

class CertificationClass(str, Enum):
    BOUNDED_CERTIFICATION = "bounded_certification"
    PROVISIONAL_CERTIFICATION = "provisional_certification"
    EXPIRED_CERTIFICATION = "expired_certification"
    SCOPE_MISALIGNED_CERTIFICATION = "scope_misaligned_certification"

class AttestationClass(str, Enum):
    SELF_ATTESTATION = "self_attestation"
    INTERNAL_ATTESTATION = "internal_attestation"
    INDEPENDENT_ATTESTATION = "independent_attestation"
    CONFLICTED_ATTESTATION = "conflicted_attestation"

class SurveillanceClass(str, Enum):
    ACTIVE_SURVEILLANCE = "active_surveillance"
    REDUCED_SURVEILLANCE = "reduced_surveillance"
    MISSED_SURVEILLANCE = "missed_surveillance"
    SURVEILLANCE_THEATER = "surveillance_theater"

class CaveatClass(str, Enum):
    BOUNDED_CAVEAT = "bounded_caveat"
    MATERIAL_CAVEAT = "material_caveat"
    BENEFICIARY_CAVEAT = "beneficiary_caveat"
    HIDDEN_CAVEAT = "hidden_caveat"

class RevocationClass(str, Enum):
    IMMEDIATE_REVOCATION = "immediate_revocation"
    CONDITIONAL_REVOCATION = "conditional_revocation"
    DOWNGRADE_FIRST_REVOCATION = "downgrade_first_revocation"
    MISSING_REVOCATION_PATH = "missing_revocation_path"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_EQUIVALENT = "partial_equivalent"
    DIVERGED = "diverged"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
