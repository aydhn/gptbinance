import uuid
from datetime import datetime, timezone
from app.order_intent import (
    HighLevelIntent,
    IntentContext,
    IntentCompiler,
    PolicyEngine,
    PlanValidator,
    DiffCalculator,
    Explainer,
    IntentRepository,
    IntentStorage,
    CompileVerdict,
    CompileAuditRecord,
    IntentCompilationResult,
)
from app.order_intent.exceptions import CompilePolicyViolation


class IntentFacade:
    def __init__(self):
        self.compiler = IntentCompiler()
        self.policy = PolicyEngine()
        self.validator = PlanValidator()
        self.differ = DiffCalculator()
        self.explainer = Explainer()
        self.repo = IntentRepository(IntentStorage())

    def process_intent(
        self, intent: HighLevelIntent, context: IntentContext, dry_run: bool = False
    ) -> IntentCompilationResult:
        run_id = f"run_{uuid.uuid4().hex[:8]}"
        reasons = []
        plan = None
        verdict = CompileVerdict.SUCCESS
        diff = None
        explanation = None
        validation = None

        try:
            # 1. Policy check
            self.policy.check_intent(intent, context)

            # 2. Compile
            plan = self.compiler.compile_intent(intent, context)

            # 3. Validate
            validation = self.validator.validate(plan)
            if not validation.is_valid:
                verdict = CompileVerdict.FAILED
                reasons.extend(validation.errors)
            else:
                # 4. Diff & Explain
                diff = self.differ.calculate(intent, plan)
                explanation = self.explainer.explain(intent, plan)

        except CompilePolicyViolation as e:
            verdict = CompileVerdict.BLOCKED
            reasons.append(str(e))
        except Exception as e:
            verdict = CompileVerdict.FAILED
            reasons.append(str(e))

        audit = CompileAuditRecord(
            run_id=run_id,
            intent_id=intent.intent_id,
            verdict=verdict,
            reasons=reasons,
            timestamp=datetime.now(timezone.utc),
        )

        result = IntentCompilationResult(
            intent=intent,
            plan=plan,
            verdict=verdict,
            audit_record=audit,
            explanation=explanation,
            diff=diff,
            validation_result=validation,
        )

        if not dry_run:
            self.repo.store_compilation(result)

        return result
