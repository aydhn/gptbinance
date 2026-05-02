from datetime import datetime, timezone
import uuid

from app.qualification.base import BaseQualificationRunner
from app.qualification.models import QualificationRun, QualificationConfig
from app.qualification.enums import QualificationProfile
from app.qualification.profiles import get_profile_definition
from app.qualification.scenarios import GoldenPathRunner
from app.qualification.negative import ForbiddenActionRunner
from app.qualification.contracts import ContractVerifier
from app.qualification.evidence_pack import EvidencePackAssembler
from app.qualification.scoring import calculate_score
from app.qualification.verdicts import evaluate_verdict


class QualificationRunner(BaseQualificationRunner):
    def run(
        self, profile: QualificationProfile, config: QualificationConfig
    ) -> QualificationRun:
        run_id = str(uuid.uuid4())
        q_run = QualificationRun(run_id=run_id, profile=profile, config=config)

        prof_def = get_profile_definition(profile)

        # 1. Golden Path
        golden_runner = GoldenPathRunner()
        # Flat mock of scenarios mapped from suites
        scenario_ids = [
            s
            for suite in prof_def.required_suites
            for s in [
                "gold-risk-to-exec",
                "gold-restore-dry-run",
                "gold-upgrade-dry-run",
                "gold-portfolio-concentration",
            ]
        ]
        q_run.scenarios = golden_runner.run_suite(list(set(scenario_ids)))

        # 2. Negative/Forbidden Tests
        forbidden_runner = ForbiddenActionRunner()
        q_run.forbidden_actions = forbidden_runner.run_forbidden_checks(
            prof_def.mandatory_negative_tests
        )

        # 3. Contracts
        contract_verifier = ContractVerifier()
        q_run.contracts = contract_verifier.verify_contracts()

        # 4. Evidence
        pack_assembler = EvidencePackAssembler()
        evidence_pack = pack_assembler.assemble(
            run_id, prof_def.required_evidence_sections
        )
        q_run.evidence_pack_id = evidence_pack.pack_id

        # Mocking Findings (e.g., finding unblocked forbidden action)
        q_run.findings = []

        # 5. Score
        q_run.score = calculate_score(
            q_run.scenarios,
            q_run.contracts,
            q_run.forbidden_actions,
            q_run.findings,
            evidence_pack,
        )

        # 6. Verdict
        q_run.verdict = evaluate_verdict(profile, q_run.score)

        q_run.completed_at = datetime.now(timezone.utc)
        return q_run
