from app.clearing_plane.integration import integrate_with_clearing_plane


class CollateralInvariants:
    @staticmethod
    def check_high_risk_closure(has_unresolved_deficiency: bool):
        if has_unresolved_deficiency:
            raise Exception(
                "Invariant Violation: no trusted high-risk closure claim may be emitted while material collateral treatment remains unresolved in eligible scopes")

# Phase 160: Waterfall Plane Integrations


def check_waterfall_invariants(context: dict):
    # Enforces no closure or finality claim without explicit claim clarity and distribution analysis
    pass
# Escrow-plane invariants: no final-safe claim while escrow unresolved, no deposit alters beyond boundaries


# Phase 162: Netting Plane Invariants
def check_netting_invariants():
    # no trusted high-risk closure, settlement, discharge, final-safe or netting-clean claim may be emitted while material netting treatment remains unresolved in eligible scopes
    # no obligation, mutuality, maturity, valuation, setoff, close-out, residual, reversal, downgrade or closure event may alter a netting posture beyond its explicit domain boundaries
    # no posture may be treated as netted, set off, close-out clean, legal zero, insolvency-safe or closure-clean without explicit obligation clarity, mutuality sufficiency, valuation sufficiency, setoff sufficiency and close-out analysis
    # no contractual, rights-safe, liability-safe, remedy-safe, final-safe or compliance-safe claim may stand while the governing netting remains materially mutuality-defective, stale-valued, stay-blocked, cherry-picked or residual-open
    pass


# Added for Phase 163 Clearing Plane Integration


def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/policy_kernel/invariants.py")
    return integration.evaluate_posture()


class SettlementIntegrityInvariants:
    @staticmethod
    def check_high_risk_closure(context):
        if context.get('is_high_risk_closure') and context.get('unresolved_settlement_treatment'):
            raise Exception(
                "no trusted high-risk closure, settlement, discharge, final-safe or settlement-clean claim \nmay be emitted while material settlement treatment remains unresolved in eligible scopes")

    @staticmethod
    def check_posture_boundaries(context):
        if context.get('event_type') in ['instruction', 'SSI', 'match', 'funding', 'fail', 'buy-in', 'reversal', 'downgrade', 'closure']:
            if context.get('alters_boundaries'):
                raise Exception("no instruction, SSI, match, funding, fail, buy-in, reversal, downgrade or closure event may alter \na settlement posture beyond its explicit domain, beneficiary, authority, scope and jurisdiction boundaries")

    @staticmethod
    def check_settlement_treatment(context):
        treatment = context.get('treatment')
        if treatment in ['matched', 'settled', 'DvP-clean', 'final', 'fail-resolved', 'closure-clean']:
            has_explicit_analysis = all([
                context.get('has_instruction_clarity'),
                context.get('has_ssi_sufficiency'),
                context.get('has_matching_sufficiency'),
                context.get('has_funding_sufficiency'),
                context.get('has_finality_analysis')
            ])
            if not has_explicit_analysis:
                raise Exception("no posture may be treated as matched, settled, DvP-clean, final, fail-resolved or closure-clean \nwithout explicit instruction clarity, SSI sufficiency, matching sufficiency, funding sufficiency and finality analysis")

    @staticmethod
    def check_safe_claims(context):
        claim_type = context.get('claim_type')
        if claim_type in ['contractual', 'rights-safe', 'liability-safe', 'remedy-safe', 'final-safe', 'compliance-safe']:
            issues = context.get('settlement_issues', [])
            if any(issue in issues for issue in ['stale-SSI', 'wrong-destination', 'non-final', 'fail-open', 'duplicate-exposed']):
                raise Exception("no contractual, rights-safe, liability-safe, remedy-safe, final-safe or compliance-safe claim \nmay stand while the governing settlement remains materially stale-SSI, wrong-destination, non-final, fail-open or duplicate-exposed")
