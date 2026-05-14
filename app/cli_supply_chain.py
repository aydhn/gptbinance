import argparse
import sys
from app.supply_chain_plane.registry import CanonicalComponentRegistry
from app.supply_chain_plane.models import ComponentDefinition
from app.supply_chain_plane.enums import ComponentClass
from app.supply_chain_plane.reporting import SupplyChainReporter

def setup_mock_data(registry: CanonicalComponentRegistry):
    registry.register_component(ComponentDefinition(
        component_id="core-service",
        name="Core Trading Service",
        component_class=ComponentClass.SOURCE_COMPONENT,
        owner="team-execution",
        criticality="critical",
        supported_environments=["dev", "paper", "live"],
        lifecycle_state="active"
    ))

def handle_cli(parser):
    parser.add_argument("--show-supply-chain-registry", action="store_true")
    parser.add_argument("--show-component", type=str, help="Component ID")
    parser.add_argument("--show-component-origins", action="store_true")
    parser.add_argument("--show-dependencies", action="store_true")
    parser.add_argument("--show-dependency-graphs", action="store_true")
    parser.add_argument("--show-build-recipes", action="store_true")
    parser.add_argument("--show-build-inputs", action="store_true")
    parser.add_argument("--show-build-provenance", action="store_true")
    parser.add_argument("--show-generated-artifacts", action="store_true")
    parser.add_argument("--show-packages", action="store_true")
    parser.add_argument("--show-container-artifacts", action="store_true")
    parser.add_argument("--show-sboms", action="store_true")
    parser.add_argument("--show-signatures", action="store_true")
    parser.add_argument("--show-artifact-verification", action="store_true")
    parser.add_argument("--show-licenses", action="store_true")
    parser.add_argument("--show-origin-trust", action="store_true")
    parser.add_argument("--show-runtime-lineage", action="store_true")
    parser.add_argument("--show-supply-chain-drift", action="store_true")
    parser.add_argument("--show-supply-chain-exceptions", action="store_true")
    parser.add_argument("--show-supply-chain-debt", action="store_true")
    parser.add_argument("--show-supply-chain-equivalence", action="store_true")
    parser.add_argument("--show-supply-chain-trust", action="store_true")
    parser.add_argument("--show-supply-chain-review-packs", action="store_true")

def execute_cli(args):
    registry = CanonicalComponentRegistry()
    setup_mock_data(registry)
    reporter = SupplyChainReporter()

    if args.show_supply_chain_registry:
        print(reporter.format_component_summary(registry.list_components()))
        sys.exit(0)

    if args.show_component:
        comp = registry.get_component(args.show_component)
        if comp:
            print(f"Component: {comp.name} ({comp.component_id})")
            print(f"Class: {comp.component_class.name}")
            print(f"Owner: {comp.owner}")
            print(f"Criticality: {comp.criticality}")
        else:
            print(f"Component {args.show_component} not found.")
        sys.exit(0)

    flags = [
        "show_component_origins", "show_dependencies", "show_dependency_graphs",
        "show_build_recipes", "show_build_inputs", "show_build_provenance",
        "show_generated_artifacts", "show_packages", "show_container_artifacts",
        "show_sboms", "show_signatures", "show_artifact_verification", "show_licenses",
        "show_origin_trust", "show_runtime_lineage", "show_supply_chain_drift",
        "show_supply_chain_exceptions", "show_supply_chain_debt", "show_supply_chain_equivalence",
        "show_supply_chain_trust", "show_supply_chain_review_packs"
    ]
    for flag in flags:
        if getattr(args, flag, False):
            print(f"Displaying data for: --{flag.replace('_', '-')}")
            print("Status: Available (Mocked Output for implementation)")
            sys.exit(0)
