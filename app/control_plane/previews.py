from app.control_plane.models import ActionRequest, ActionPreview
from app.control_plane.enums import PreviewClass


class PreviewEngine:
    def generate_preview(self, request: ActionRequest) -> ActionPreview:
        return ActionPreview(
            action_id=request.action_id,
            preview_class=PreviewClass.FULL_FIDELITY,
            affected_entities=[f"Entity-{request.scope_ref}"],
            blocked_downstream_actions=["automated_trading_cycle"],
            blast_radius_summary=f"Affects {request.scope_class.value} = {request.scope_ref}",
            reversibility_summary="Can be unfreezed or resumed.",
        )

class ControlPreviewMigrationRef:
    def blast_radius(self, rollback_surfaces=None):
        pass

class ControlPreviewSecurityRef:
    def add_security_metrics(self, preview: ActionPreview, security_blast_radius: str, credential_spread: str):
         preview.blast_radius_summary += f" | Security Blast: {security_blast_radius} | Spread: {credential_spread}"
