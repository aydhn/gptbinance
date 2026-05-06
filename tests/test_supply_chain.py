import pytest
from datetime import datetime, timezone
from app.supply_chain.models import (
    SourceSnapshot,
    DependencySnapshot,
    DependencyItem,
    LockIntegrityRecord,
    BuildOutputManifest,
    BuildInputManifest,
    BuildEnvironmentSnapshot,
    BuildArtifactRecord,
    AttestationRecord,
    ProvenanceChain,
    ReproducibilityResult,
    RuntimeEquivalenceReport,
    TrustedArtifactVerdict,
)
from app.supply_chain.enums import (
    SourceClass,
    DependencyClass,
    ArtifactClass,
    IntegrityVerdict,
    ReproducibilityClass,
    TrustVerdict,
    RuntimeEquivalence,
    AttestationClass,
)
from app.supply_chain.hashes import generate_hash
from app.supply_chain.sources import GitSourceSnapshotter
from app.supply_chain.dependencies import PoetryDependencyInventory
from app.supply_chain.locks import LockIntegrityChecker
from app.supply_chain.attestations import (
    LocalAttestationGenerator,
    LocalAttestationVerifier,
)
from app.supply_chain.reproducibility import ReproducibilityChecker
from app.supply_chain.runtime import RuntimeEquivalenceEvaluator
from app.supply_chain.trust import TrustVerdictEngine


def test_source_snapshot():
    snapshotter = GitSourceSnapshotter()
    snap = snapshotter.create_snapshot()
    assert snap.id.startswith("src_")


def test_dependency_snapshot():
    inv = PoetryDependencyInventory()
    snap = inv.create_snapshot()
    assert snap.id.startswith("dep_")


def test_lock_integrity():
    checker = LockIntegrityChecker()
    res = checker.check("hash1", "hash1", "dep1")
    assert res.is_intact is True
    assert res.verdict == IntegrityVerdict.VERIFIED

    res2 = checker.check("hash1", "hash2", "dep1")
    assert res2.is_intact is False
    assert res2.verdict == IntegrityVerdict.MISMATCH


def test_attestation():
    gen = LocalAttestationGenerator()
    att = gen.generate("build1", "payloadhash", "system")
    assert att.signature is not None

    ver = LocalAttestationVerifier()
    assert ver.verify(att) is True


def test_reproducibility():
    env = BuildEnvironmentSnapshot(
        python_version="3.10",
        os_platform="linux",
        tool_versions={},
        env_vars_hash="123",
        is_deterministic=True,
    )
    inputs = BuildInputManifest(
        source_snapshot_id="src1",
        dependency_snapshot_id="dep1",
        environment_snapshot=env,
    )

    man1 = BuildOutputManifest(
        id="man1",
        artifact_class=ArtifactClass.RELEASE_BUNDLE,
        timestamp=datetime.now(timezone.utc),
        inputs=inputs,
        artifacts=[],
        hash="hash_same",
    )
    man2 = BuildOutputManifest(
        id="man2",
        artifact_class=ArtifactClass.RELEASE_BUNDLE,
        timestamp=datetime.now(timezone.utc),
        inputs=inputs,
        artifacts=[],
        hash="hash_same",
    )

    checker = ReproducibilityChecker()
    res = checker.check(man1, man2)
    assert res.result.reproducibility_class == ReproducibilityClass.DETERMINISTIC


def test_runtime_equivalence():
    env = BuildEnvironmentSnapshot(
        python_version="3.10",
        os_platform="linux",
        tool_versions={},
        env_vars_hash="123",
        is_deterministic=True,
    )
    inputs = BuildInputManifest(
        source_snapshot_id="src1",
        dependency_snapshot_id="dep1",
        environment_snapshot=env,
    )
    man = BuildOutputManifest(
        id="man1",
        artifact_class=ArtifactClass.RELEASE_BUNDLE,
        timestamp=datetime.now(timezone.utc),
        inputs=inputs,
        artifacts=[],
        hash="hash_active",
    )

    evaluator = RuntimeEquivalenceEvaluator()
    res = evaluator.evaluate("hash_active", man)
    assert res.equivalence == RuntimeEquivalence.EQUIVALENT


def test_trust_verdict():
    lock = LockIntegrityRecord(
        dependency_snapshot_id="dep1",
        is_intact=True,
        drift_findings=[],
        verdict=IntegrityVerdict.VERIFIED,
    )
    repro = ReproducibilityResult(
        build_id="man1",
        reproducibility_class=ReproducibilityClass.DETERMINISTIC,
        diff_surfaces=[],
        timestamp=datetime.now(timezone.utc),
    )
    run_eq = RuntimeEquivalenceReport(
        id="rteq",
        runtime_surface_hash="active",
        expected_build_id="man1",
        equivalence=RuntimeEquivalence.EQUIVALENT,
        mismatches=[],
        timestamp=datetime.now(timezone.utc),
    )

    engine = TrustVerdictEngine()
    verdict = engine.evaluate("art1", lock, repro, run_eq, has_attestation=True)
    assert verdict.verdict == TrustVerdict.TRUSTED
