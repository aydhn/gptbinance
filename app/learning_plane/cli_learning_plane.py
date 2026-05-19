import argparse
from typing import List, Dict, Any

from app.learning_plane.models import (
    LearningClass, SignalClass, OriginClass, OutcomeClass, FailureClass,
    FindingClass, LessonClass, HardeningClass, ValidationClass, RecurrenceClass,
    EquivalenceVerdict, TrustVerdict, ReadinessClass, UncertaintyClass, AdoptionStatus
)
from app.learning_plane.storage import storage
from app.learning_plane.registry import CanonicalLearningRegistry
from app.learning_plane.trust import TrustedLearningVerdictEngine
from app.learning_plane.equivalence import EquivalenceAnalyzer

registry = CanonicalLearningRegistry()
trust_engine = TrustedLearningVerdictEngine(registry)

def show_learning_registry():
    print("=== Canonical Learning Registry ===")
    objects = registry.get_all_objects()
    for obj in objects:
        print(f"- ID: {obj.learning_id} | Class: {obj.learning_class.value} | State: {obj.state}")

def show_learning_object(learning_id: str):
    print(f"=== Learning Object: {learning_id} ===")
    try:
        obj = registry.get_object(learning_id)
        print(f"Class: {obj.learning_class.value}")
        print(f"Owner: {obj.owner}")
        print(f"Scope: {obj.scope}")
        print(f"Origin ID: {obj.origin_id}")
        print(f"Signals: {obj.signal_ids}")
        print(f"Findings: {obj.finding_ids}")
        print(f"Lessons: {obj.lesson_ids}")
        print(f"Hardening Actions: {obj.action_ids}")
        print(f"Validations: {obj.validation_ids}")
        print(f"Recurrences: {obj.recurrence_ids}")
    except Exception as e:
        print(f"Error: {e}")

def show_learning_signals():
    print("=== Learning Signals ===")
    for sig in storage.signals.values():
        print(f"- {sig.signal_id} ({sig.signal_class.value}): {sig.description}")

def show_learning_origins():
    print("=== Learning Origins ===")
    for origin in storage.origins.values():
        print(f"- {origin.origin_id} ({origin.origin_class.value}): {origin.description}")

def show_learning_outcomes():
    print("=== Learning Outcomes ===")
    for out in storage.outcomes.values():
        print(f"- {out.outcome_id} ({out.outcome_class.value}): {out.description}")

def show_failure_classes():
    print("=== Failure Classes ===")
    for fc in storage.failure_classes.values():
        print(f"- {fc.failure_class_id} ({fc.failure_class.value}): {fc.description}")

def show_near_misses():
    print("=== Near Misses ===")
    for nm in storage.near_misses.values():
        print(f"- {nm.near_miss_id}: {nm.description}")

def show_avoided_failures():
    print("=== Avoided Failures ===")
    for af in storage.avoided_failures.values():
        print(f"- {af.avoided_failure_id}: {af.description}")

def show_findings():
    print("=== Findings ===")
    for finding in storage.findings.values():
        print(f"- {finding.finding_id} ({finding.finding_class.value}): {finding.description}")

def show_causal_hypotheses():
    print("=== Causal Hypotheses ===")
    for hyp in storage.hypotheses.values():
        print(f"- {hyp.hypothesis_id}: {hyp.description}")

def show_validated_causes():
    print("=== Validated Causes ===")
    for cause in storage.causes.values():
        print(f"- {cause.cause_id}: {cause.description}")

def show_lessons():
    print("=== Lessons ===")
    for lesson in storage.lessons.values():
        print(f"- {lesson.lesson_id} ({lesson.lesson_class.value}): {lesson.description}")

def show_lesson_scopes():
    print("=== Lesson Scopes ===")
    for scope in storage.scopes.values():
        print(f"- {scope.scope_id}: {scope.description}")

def show_hardening_actions():
    print("=== Hardening Actions ===")
    for action in storage.actions.values():
        print(f"- {action.action_id} ({action.hardening_class.value}): {action.description}")

def show_update_targets():
    print("=== Update Targets ===")
    for target in storage.targets.values():
        print(f"- {target.target_id}: {target.description}")

def show_learning_adoption():
    print("=== Learning Adoption ===")
    for adoption in storage.adoptions.values():
        print(f"- {adoption.adoption_id} ({adoption.status.value}): {adoption.description}")

def show_learning_validation():
    print("=== Learning Validation ===")
    for validation in storage.validations.values():
        print(f"- {validation.validation_id} ({validation.validation_class.value}): {validation.description}")

def show_recurrence():
    print("=== Recurrences ===")
    for recurrence in storage.recurrences.values():
        print(f"- {recurrence.recurrence_id} ({recurrence.recurrence_class.value}): {recurrence.description}")

def show_learning_precedents():
    print("=== Learning Precedents ===")
    for precedent in storage.precedents.values():
        print(f"- {precedent.precedent_id}: {precedent.description}")

def show_learning_comparisons():
    print("=== Learning Comparisons ===")
    for comparison in storage.comparisons.values():
        print(f"- {comparison.comparison_id}: {comparison.description}")

def show_learning_forecast():
    print("=== Learning Forecast ===")
    for forecast in storage.forecasts.values():
         print(f"- {forecast.forecast_id}: Likelihood {forecast.recurrence_likelihood}")

def show_learning_debt():
    print("=== Learning Debt ===")
    for debt in storage.debts.values():
         print(f"- {debt.debt_id}: {debt.description}")

def show_learning_readiness():
    print("=== Learning Readiness ===")
    # Stub

def show_learning_equivalence():
    print("=== Learning Equivalence ===")
    for r in storage.equivalence_reports.values():
        print(f"- {r.report_id}: {r.verdict.value}")

def show_learning_trust(learning_id: str):
    print(f"=== Learning Trust: {learning_id} ===")
    try:
        verdict = trust_engine.evaluate_trust(learning_id)
        print(f"Verdict: {verdict.verdict.value}")
        print("Factors:")
        for k, v in verdict.factors.items():
            print(f"  {k}: {v}")
        print("Caveats:")
        for c in verdict.caveats:
            print(f"  - {c}")
    except Exception as e:
        print(f"Error: {e}")

def show_learning_review_packs():
    print("=== Learning Review Packs ===")
    # Stub

def register_cli_args(subparsers):
    parser = subparsers.add_parser("learning")
    parser.add_argument("--show-learning-registry", action="store_true")
    parser.add_argument("--show-learning-object", action="store_true")
    parser.add_argument("--learning-id", type=str)
    parser.add_argument("--show-learning-signals", action="store_true")
    parser.add_argument("--show-learning-origins", action="store_true")
    parser.add_argument("--show-learning-outcomes", action="store_true")
    parser.add_argument("--show-failure-classes", action="store_true")
    parser.add_argument("--show-near-misses", action="store_true")
    parser.add_argument("--show-avoided-failures", action="store_true")
    parser.add_argument("--show-findings", action="store_true")
    parser.add_argument("--show-causal-hypotheses", action="store_true")
    parser.add_argument("--show-validated-causes", action="store_true")
    parser.add_argument("--show-lessons", action="store_true")
    parser.add_argument("--show-lesson-scopes", action="store_true")
    parser.add_argument("--show-hardening-actions", action="store_true")
    parser.add_argument("--show-update-targets", action="store_true")
    parser.add_argument("--show-learning-adoption", action="store_true")
    parser.add_argument("--show-learning-validation", action="store_true")
    parser.add_argument("--show-recurrence", action="store_true")
    parser.add_argument("--show-learning-precedents", action="store_true")
    parser.add_argument("--show-learning-comparisons", action="store_true")
    parser.add_argument("--show-learning-forecast", action="store_true")
    parser.add_argument("--show-learning-debt", action="store_true")
    parser.add_argument("--show-learning-readiness", action="store_true")
    parser.add_argument("--show-learning-equivalence", action="store_true")
    parser.add_argument("--show-learning-trust", action="store_true")
    parser.add_argument("--show-learning-review-packs", action="store_true")

def handle_cli(args):
    if args.show_learning_registry:
        show_learning_registry()
    elif args.show_learning_object and args.learning_id:
        show_learning_object(args.learning_id)
    elif args.show_learning_signals:
        show_learning_signals()
    elif args.show_learning_origins:
        show_learning_origins()
    elif args.show_learning_outcomes:
        show_learning_outcomes()
    elif args.show_failure_classes:
        show_failure_classes()
    elif args.show_near_misses:
        show_near_misses()
    elif args.show_avoided_failures:
        show_avoided_failures()
    elif args.show_findings:
        show_findings()
    elif args.show_causal_hypotheses:
        show_causal_hypotheses()
    elif args.show_validated_causes:
        show_validated_causes()
    elif args.show_lessons:
        show_lessons()
    elif args.show_lesson_scopes:
        show_lesson_scopes()
    elif args.show_hardening_actions:
        show_hardening_actions()
    elif args.show_update_targets:
        show_update_targets()
    elif args.show_learning_adoption:
        show_learning_adoption()
    elif args.show_learning_validation:
        show_learning_validation()
    elif args.show_recurrence:
        show_recurrence()
    elif args.show_learning_precedents:
        show_learning_precedents()
    elif args.show_learning_comparisons:
        show_learning_comparisons()
    elif args.show_learning_forecast:
        show_learning_forecast()
    elif args.show_learning_debt:
        show_learning_debt()
    elif args.show_learning_readiness:
        show_learning_readiness()
    elif args.show_learning_equivalence:
        show_learning_equivalence()
    elif args.show_learning_trust and args.learning_id:
        show_learning_trust(args.learning_id)
    elif args.show_learning_review_packs:
        show_learning_review_packs()
