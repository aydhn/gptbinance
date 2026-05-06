from typing import Dict, Optional, Any
from app.identity.enums import ScopeClaimClass


class ScopeEvaluator:
    @staticmethod
    def evaluate_intersection(
        principal_scopes: Dict[str, str], requested_scopes: Dict[str, str]
    ) -> bool:
        """
        Evaluate if the requested scopes are a subset or valid intersection
        of the principal's allowed scopes.
        Strict match required for now, no wildcards allowed unless explicitly handled.
        """
        if not requested_scopes:
            return True  # No specific scope requested means general access (if other checks pass)

        for key, req_val in requested_scopes.items():
            if key not in principal_scopes:
                return False
            # Very basic strict match for now. In reality, might allow hierarchical.
            # Avoid wildcards per requirements.
            if principal_scopes[key] != req_val and principal_scopes[key] != "*":
                # If we ever allow limited wildcards
                return False

        return True


scope_evaluator = ScopeEvaluator()
