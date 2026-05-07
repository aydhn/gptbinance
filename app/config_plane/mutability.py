from app.config_plane.models import MutabilityPolicy
from app.config_plane.enums import MutabilityClass, LayerClass
from app.config_plane.exceptions import MutabilityViolation


class MutabilityGovernance:
    def __init__(self):
        self.policies = {
            MutabilityClass.IMMUTABLE: MutabilityPolicy(
                mutability_class=MutabilityClass.IMMUTABLE, allowed_patch_classes=[]
            ),
            MutabilityClass.RUNTIME_SAFE: MutabilityPolicy(
                mutability_class=MutabilityClass.RUNTIME_SAFE,
                allowed_patch_classes=[LayerClass.RUNTIME_SAFE_PATCH_INTENT],
            ),
        }

    def check_mutation(self, mutability_class: MutabilityClass, layer: LayerClass):
        policy = self.policies.get(mutability_class)
        if policy and layer not in policy.allowed_patch_classes:
            raise MutabilityViolation(
                f"Layer {layer} not allowed to patch class {mutability_class}"
            )
