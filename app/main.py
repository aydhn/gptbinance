import argparse
from app.insolvency_plane.repository import InsolvencyRepository

def main():
    parser = argparse.ArgumentParser(description="Insolvency Plane CLI")
    parser.add_argument("--show-insolvency-registry", action="store_true")
    parser.add_argument("--show-insolvency-object", action="store_true")
    parser.add_argument("--insolvency-id", type=str)
    parser.add_argument("--show-insolvencies", action="store_true")
    parser.add_argument("--show-distress-triggers", action="store_true")
    parser.add_argument("--show-estates", action="store_true")
    parser.add_argument("--show-estate-assets", action="store_true")
    parser.add_argument("--show-estate-scope", action="store_true")
    parser.add_argument("--show-insolvency-claims", action="store_true")
    parser.add_argument("--show-claim-admission", action="store_true")
    parser.add_argument("--show-claim-objections", action="store_true")
    parser.add_argument("--show-secured-claims", action="store_true")
    parser.add_argument("--show-unsecured-claims", action="store_true")
    parser.add_argument("--show-priority-claims", action="store_true")
    parser.add_argument("--show-subordination", action="store_true")
    parser.add_argument("--show-administrative-claims", action="store_true")
    parser.add_argument("--show-stays", action="store_true")
    parser.add_argument("--show-stay-scope", action="store_true")
    parser.add_argument("--show-moratoria", action="store_true")
    parser.add_argument("--show-avoidance", action="store_true")
    parser.add_argument("--show-preference-risk", action="store_true")
    parser.add_argument("--show-fraud-like-transfers", action="store_true")
    parser.add_argument("--show-dip-support", action="store_true")
    parser.add_argument("--show-restructuring-plans", action="store_true")
    parser.add_argument("--show-plan-classes", action="store_true")
    parser.add_argument("--show-plan-support", action="store_true")
    parser.add_argument("--show-confirmation", action="store_true")
    parser.add_argument("--show-cures", action="store_true")
    parser.add_argument("--show-haircuts", action="store_true")
    parser.add_argument("--show-assumption-rejection", action="store_true")
    parser.add_argument("--show-liquidation", action="store_true")
    parser.add_argument("--show-going-concern", action="store_true")
    parser.add_argument("--show-distribution-loss", action="store_true")
    parser.add_argument("--show-post-confirmation-duties", action="store_true")
    parser.add_argument("--show-residual-deficits", action="store_true")
    parser.add_argument("--show-insolvency-comparisons", action="store_true")
    parser.add_argument("--show-insolvency-readiness", action="store_true")
    parser.add_argument("--show-insolvency-forecast", action="store_true")
    parser.add_argument("--show-insolvency-debt", action="store_true")
    parser.add_argument("--show-insolvency-equivalence", action="store_true")
    parser.add_argument("--show-insolvency-trust", action="store_true")
    parser.add_argument("--show-insolvency-review-packs", action="store_true")

    args = parser.parse_args()
    repo = InsolvencyRepository()

    if args.show_insolvency_registry:
        objects = repo.registry.list_all()
        print(f"Insolvency Registry: {len(objects)} objects")
        for obj in objects:
            print(f"  - {obj.id} ({obj.class_type}) Owner: {obj.owner}")

    elif args.show_insolvency_object:
        if not args.insolvency_id:
            print("Error: --insolvency-id required")
        else:
            obj = repo.registry.get(args.insolvency_id)
            if obj:
                print(f"Insolvency Object {args.insolvency_id}:")
                print(f"  Class: {obj.class_type}")
                print(f"  Owner: {obj.owner}")
                print(f"  Scope: {obj.scope}")
            else:
                print(f"Insolvency Object {args.insolvency_id}: [Not Found]")

    elif args.show_insolvencies:
        items = repo.insolvency_manager.list_insolvencies()
        print(f"Insolvencies: {len(items)}")
    elif args.show_distress_triggers:
        items = repo.trigger_manager.list_triggers()
        print(f"Distress Triggers: {len(items)}")
    elif args.show_estates:
        items = repo.estate_manager.list_estates()
        print(f"Estates: {len(items)}")
    elif args.show_estate_assets:
        items = repo.estate_asset_manager.list_assets()
        print(f"Estate Assets: {len(items)}")
    elif args.show_estate_scope:
        items = repo.estate_scope_manager.list_scopes()
        print(f"Estate Scopes: {len(items)}")
    elif args.show_insolvency_claims:
        items = repo.claim_manager.list_claims()
        print(f"Claims: {len(items)}")
    elif args.show_claim_admission:
        items = repo.admission_manager.list_admissions()
        print(f"Claim Admissions: {len(items)}")
    elif args.show_claim_objections:
        items = repo.objection_manager.list_objections()
        print(f"Claim Objections: {len(items)}")
    elif args.show_secured_claims:
        items = repo.secured_claim_manager.list_secured_claims()
        print(f"Secured Claims: {len(items)}")
    elif args.show_unsecured_claims:
        items = repo.unsecured_claim_manager.list_unsecured_claims()
        print(f"Unsecured Claims: {len(items)}")
    elif args.show_priority_claims:
        items = repo.priority_claim_manager.list_priority_claims()
        print(f"Priority Claims: {len(items)}")
    elif args.show_subordination:
        items = repo.subordination_manager.list_subordinated_claims()
        print(f"Subordinated Claims: {len(items)}")
    elif args.show_administrative_claims:
        items = repo.administrative_claim_manager.list_administrative_claims()
        print(f"Administrative Claims: {len(items)}")
    elif args.show_stays:
        items = repo.stay_manager.list_stays()
        print(f"Stays: {len(items)}")
    elif args.show_stay_scope:
        items = repo.stay_scope_manager.list_scopes()
        print(f"Stay Scopes: {len(items)}")
    elif args.show_moratoria:
        items = repo.moratorium_manager.list_moratoria()
        print(f"Moratoria: {len(items)}")
    elif args.show_avoidance:
        items = repo.avoidance_manager.list_avoidances()
        print(f"Avoidances: {len(items)}")
    elif args.show_preference_risk:
        items = repo.preference_risk_manager.list_preference_risks()
        print(f"Preference Risks: {len(items)}")
    elif args.show_fraud_like_transfers:
        items = repo.fraud_transfer_manager.list_fraud_transfers()
        print(f"Fraud-like Transfers: {len(items)}")
    elif args.show_dip_support:
        items = repo.dip_support_manager.list_dip_supports()
        print(f"DIP Supports: {len(items)}")
    elif args.show_restructuring_plans:
        items = repo.plan_manager.list_plans()
        print(f"Restructuring Plans: {len(items)}")
    elif args.show_plan_classes:
        items = repo.plan_class_manager.list_plan_classes()
        print(f"Plan Classes: {len(items)}")
    elif args.show_plan_support:
        items = repo.plan_support_manager.list_supports()
        print(f"Plan Supports: {len(items)}")
    elif args.show_confirmation:
        items = repo.confirmation_manager.list_confirmations()
        print(f"Confirmations: {len(items)}")
    elif args.show_cures:
        items = repo.cure_manager.list_cures()
        print(f"Cures: {len(items)}")
    elif args.show_haircuts:
        items = repo.haircut_manager.list_haircuts()
        print(f"Haircuts: {len(items)}")
    elif args.show_assumption_rejection:
        items = repo.assumption_rejection_manager.list_actions()
        print(f"Assumption/Rejections: {len(items)}")
    elif args.show_liquidation:
        items = repo.liquidation_manager.list_liquidations()
        print(f"Liquidations: {len(items)}")
    elif args.show_going_concern:
        items = repo.going_concern_manager.list_going_concerns()
        print(f"Going Concerns: {len(items)}")
    elif args.show_distribution_loss:
        items = repo.distribution_loss_manager.list_losses()
        print(f"Distribution Losses: {len(items)}")
    elif args.show_post_confirmation_duties:
        items = repo.post_confirmation_manager.list_duties()
        print(f"Post-Confirmation Duties: {len(items)}")
    elif args.show_residual_deficits:
        items = repo.residual_deficit_manager.list_deficits()
        print(f"Residual Deficits: {len(items)}")
    elif args.show_insolvency_comparisons:
        items = repo.comparison_manager.list_comparisons()
        print(f"Comparisons: {len(items)}")
    elif args.show_insolvency_readiness:
        items = repo.readiness_manager.list_reports()
        print(f"Readiness Reports: {len(items)}")
    elif args.show_insolvency_forecast:
        items = repo.forecast_manager.list_forecasts()
        print(f"Forecasts: {len(items)}")
    elif args.show_insolvency_debt:
        items = repo.debt_manager.list_debts()
        print(f"Insolvency Debts: {len(items)}")
    elif args.show_insolvency_equivalence:
        items = repo.equivalence_manager.list_reports()
        print(f"Equivalence Reports: {len(items)}")
    elif args.show_insolvency_trust:
        items = repo.trust_manager.list_reports()
        print(f"Trust Reports: {len(items)}")
    elif args.show_insolvency_review_packs:
        print("Insolvency Review Packs: 0")
    else:
        print("Insolvency Plane CLI. Use --help to see available commands.")

if __name__ == "__main__":
    main()
