import argparse
from app.research_plane.repository import ResearchRepository
from app.research_plane.reporting import ResearchReporter
import json

def run_research_cli(args):
    repo = ResearchRepository()
    reporter = ResearchReporter(repo)

    if args.show_research_registry:
        print(reporter.summary())
    elif args.show_research_item:
        print(reporter.item_details(args.show_research_item))
    elif args.show_research_questions:
        print("Showing Questions...")
        for item in repo.list_all():
            if item.question:
                print(f"[{item.research_id}] {item.question.text} (Falsifiable: {item.question.falsifiable})")
    elif args.show_research_observations:
        print("Showing Observations...")
        for item in repo.list_all():
            for obs in item.observations:
                print(f"[{item.research_id}] {obs.source}: {obs.text} (Conf: {obs.confidence_score})")
    elif args.show_research_hypotheses:
        print("Showing Hypotheses...")
        for item in repo.list_all():
            for hyp in item.hypotheses:
                print(f"[{item.research_id}] Effect: {hyp.claimed_effect} | Mech: {hyp.expected_mechanism}")
    elif args.show_research_evidence:
        print("Showing Evidence...")
        for item in repo.list_all():
             for bundle in item.evidence_bundles:
                 print(f"[{item.research_id}] Bundle {bundle.bundle_id}: {len(bundle.entries)} entries")
    elif args.show_research_contradictions:
         print("Showing Contradictions...")
         for item in repo.list_all():
             for cont in item.contradictions:
                 print(f"[{item.research_id}] {cont.contradiction_class.name}: {cont.description} (Unresolved: {cont.unresolved_burden})")
    elif args.show_research_confidence:
         print("Showing Confidence...")
         for item in repo.list_all():
             if item.confidence:
                 print(f"[{item.research_id}] Current: {item.confidence.current_class.name} (Prev: {item.confidence.previous_class.name if item.confidence.previous_class else 'None'})")
    elif args.show_research_readiness:
         from app.research_plane.readiness import ReadinessEvaluator
         print("Showing Readiness...")
         evaluator = ReadinessEvaluator()
         for item in repo.list_all():
             r = evaluator.evaluate(item)
             print(f"[{item.research_id}] {r.readiness_class.name} - Blockers: {r.blockers}")
    elif args.show_research_overlap:
         from app.research_plane.overlap import OverlapDetector
         print("Showing Overlap...")
         detector = OverlapDetector()
         all_items = repo.list_all()
         for item in all_items:
             ov = detector.detect_overlap(item, all_items)
             print(f"[{item.research_id}] Severity: {ov.severity.name} - {ov.description}")
    elif args.show_research_maturation:
         from app.research_plane.maturation import MaturationAnalytics
         print("Showing Maturation...")
         analytics = MaturationAnalytics()
         for item in repo.list_all():
             m = analytics.analyze(item)
             print(f"[{item.research_id}] Stagnant: {m.stagnation_detected}, Candidate: {m.maturation_to_candidate}, Dead End: {m.dead_end}")
    elif args.show_research_equivalence:
         # Simplified for CLI
         print("Equivalence checking requires 2 items.")
    elif args.show_research_trust:
         from app.research_plane.trust import TrustVerdictEngine
         print("Showing Trust...")
         engine = TrustVerdictEngine()
         for item in repo.list_all():
             t = engine.evaluate(item)
             print(f"[{item.research_id}] Verdict: {t.verdict.name} Caveats: {t.caveats}")
    elif args.show_research_review_packs:
         print("Review packs generated from manifests.")
    else:
        print("No specific research command provided. Use --help")
