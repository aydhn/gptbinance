class CollateralInvariants:
    @staticmethod
    def check_high_risk_closure(has_unresolved_deficiency: bool):
        if has_unresolved_deficiency:
            raise Exception("Invariant Violation: no trusted high-risk closure claim may be emitted while material collateral treatment remains unresolved in eligible scopes")
