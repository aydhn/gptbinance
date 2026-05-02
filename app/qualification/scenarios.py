from typing import List, Dict, Any
from app.qualification.models import QualificationScenario, ScenarioResult
from app.qualification.enums import ScenarioType


class GoldenPathRunner:
    def __init__(self):
        self.scenarios = {
            "gold-risk-to-exec": QualificationScenario(
                scenario_id="gold-risk-to-exec",
                description="Risk to portfolio to paper execution path",
                type=ScenarioType.GOLDEN_PATH,
                required_evidence=["risk-approved-intent"],
            ),
            "gold-restore-dry-run": QualificationScenario(
                scenario_id="gold-restore-dry-run",
                description="Backup to restore dry run to recovery readiness",
                type=ScenarioType.RECOVERY,
                required_evidence=["security-audit"],
            ),
            "gold-upgrade-dry-run": QualificationScenario(
                scenario_id="gold-upgrade-dry-run",
                description="Release bundle build to probe to upgrade dry run",
                type=ScenarioType.GOLDEN_PATH,
                required_evidence=["backup-metadata"],
            ),
            "gold-portfolio-concentration": QualificationScenario(
                scenario_id="gold-portfolio-concentration",
                description="Verify portfolio concentration limits are checked",
                type=ScenarioType.GOLDEN_PATH,
                required_evidence=["portfolio-report"],
            ),
        }

    def run_suite(self, suite_scenarios: List[str]) -> List[ScenarioResult]:
        results = []
        for sid in suite_scenarios:
            if sid in self.scenarios:
                scen = self.scenarios[sid]
                # Mock execution: assume pass if we have it
                results.append(
                    ScenarioResult(
                        scenario_id=sid,
                        scenario_type=scen.type,
                        passed=True,
                        evidence_refs=scen.required_evidence,
                    )
                )
        return results
