import argparse
import sys
from datetime import datetime, timezone
from app.supply_chain.sources import GitSourceSnapshotter
from app.supply_chain.dependencies import PoetryDependencyInventory
from app.supply_chain.locks import LockIntegrityChecker
from app.supply_chain.builds import BuildProvenanceAssembler
from app.supply_chain.attestations import (
    LocalAttestationGenerator,
    LocalAttestationVerifier,
)
from app.supply_chain.provenance import ProvenanceBuilder
from app.supply_chain.reproducibility import ReproducibilityChecker
from app.supply_chain.drift import DriftDetector
from app.supply_chain.runtime import RuntimeEquivalenceEvaluator
from app.supply_chain.trust import TrustVerdictEngine
from app.supply_chain.reporting import SupplyChainReporter
from app.supply_chain.storage import SupplyChainStorage
from app.supply_chain.repository import SupplyChainRepository
from app.supply_chain.models import SupplyChainEvidenceBundle
from app.supply_chain.enums import ArtifactClass


def main():
    parser = argparse.ArgumentParser(description="Supply Chain Integrity CLI")
    parser.add_argument(
        "--show-source-snapshots", action="store_true", help="Show source snapshots"
    )
    parser.add_argument(
        "--show-dependency-snapshot",
        action="store_true",
        help="Show dependency snapshot",
    )
    parser.add_argument(
        "--show-lock-integrity", action="store_true", help="Show lock integrity"
    )
    parser.add_argument(
        "--show-build-manifest", action="store_true", help="Show build manifest"
    )
    parser.add_argument("--build-id", type=str, help="Build ID")
    parser.add_argument(
        "--show-attestations", action="store_true", help="Show attestations"
    )
    parser.add_argument(
        "--show-provenance-chain", action="store_true", help="Show provenance chain"
    )
    parser.add_argument("--artefact-id", type=str, help="Artefact ID")
    parser.add_argument(
        "--run-reproducibility-check",
        action="store_true",
        help="Run reproducibility check",
    )
    parser.add_argument(
        "--show-runtime-equivalence",
        action="store_true",
        help="Show runtime equivalence",
    )
    parser.add_argument(
        "--show-supply-chain-trust", action="store_true", help="Show supply chain trust"
    )
    parser.add_argument(
        "--show-dependency-drift", action="store_true", help="Show dependency drift"
    )
    parser.add_argument(
        "--build-supply-chain-pack", action="store_true", help="Build supply chain pack"
    )
    parser.add_argument("--pack-class", type=str, help="Pack class")
    parser.add_argument(
        "--show-supply-chain-evidence",
        action="store_true",
        help="Show supply chain evidence",
    )

    args = parser.parse_args()

    # Simple mock storage & repository for demo purposes
    storage = SupplyChainStorage()
    repo = SupplyChainRepository(storage)

    if args.show_source_snapshots:
        src = GitSourceSnapshotter().create_snapshot()
        print(f"Source Snapshot ID: {src.id}")
        print(f"Is Clean: {src.is_clean}")
        print(f"Ref: {src.ref}")
        print(f"Tracked Files Count: {len(src.tracked_files)}")

    elif args.show_dependency_snapshot:
        dep = PoetryDependencyInventory().create_snapshot()
        print(f"Dependency Snapshot ID: {dep.id}")
        print(f"Dependencies Count: {len(dep.dependencies)}")
        print(f"Lock Hash: {dep.lock_hash}")

    elif args.show_lock_integrity:
        checker = LockIntegrityChecker()
        res = checker.check("hash1", "hash1", "dep1")
        print(f"Lock Integrity Intact: {res.is_intact}")
        print(f"Verdict: {res.verdict.value}")

    elif args.show_build_manifest:
        if not args.build_id:
            print("Please provide --build-id")
            sys.exit(1)
        assembler = BuildProvenanceAssembler()
        manifest = assembler.assemble("src1", "dep1", [], ArtifactClass.RELEASE_BUNDLE)
        print(f"Build Manifest ID: {manifest.id}")
        print(f"Hash: {manifest.hash}")

    elif args.show_attestations:
        gen = LocalAttestationGenerator()
        att = gen.generate("build1", "payload1", "human")
        print(f"Attestation ID: {att.id}")
        print(f"Signature: {att.signature}")

    elif args.show_provenance_chain:
        builder = ProvenanceBuilder()
        chain = builder.build_chain(
            "build1", "src1", "dep1", datetime.now(timezone.utc)
        )
        print(f"Provenance Chain ID: {chain.id}")
        print(f"Completeness Score: {chain.completeness_score}")

    elif args.show_supply_chain_trust:
        checker = LockIntegrityChecker()
        lock_res = checker.check("hash1", "hash1", "dep1")
        engine = TrustVerdictEngine()
        verdict = engine.evaluate("art1", lock_res, None, None, True)
        print(f"Trust Verdict: {verdict.verdict.value}")
        print(f"Factors: {verdict.factors}")

    else:
        print("Please provide a valid supply chain command. Use -h for help.")


if __name__ == "__main__":
    main()
