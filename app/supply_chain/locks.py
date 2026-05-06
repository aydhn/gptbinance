from app.supply_chain.models import LockIntegrityRecord
from app.supply_chain.enums import IntegrityVerdict


class LockIntegrityChecker:
    def check(
        self, current_lock_hash: str, expected_lock_hash: str, dep_snap_id: str
    ) -> LockIntegrityRecord:
        is_intact = current_lock_hash == expected_lock_hash
        verdict = IntegrityVerdict.VERIFIED if is_intact else IntegrityVerdict.MISMATCH
        findings = []
        if not is_intact:
            findings.append(
                "Lockfile hash mismatch: Generated lock differs from committed lock."
            )

        return LockIntegrityRecord(
            dependency_snapshot_id=dep_snap_id,
            is_intact=is_intact,
            drift_findings=findings,
            verdict=verdict,
        )
