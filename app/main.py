import argparse
import sys
from datetime import datetime, timezone
from app.risk_plane.enums import RiskDomain, LimitClass, BreachClass, DrawdownClass, MarginClass, LiquidationClass
from app.risk_plane.models import RiskLimitDefinition, RiskState, DrawdownState, MarginState, LiquidationProximityState
from app.risk_plane.limits import global_limit_registry
from app.risk_plane.states import CanonicalRiskStateBuilder
from app.risk_plane.breaches import CanonicalBreachClassifier
from app.risk_plane.responses import ResponseIntentEngine
from app.risk_plane.cooldowns import global_cooldown_governance, CooldownClass
from app.risk_plane.reentry import ReentryEvaluator
from app.risk_plane.scenarios import generate_risk_scenarios
from app.risk_plane.equivalence import EquivalenceChecker
from app.risk_plane.trust import TrustedRiskVerdictEngine
from app.risk_plane.reporting import format_risk_summary

def seed_dummy_data():
    global_limit_registry.register_limit(RiskLimitDefinition(
        limit_id="lim_gross_1",
        limit_class=LimitClass.HARD,
        owner_domain="POLICY",
        domain=RiskDomain.ACCOUNT,
        target_id="MAIN",
        value=10000.0,
        description="Max Gross Exposure"
    ))

def main():
    parser = argparse.ArgumentParser(description="Binance Trading Platform - Risk Plane CLI")
    parser.add_argument("--show-risk-limit-registry", action="store_true")
    parser.add_argument("--show-risk-state", action="store_true")
    parser.add_argument("--show-drawdown-state", action="store_true")
    parser.add_argument("--show-loss-state", action="store_true")
    parser.add_argument("--show-margin-liquidation", action="store_true")
    parser.add_argument("--show-risk-breaches", action="store_true")
    parser.add_argument("--show-risk-response-intents", action="store_true")
    parser.add_argument("--show-risk-cooldowns", action="store_true")
    parser.add_argument("--show-reentry-gates", action="store_true")
    parser.add_argument("--show-risk-scenarios", action="store_true")
    parser.add_argument("--show-risk-equivalence", action="store_true")
    parser.add_argument("--show-risk-trust", action="store_true")
    parser.add_argument("--show-risk-review-packs", action="store_true")

    args = parser.parse_args()
    seed_dummy_data()

    builder = CanonicalRiskStateBuilder()
    state = builder.build_risk_state(
        state_id="state_1",
        domain=RiskDomain.ACCOUNT,
        target_id="MAIN",
        authoritative=True,
        source_position_refs=[],
        source_ledger_refs=[],
        source_market_truth_refs=[],
        drawdown=DrawdownState(
            domain=RiskDomain.ACCOUNT,
            target_id="MAIN",
            drawdown_class=DrawdownClass.ACCOUNT,
            realized_drawdown=100.0,
            unrealized_drawdown=50.0,
            peak_value=1000.0,
            current_value=850.0,
            reset_semantics="DAILY",
            proof_notes=[]
        ),
        margin=MarginState(
            margin_class=MarginClass.SAFE,
            margin_usage_ratio=0.2,
            usable_collateral=800.0,
            collateral_fragility_ratio=0.1,
            evidence_refs=[],
            proof_notes=[]
        ),
        liquidation=LiquidationProximityState(
            liquidation_class=LiquidationClass.SAFE,
            proximity_ratio=0.5,
            conservative_buffer=0.4,
            stale_mark_caution=False,
            proof_notes=[]
        )
    )

    classifier = CanonicalBreachClassifier()
    breaches = []
    for limit in global_limit_registry.all_limits():
        # simulate current value of 11000 to trigger breach
        breach = classifier.classify(state, limit, 11000.0)
        if breach:
            breaches.append(breach)

    intent_engine = ResponseIntentEngine()
    intents = intent_engine.generate_intents(breaches)

    if args.show_risk_limit_registry:
        print("=== RISK LIMIT REGISTRY ===")
        for l in global_limit_registry.all_limits():
            print(f"[{l.limit_class.value}] {l.limit_id} on {l.domain.value}:{l.target_id} -> {l.value} ({l.description})")

    elif args.show_risk_state:
        print("=== RISK STATE ===")
        print(f"ID: {state.state_id} | Authoritative: {state.authoritative} | Completeness: {state.completeness_summary}")

    elif args.show_drawdown_state:
        print("=== DRAWDOWN STATE ===")
        print(f"Realized: {state.drawdown.realized_drawdown} | Unrealized: {state.drawdown.unrealized_drawdown}")

    elif args.show_loss_state:
        print("=== LOSS STATE ===")
        print("No active loss state generated for this demo.")

    elif args.show_margin_liquidation:
        print("=== MARGIN & LIQUIDATION ===")
        print(f"Margin Usage: {state.margin.margin_usage_ratio:.2f} ({state.margin.margin_class.value})")
        print(f"Liquidation Buffer: {state.liquidation.conservative_buffer:.2f} ({state.liquidation.liquidation_class.value})")

    elif args.show_risk_breaches:
        print("=== ACTIVE BREACHES ===")
        for b in breaches:
            print(f"[{b.breach_class.value}] Limit: {b.limit_ref.limit_id} | Value: {b.breached_value}")

    elif args.show_risk_response_intents:
        print("=== RESPONSE INTENTS ===")
        for i in intents:
            print(f"[{i.response_class.value}] Target: {i.target_domain.value}:{i.target_id} | Rationale: {i.rationale}")

    elif args.show_risk_cooldowns:
        global_cooldown_governance.apply_cooldown(RiskDomain.ACCOUNT, "MAIN", CooldownClass.POST_BREACH, 60, "Limit Breach")
        print("=== ACTIVE COOLDOWNS ===")
        for c in global_cooldown_governance.get_active_cooldowns():
            print(f"[{c.cooldown_class.value}] Expires: {c.end_time} | Reason: {c.reason}")

    elif args.show_reentry_gates:
        global_cooldown_governance.apply_cooldown(RiskDomain.ACCOUNT, "MAIN", CooldownClass.POST_BREACH, 60, "Limit Breach")
        evaluator = ReentryEvaluator()
        gate = evaluator.evaluate(RiskDomain.ACCOUNT, "MAIN", state, active_cooldowns=True)
        print("=== RE-ENTRY GATES ===")
        print(f"Cleared: {gate.cleared}")
        for r in gate.requirements:
            print(f"- {r}")

    elif args.show_risk_scenarios:
        print("=== RISK SCENARIOS ===")
        for s in generate_risk_scenarios(exposure=10000, margin_usage=0.2):
            print(f"{s.description}: {s.burden_summary}")

    elif args.show_risk_equivalence:
        print("=== RISK EQUIVALENCE ===")
        checker = EquivalenceChecker()
        rep = checker.check_equivalence(state, state)
        print(f"Verdict: {rep.verdict.value} | Divergences: {len(rep.divergence_sources)}")

    elif args.show_risk_trust:
        print("=== RISK TRUST VERDICT ===")
        trust_engine = TrustedRiskVerdictEngine()
        verdict = trust_engine.evaluate([state], breaches)
        print(format_risk_summary([state], breaches, intents, verdict))

    elif args.show_risk_review_packs:
        print("=== RISK REVIEW PACKS ===")
        print("Packs: [Risk Integrity Pack, Cooldown/Reentry Pack]")
        print("Completeness: 100% | Freshness: Just now")

    else:
        print("Binance Trading Platform Risk Plane. Run with a flag like --show-risk-limit-registry.")

if __name__ == "__main__":
    main()
