from typing import List, Dict, Optional
from app.remediation.models import RemediationRecipe
from app.remediation.enums import RemediationClass, ApplyMode


class RecipeRegistry:
    def __init__(self):
        self._recipes: Dict[str, RemediationRecipe] = {
            "refresh_venue_shadow_snapshot": RemediationRecipe(
                recipe_id="refresh_venue_shadow_snapshot",
                name="Refresh Venue Shadow Snapshot",
                safety_class=RemediationClass.READ_ONLY,
                supported_finding_sources=["shadow_state"],
                allowed_apply_modes=[ApplyMode.DIRECT_SAFE],
                requires_approval=False,
            ),
            "rerun_lifecycle_reconciliation": RemediationRecipe(
                recipe_id="rerun_lifecycle_reconciliation",
                name="Rerun Lifecycle Reconciliation",
                safety_class=RemediationClass.LOCAL_RECOMPUTE,
                supported_finding_sources=["order_lifecycle"],
                allowed_apply_modes=[ApplyMode.DIRECT_SAFE],
                requires_approval=False,
            ),
            "rebuild_crossbook_posture": RemediationRecipe(
                recipe_id="rebuild_crossbook_posture",
                name="Rebuild Cross-Book Posture",
                safety_class=RemediationClass.LOCAL_RECOMPUTE,
                supported_finding_sources=["crossbook"],
                allowed_apply_modes=[ApplyMode.DIRECT_SAFE],
                requires_approval=False,
            ),
            "refresh_account_mode_truth": RemediationRecipe(
                recipe_id="refresh_account_mode_truth",
                name="Refresh Account Mode Truth",
                safety_class=RemediationClass.READ_ONLY,
                supported_finding_sources=["shadow_state", "qualification"],
                allowed_apply_modes=[ApplyMode.DIRECT_SAFE],
                requires_approval=False,
            ),
            "rerun_ledger_reconciliation": RemediationRecipe(
                recipe_id="rerun_ledger_reconciliation",
                name="Rerun Ledger Reconciliation",
                safety_class=RemediationClass.LOCAL_RECOMPUTE,
                supported_finding_sources=["ledger"],
                allowed_apply_modes=[ApplyMode.DIRECT_SAFE],
                requires_approval=False,
            ),
            "quarantine_symbol_universe": RemediationRecipe(
                recipe_id="quarantine_symbol_universe",
                name="Quarantine Symbol from Universe",
                safety_class=RemediationClass.APPROVAL_BOUND_LOCAL,
                supported_finding_sources=["crossbook", "universe"],
                allowed_apply_modes=[
                    ApplyMode.REQUEST_GENERATION,
                    ApplyMode.MANUAL_INSTRUCTION,
                ],
                requires_approval=True,
            ),
            "freeze_capital_advisory_request": RemediationRecipe(
                recipe_id="freeze_capital_advisory_request",
                name="Request Capital Freeze",
                safety_class=RemediationClass.APPROVAL_BOUND_LOCAL,
                supported_finding_sources=["capital"],
                allowed_apply_modes=[ApplyMode.REQUEST_GENERATION],
                requires_approval=True,
            ),
            "request_orphan_order_review": RemediationRecipe(
                recipe_id="request_orphan_order_review",
                name="Request Orphan Order Review",
                safety_class=RemediationClass.VENUE_AFFECTING,
                supported_finding_sources=["order_lifecycle"],
                allowed_apply_modes=[ApplyMode.REQUEST_GENERATION],
                requires_approval=True,
            ),
            "request_balance_investigation": RemediationRecipe(
                recipe_id="request_balance_investigation",
                name="Request Balance Investigation",
                safety_class=RemediationClass.REVIEW_ONLY,
                supported_finding_sources=["ledger"],
                allowed_apply_modes=[ApplyMode.REQUEST_GENERATION],
                requires_approval=True,
            ),
            "rerun_qualification_evidence": RemediationRecipe(
                recipe_id="rerun_qualification_evidence",
                name="Rerun Qualification Evidence",
                safety_class=RemediationClass.LOCAL_RECOMPUTE,
                supported_finding_sources=["qualification"],
                allowed_apply_modes=[ApplyMode.DIRECT_SAFE],
                requires_approval=False,
            ),
            "rerun_stress_evidence": RemediationRecipe(
                recipe_id="rerun_stress_evidence",
                name="Rerun Stress Evidence",
                safety_class=RemediationClass.LOCAL_RECOMPUTE,
                supported_finding_sources=["stressrisk"],
                allowed_apply_modes=[ApplyMode.DIRECT_SAFE],
                requires_approval=False,
            ),
            "mark_workspace_degraded": RemediationRecipe(
                recipe_id="mark_workspace_degraded",
                name="Mark Workspace Degraded",
                safety_class=RemediationClass.APPROVAL_BOUND_LOCAL,
                supported_finding_sources=[
                    "shadow_state",
                    "order_lifecycle",
                    "qualification",
                    "workspace",
                ],
                allowed_apply_modes=[
                    ApplyMode.REQUEST_GENERATION,
                    ApplyMode.MANUAL_INSTRUCTION,
                ],
                requires_approval=True,
            ),
            "invalidate_stale_cache": RemediationRecipe(
                recipe_id="invalidate_stale_cache",
                name="Invalidate Stale Cache",
                safety_class=RemediationClass.LOCAL_RECOMPUTE,
                supported_finding_sources=[
                    "shadow_state",
                    "qualification",
                    "crossbook",
                ],
                allowed_apply_modes=[ApplyMode.DIRECT_SAFE],
                requires_approval=False,
            ),
            "request_live_action_review": RemediationRecipe(
                recipe_id="request_live_action_review",
                name="Request Live Action Review",
                safety_class=RemediationClass.VENUE_AFFECTING,
                supported_finding_sources=["order_lifecycle", "capital"],
                allowed_apply_modes=[ApplyMode.REQUEST_GENERATION],
                requires_approval=True,
            ),
        }

    def get_recipe(self, recipe_id: str) -> Optional[RemediationRecipe]:
        return self._recipes.get(recipe_id)

    def find_recipes_for_source(self, source_domain: str) -> List[RemediationRecipe]:
        return [
            r
            for r in self._recipes.values()
            if source_domain in r.supported_finding_sources
        ]
