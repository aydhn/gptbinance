from app.config_plane.enums import MutabilityClass, LayerClass
from app.config_plane.models import MutabilityPolicy
from app.config_plane.exceptions import MutabilityViolation
from typing import Dict

DEFAULT_POLICIES = {
    MutabilityClass.IMMUTABLE: MutabilityPolicy(
        mutability_class=MutabilityClass.IMMUTABLE,
        allowed_layer_classes=[LayerClass.BASE_DEFAULTS, LayerClass.WORKSPACE_DEFAULTS],
        requires_review=False,
    ),
    MutabilityClass.RELEASE_ONLY: MutabilityPolicy(
        mutability_class=MutabilityClass.RELEASE_ONLY,
        allowed_layer_classes=[
            LayerClass.BASE_DEFAULTS,
            LayerClass.WORKSPACE_DEFAULTS,
            LayerClass.PROFILE_DEFAULTS,
            LayerClass.CANDIDATE_BUNDLE,
        ],
        requires_review=True,
    ),
    MutabilityClass.REVIEW_ONLY: MutabilityPolicy(
        mutability_class=MutabilityClass.REVIEW_ONLY,
        allowed_layer_classes=[
            LayerClass.CANDIDATE_BUNDLE,
            LayerClass.DEGRADED_MODE_OVERLAY,
        ],
        requires_review=True,
    ),
    MutabilityClass.RUNTIME_SAFE: MutabilityPolicy(
        mutability_class=MutabilityClass.RUNTIME_SAFE,
        allowed_layer_classes=[
            LayerClass.CANDIDATE_BUNDLE,
            LayerClass.DEGRADED_MODE_OVERLAY,
            LayerClass.RUNTIME_SAFE_PATCH_INTENT,
            LayerClass.EXPERIMENT_CANDIDATE_OVERLAY,
        ],
        requires_review=False,  # Or soft review
    ),
    MutabilityClass.EMERGENCY_OVERLAY_ONLY: MutabilityPolicy(
        mutability_class=MutabilityClass.EMERGENCY_OVERLAY_ONLY,
        allowed_layer_classes=[
            LayerClass.INCIDENT_CONTAINMENT_OVERLAY,
            LayerClass.REMEDIATION_RECOVERY_OVERLAY,
        ],
        requires_review=True,
    ),
}


def validate_mutability(
    mutability_class: MutabilityClass, target_layer_class: LayerClass
):
    policy = DEFAULT_POLICIES.get(mutability_class)
    if not policy:
        raise MutabilityViolation(f"No policy defined for {mutability_class}")

    if target_layer_class not in policy.allowed_layer_classes:
        raise MutabilityViolation(
            f"Cannot apply {target_layer_class.value} to parameter with mutability {mutability_class.value}. "
            f"Allowed: {[l.value for l in policy.allowed_layer_classes]}"
        )
