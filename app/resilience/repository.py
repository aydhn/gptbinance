import uuid
import asyncio
from datetime import datetime, timezone
from app.resilience.base import BaseExperimentRunner
from app.resilience.models import (
    ExperimentDefinition,
    ExperimentScope,
    ExperimentRun,
    ExperimentSummary,
    ExperimentStatus,
    DegradationSummary,
)
from app.resilience.gates import SafetyGate
from app.resilience.faults import FaultInjector
from app.resilience.stress import StressGenerator
from app.resilience.assertions import AssertionEvaluator
from app.resilience.recovery_checks import RecoveryEvaluator
from app.resilience.scoring import ResilienceScorer
from app.resilience.telemetry import ExperimentTelemetry
from app.resilience.storage import StorageLayer


class ExperimentRunner(BaseExperimentRunner):
    def __init__(self):
        self.gate = SafetyGate()
        self.fault_injector = FaultInjector()
        self.stress_generator = StressGenerator()
        self.assertion_evaluator = AssertionEvaluator()
        self.recovery_evaluator = RecoveryEvaluator()
        self.scorer = ResilienceScorer()
        self.telemetry = ExperimentTelemetry()
        self.storage = StorageLayer()

    async def run_experiment(
        self, definition: ExperimentDefinition, scope: ExperimentScope
    ) -> ExperimentRun:
        run_id = f"exp_{uuid.uuid4().hex[:8]}"

        run = ExperimentRun(
            id=run_id,
            definition=definition,
            scope=scope,
            status=ExperimentStatus.PENDING,
        )

        gate_report = self.gate.evaluate(definition, scope)

        if gate_report.verdict != "allow":
            run.status = ExperimentStatus.GATED
            run.summary = ExperimentSummary(
                run_id=run_id,
                definition_id=definition.id,
                scope=scope.safe_scope,
                status=run.status,
                start_time=datetime.now(timezone.utc),
                gate_report=gate_report,
            )
            self.storage.save_summary(run.summary)
            return run

        run.status = ExperimentStatus.RUNNING
        self.telemetry.record_event(
            run_id, "experiment_started", {"definition_id": definition.id}
        )

        summary = ExperimentSummary(
            run_id=run_id,
            definition_id=definition.id,
            scope=scope.safe_scope,
            status=run.status,
            start_time=datetime.now(timezone.utc),
            gate_report=gate_report,
        )

        # Inject Faults
        for fault_spec in definition.fault_specs:
            await self.fault_injector.inject(fault_spec, run_id)

        # Apply Stress
        for stress_spec in definition.stress_specs:
            await self.stress_generator.apply_stress(stress_spec, run_id)

        # Wait for duration (simulated)
        max_duration = max(
            [f.duration_ms for f in definition.fault_specs]
            + [s.duration_ms for s in definition.stress_specs]
            + [1000]
        )
        await asyncio.sleep(max_duration / 1000.0)

        run.status = ExperimentStatus.ASSERTING
        # Evaluate Assertions
        for assertion_spec in definition.assertions:
            result = await self.assertion_evaluator.evaluate(assertion_spec, run_id)
            summary.assertion_results.append(result)

        run.status = ExperimentStatus.RECOVERING
        # Cleanup
        for fault_spec in definition.fault_specs:
            await self.fault_injector.cleanup(fault_spec, run_id)
        for stress_spec in definition.stress_specs:
            await self.stress_generator.remove_stress(stress_spec, run_id)

        # Wait for recovery (simulated)
        await asyncio.sleep(1.0)

        # Evaluate Recovery
        for rec_spec in definition.recovery_assertions:
            result = await self.recovery_evaluator.evaluate(rec_spec, run_id)
            summary.recovery_results.append(result)

        run.status = ExperimentStatus.COMPLETED
        summary.status = run.status
        summary.end_time = datetime.now(timezone.utc)

        summary.degradation_summary = DegradationSummary(
            mode_entered=definition.expected_degradation_mode
        )
        summary.resilience_score = self.scorer.calculate_score(summary)

        run.summary = summary
        self.storage.save_summary(summary)
        self.telemetry.record_event(
            run_id,
            "experiment_completed",
            {"score": summary.resilience_score.overall_score},
        )

        return run
