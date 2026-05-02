import json
from app.resilience.models import ExperimentSummary


class Reporter:
    @staticmethod
    def generate_summary(summary: ExperimentSummary) -> str:
        data = {
            "run_id": summary.run_id,
            "scenario_id": summary.definition_id,
            "status": summary.status.value,
            "scope": summary.scope.value,
            "start_time": summary.start_time.isoformat()
            if summary.start_time
            else None,
            "end_time": summary.end_time.isoformat() if summary.end_time else None,
            "assertions": [
                {"id": a.spec_id, "verdict": a.verdict.value}
                for a in summary.assertion_results
            ],
            "recovery": [
                {"id": a.spec_id, "verdict": a.verdict.value}
                for a in summary.recovery_results
            ],
            "score": summary.resilience_score.model_dump()
            if summary.resilience_score
            else None,
        }
        return json.dumps(data, indent=2)

    @staticmethod
    def print_cli_report(summary: ExperimentSummary):
        print("\n" + "=" * 50)
        print("RESILIENCE EXPERIMENT SUMMARY")
        print("=" * 50)
        print(f"Run ID      : {summary.run_id}")
        print(f"Scenario    : {summary.definition_id}")
        print(f"Status      : {summary.status.value.upper()}")
        print(f"Safe Scope  : {summary.scope.value.upper()}")

        if summary.gate_report.verdict != "allow":
            print(f"\nGATE BLOCKED: {summary.gate_report.reason}")
            return

        if summary.resilience_score:
            print("\nSCORE BREAKDOWN:")
            print(f"  Overall     : {summary.resilience_score.overall_score}/100")
            print(f"  Detection   : {summary.resilience_score.detection_score}/100")
            print(f"  Containment : {summary.resilience_score.containment_score}/100")
            print(f"  Recovery    : {summary.resilience_score.recovery_score}/100")

        print("\nASSERTIONS:")
        for a in summary.assertion_results:
            print(f"  [{a.verdict.value.upper()}] {a.spec_id}")

        print("\nRECOVERY CHECKS:")
        for r in summary.recovery_results:
            print(f"  [{r.verdict.value.upper()}] {r.spec_id}")

        print("=" * 50 + "\n")
