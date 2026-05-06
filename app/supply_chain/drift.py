from typing import List
from app.supply_chain.models import DependencySnapshot, DependencyDriftFinding
from app.supply_chain.enums import DriftSeverity


class DriftDetector:
    def detect_dependency_drift(
        self, expected: DependencySnapshot, actual: DependencySnapshot
    ) -> List[DependencyDriftFinding]:
        findings = []
        exp_dict = {d.name: d.version for d in expected.dependencies}
        act_dict = {d.name: d.version for d in actual.dependencies}

        for name, exp_ver in exp_dict.items():
            if name not in act_dict:
                findings.append(
                    DependencyDriftFinding(
                        dependency_name=name,
                        expected_version=exp_ver,
                        actual_version="missing",
                        severity=DriftSeverity.HIGH,
                    )
                )
            elif act_dict[name] != exp_ver:
                findings.append(
                    DependencyDriftFinding(
                        dependency_name=name,
                        expected_version=exp_ver,
                        actual_version=act_dict[name],
                        severity=DriftSeverity.MEDIUM,
                    )
                )

        for name, act_ver in act_dict.items():
            if name not in exp_dict:
                findings.append(
                    DependencyDriftFinding(
                        dependency_name=name,
                        expected_version="missing",
                        actual_version=act_ver,
                        severity=DriftSeverity.MEDIUM,
                    )
                )

        return findings
