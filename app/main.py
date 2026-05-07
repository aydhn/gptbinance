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


    build_config_plane_parser(subparsers)
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
    if args.command == "config-plane":
        run_config_plane_command(args)
        return

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

# --- CONFIGURATION PLANE INTEGRATION ---
def build_config_plane_parser(subparsers):
    cp_parser = subparsers.add_parser("config-plane", help="Configuration Plane Management")
    cp_parser.add_argument("--show-config-schemas", action="store_true")
    cp_parser.add_argument("--show-config-parameters", action="store_true")
    cp_parser.add_argument("--show-config-layers", action="store_true")
    cp_parser.add_argument("--show-effective-config", action="store_true")
    cp_parser.add_argument("--profile", type=str, default="default")
    cp_parser.add_argument("--show-config-lineage", action="store_true")
    cp_parser.add_argument("--param", type=str)
    cp_parser.add_argument("--show-config-diff", action="store_true")
    cp_parser.add_argument("--left", type=str)
    cp_parser.add_argument("--right", type=str)
    cp_parser.add_argument("--show-config-drift", action="store_true")
    cp_parser.add_argument("--show-config-equivalence", action="store_true")
    cp_parser.add_argument("--show-runtime-config-snapshot", action="store_true")
    cp_parser.add_argument("--show-config-mutability", action="store_true")
    cp_parser.add_argument("--show-config-review-packs", action="store_true")
    cp_parser.add_argument("--show-secret-adjacent-config-metadata", action="store_true")
    return cp_parser

def run_config_plane_command(args):
    import sys
    from app.config_plane.schemas import registry as schema_registry
    from app.config_plane.layers import layer_registry
    from app.config_plane.sources import source_repository, ConfigSourceFactory
    from app.config_plane.resolution import resolution_engine
    from app.config_plane.models import ConfigScope
    from app.config_plane.enums import ScopeClass
    from app.config_plane.storage import save_manifest
    from app.config_plane.reporting import summarize_effective_config
    from app.config_plane.drift import detect_drift
    from app.config_plane.equivalence import evaluate_equivalence

    if args.show_config_schemas:
        schemas = schema_registry.list_schemas()
        for domain, schema in schemas.items():
            print(f"Domain: {domain.value}")
            print(f"  Version: {schema.version.version_id}")
            print(f"  Parameters: {list(schema.parameters.keys())}")
        sys.exit(0)

    if args.show_config_parameters:
        for domain, schema in schema_registry.list_schemas().items():
            for name, param in schema.parameters.items():
                print(f"[{domain.value}.{name}] Type: {param.type_name}, Mutability: {param.mutability_class.value}, Default: {param.default_value}")
        sys.exit(0)

    if args.show_config_layers:
        for layer in layer_registry.list_layers():
            print(f"[{layer.priority}] {layer.layer_class.value} - Scopes: {[s.value for s in layer.allowed_scopes]}")
        sys.exit(0)

    if args.show_effective_config:
        source = ConfigSourceFactory.create_source(
            layer_id="profile_defaults_1",
            scope=ConfigScope(scope_class=ScopeClass.PROFILE, target_id=args.profile),
            payload={"risk.max_daily_loss_pct": 1.5}
        )
        source_repository.add_source(source)
        target_scope = ConfigScope(scope_class=ScopeClass.PROFILE, target_id=args.profile)
        manifest = resolution_engine.resolve(args.profile, target_scope, source_repository.list_sources())
        save_manifest(manifest)
        print("Effective Config Manifest resolved.")
        print(summarize_effective_config(manifest, redacted=False))
        sys.exit(0)

    if args.show_config_lineage:
        if not args.param:
            print("Must provide --param")
            sys.exit(1)
        manifest = resolution_engine.resolve("default", ConfigScope(scope_class=ScopeClass.GLOBAL), source_repository.list_sources())
        entry = manifest.entries.get(args.param)
        if entry:
            print(f"Lineage for {args.param}:")
            print(f"  Effective Value: {entry.value}")
            print(f"  Source Chain: {entry.lineage.source_chain}")
            print(f"  Is Hidden Default: {entry.lineage.is_hidden_default}")
        else:
            print(f"Parameter {args.param} not found in effective config.")
        sys.exit(0)

    if args.show_config_drift:
        manifest = resolution_engine.resolve("default", ConfigScope(scope_class=ScopeClass.GLOBAL), [])
        mock_runtime = {"risk.max_daily_loss_pct": 5.0} # drift!
        findings = detect_drift(manifest, mock_runtime)
        if findings:
            for f in findings:
                print(f"DRIFT DETECTED: {f.description}")
        else:
            print("No drift detected.")
        sys.exit(0)

    if args.show_config_equivalence:
        baseline = resolution_engine.resolve("default", ConfigScope(scope_class=ScopeClass.GLOBAL), [])
        source = ConfigSourceFactory.create_source(
            layer_id="profile_defaults_1",
            scope=ConfigScope(scope_class=ScopeClass.GLOBAL),
            payload={"risk.max_daily_loss_pct": 3.0}
        )
        target = resolution_engine.resolve("default", ConfigScope(scope_class=ScopeClass.GLOBAL), [source])
        report = evaluate_equivalence(baseline, target)
        print(f"Equivalence Verdict: {report.verdict.value}")
        print(f"Divergences: {report.divergences}")
        sys.exit(0)

    if args.show_runtime_config_snapshot:
        print("Runtime Config Snapshot:")
        print(" Active Profile: default")
        print(" Snapshot ID: rt_snap_mock")
        sys.exit(0)

    if args.show_config_mutability:
        print("Mutability Governance Summary:")
        for domain, schema in schema_registry.list_schemas().items():
            for name, param in schema.parameters.items():
                print(f" - {domain.value}.{name} -> {param.mutability_class.value}")
        sys.exit(0)

    if args.show_config_review_packs:
        print("Config Review Packs:")
        print(" No active reviews pending.")
        sys.exit(0)

    if args.show_secret_adjacent_config_metadata:
        print("Secret-Adjacent Config Metadata:")
        print(" None currently defined in bootstrap.")
        sys.exit(0)
