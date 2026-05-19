from typing import Dict, List, Optional
from app.learning_plane.models import (
    LearningObject, LearningSignalRecord, LearningOriginRecord, OutcomeRecord,
    FailureClassRecord, NearMissRecord, AvoidedFailureRecord, FindingRecord,
    CausalHypothesisRecord, ValidatedCauseRecord, LessonRecord, ScopeOfLessonRecord,
    HardeningActionRecord, UpdateTargetRecord, AdoptionRecord, ValidationRecord,
    RecurrenceRecord, PrecedentLearningRecord, LearningComparisonRecord,
    LearningForecastReport, LearningDebtRecord, LearningEquivalenceReport,
    LearningDivergenceReport, LearningTrustVerdict, LearningArtifactManifest
)
from app.learning_plane.exceptions import LearningStorageError

class LearningStorage:
    def __init__(self):
        self.objects: Dict[str, LearningObject] = {}
        self.signals: Dict[str, LearningSignalRecord] = {}
        self.origins: Dict[str, LearningOriginRecord] = {}
        self.outcomes: Dict[str, OutcomeRecord] = {}
        self.failure_classes: Dict[str, FailureClassRecord] = {}
        self.near_misses: Dict[str, NearMissRecord] = {}
        self.avoided_failures: Dict[str, AvoidedFailureRecord] = {}
        self.findings: Dict[str, FindingRecord] = {}
        self.hypotheses: Dict[str, CausalHypothesisRecord] = {}
        self.causes: Dict[str, ValidatedCauseRecord] = {}
        self.lessons: Dict[str, LessonRecord] = {}
        self.scopes: Dict[str, ScopeOfLessonRecord] = {}
        self.actions: Dict[str, HardeningActionRecord] = {}
        self.targets: Dict[str, UpdateTargetRecord] = {}
        self.adoptions: Dict[str, AdoptionRecord] = {}
        self.validations: Dict[str, ValidationRecord] = {}
        self.recurrences: Dict[str, RecurrenceRecord] = {}
        self.precedents: Dict[str, PrecedentLearningRecord] = {}
        self.comparisons: Dict[str, LearningComparisonRecord] = {}
        self.forecasts: Dict[str, LearningForecastReport] = {}
        self.debts: Dict[str, LearningDebtRecord] = {}
        self.equivalence_reports: Dict[str, LearningEquivalenceReport] = {}
        self.divergence_reports: Dict[str, LearningDivergenceReport] = {}
        self.trust_verdicts: Dict[str, LearningTrustVerdict] = {}
        self.manifests: Dict[str, LearningArtifactManifest] = {}

    def save_object(self, obj: LearningObject) -> None:
        self.objects[obj.learning_id] = obj

    def get_object(self, obj_id: str) -> Optional[LearningObject]:
        return self.objects.get(obj_id)

    def save_signal(self, sig: LearningSignalRecord) -> None:
        self.signals[sig.signal_id] = sig

    def get_signal(self, sig_id: str) -> Optional[LearningSignalRecord]:
        return self.signals.get(sig_id)

    def save_origin(self, origin: LearningOriginRecord) -> None:
        self.origins[origin.origin_id] = origin

    def get_origin(self, origin_id: str) -> Optional[LearningOriginRecord]:
        return self.origins.get(origin_id)

    def save_outcome(self, outcome: OutcomeRecord) -> None:
        self.outcomes[outcome.outcome_id] = outcome

    def get_outcome(self, outcome_id: str) -> Optional[OutcomeRecord]:
        return self.outcomes.get(outcome_id)

    def save_failure_class(self, fc: FailureClassRecord) -> None:
        self.failure_classes[fc.failure_class_id] = fc

    def get_failure_class(self, fc_id: str) -> Optional[FailureClassRecord]:
        return self.failure_classes.get(fc_id)

    def save_near_miss(self, nm: NearMissRecord) -> None:
        self.near_misses[nm.near_miss_id] = nm

    def get_near_miss(self, nm_id: str) -> Optional[NearMissRecord]:
        return self.near_misses.get(nm_id)

    def save_avoided_failure(self, af: AvoidedFailureRecord) -> None:
        self.avoided_failures[af.avoided_failure_id] = af

    def get_avoided_failure(self, af_id: str) -> Optional[AvoidedFailureRecord]:
        return self.avoided_failures.get(af_id)

    def save_finding(self, finding: FindingRecord) -> None:
        self.findings[finding.finding_id] = finding

    def get_finding(self, finding_id: str) -> Optional[FindingRecord]:
        return self.findings.get(finding_id)

    def save_hypothesis(self, hyp: CausalHypothesisRecord) -> None:
        self.hypotheses[hyp.hypothesis_id] = hyp

    def get_hypothesis(self, hyp_id: str) -> Optional[CausalHypothesisRecord]:
        return self.hypotheses.get(hyp_id)

    def save_cause(self, cause: ValidatedCauseRecord) -> None:
        self.causes[cause.cause_id] = cause

    def get_cause(self, cause_id: str) -> Optional[ValidatedCauseRecord]:
        return self.causes.get(cause_id)

    def save_lesson(self, lesson: LessonRecord) -> None:
        self.lessons[lesson.lesson_id] = lesson

    def get_lesson(self, lesson_id: str) -> Optional[LessonRecord]:
        return self.lessons.get(lesson_id)

    def save_scope(self, scope: ScopeOfLessonRecord) -> None:
        self.scopes[scope.scope_id] = scope

    def get_scope(self, scope_id: str) -> Optional[ScopeOfLessonRecord]:
        return self.scopes.get(scope_id)

    def save_action(self, action: HardeningActionRecord) -> None:
        self.actions[action.action_id] = action

    def get_action(self, action_id: str) -> Optional[HardeningActionRecord]:
        return self.actions.get(action_id)

    def save_target(self, target: UpdateTargetRecord) -> None:
        self.targets[target.target_id] = target

    def get_target(self, target_id: str) -> Optional[UpdateTargetRecord]:
        return self.targets.get(target_id)

    def save_adoption(self, adoption: AdoptionRecord) -> None:
        self.adoptions[adoption.adoption_id] = adoption

    def get_adoption(self, adoption_id: str) -> Optional[AdoptionRecord]:
        return self.adoptions.get(adoption_id)

    def save_validation(self, validation: ValidationRecord) -> None:
        self.validations[validation.validation_id] = validation

    def get_validation(self, validation_id: str) -> Optional[ValidationRecord]:
        return self.validations.get(validation_id)

    def save_recurrence(self, recurrence: RecurrenceRecord) -> None:
        self.recurrences[recurrence.recurrence_id] = recurrence

    def get_recurrence(self, recurrence_id: str) -> Optional[RecurrenceRecord]:
        return self.recurrences.get(recurrence_id)

    def save_precedent(self, precedent: PrecedentLearningRecord) -> None:
        self.precedents[precedent.precedent_id] = precedent

    def get_precedent(self, precedent_id: str) -> Optional[PrecedentLearningRecord]:
        return self.precedents.get(precedent_id)

    def save_comparison(self, comp: LearningComparisonRecord) -> None:
        self.comparisons[comp.comparison_id] = comp

    def get_comparison(self, comp_id: str) -> Optional[LearningComparisonRecord]:
        return self.comparisons.get(comp_id)

    def save_forecast(self, forecast: LearningForecastReport) -> None:
        self.forecasts[forecast.forecast_id] = forecast

    def get_forecast(self, forecast_id: str) -> Optional[LearningForecastReport]:
        return self.forecasts.get(forecast_id)

    def save_debt(self, debt: LearningDebtRecord) -> None:
        self.debts[debt.debt_id] = debt

    def get_debt(self, debt_id: str) -> Optional[LearningDebtRecord]:
        return self.debts.get(debt_id)

    def save_equivalence_report(self, report: LearningEquivalenceReport) -> None:
        self.equivalence_reports[report.report_id] = report

    def get_equivalence_report(self, report_id: str) -> Optional[LearningEquivalenceReport]:
        return self.equivalence_reports.get(report_id)

    def save_divergence_report(self, report: LearningDivergenceReport) -> None:
        self.divergence_reports[report.report_id] = report

    def get_divergence_report(self, report_id: str) -> Optional[LearningDivergenceReport]:
        return self.divergence_reports.get(report_id)

    def save_trust_verdict(self, learning_id: str, verdict: LearningTrustVerdict) -> None:
        self.trust_verdicts[learning_id] = verdict

    def get_trust_verdict(self, learning_id: str) -> Optional[LearningTrustVerdict]:
        return self.trust_verdicts.get(learning_id)

    def save_manifest(self, manifest: LearningArtifactManifest) -> None:
        self.manifests[manifest.manifest_id] = manifest

    def get_manifest(self, manifest_id: str) -> Optional[LearningArtifactManifest]:
        return self.manifests.get(manifest_id)

storage = LearningStorage()
