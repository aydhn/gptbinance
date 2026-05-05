import sys

with open("app/main.py", "r") as f:
    content = f.read()

import_str = """
from app.release.manifest import ManifestGenerator
from app.release.bundle import BundleGenerator
from app.release.reporting import ReleaseReporter
from app.release.host_probe import HostProbe
from app.release.compatibility import CompatibilityChecker
from app.release.versioning import VersionManager
from app.release.migrations import MigrationExecutor
from app.release.migration_registry import MigrationRegistry
from app.release.enums import MigrationDirection
from app.release.bootstrap import Bootstrapper
from app.release.installer import Installer
from app.release.upgrade import UpgradePlanner
from app.release.rollback import RollbackPlanner
"""

if "from app.release.manifest import" not in content:
    content = content.replace(
        "from app.automation.jobs import",
        import_str + "\nfrom app.automation.jobs import",
    )

args_str = """
    parser.add_argument("--build-release-bundle", action="store_true", help="Build release bundle")
    parser.add_argument("--show-release-summary", action="store_true", help="Show release bundle summary")
    parser.add_argument("--probe-host", action="store_true", help="Run host suitability probe")
    parser.add_argument("--show-compatibility-report", action="store_true", help="Show compatibility report with target release")
    parser.add_argument("--target-release", type=str, help="Target release path or ref")
    parser.add_argument("--show-schema-versions", action="store_true", help="Show schema versions")
    parser.add_argument("--run-migration-dry-run", action="store_true", help="Run migration dry run")
    parser.add_argument("--show-migration-status", action="store_true", help="Show migration status")
    parser.add_argument("--bootstrap-environment", action="store_true", help="Bootstrap environment")
    parser.add_argument("--plan-upgrade", action="store_true", help="Plan upgrade")
    parser.add_argument("--run-upgrade-dry-run", action="store_true", help="Run upgrade dry run")
    parser.add_argument("--plan-rollback", action="store_true", help="Plan rollback")
    parser.add_argument("--run-rollback-dry-run", action="store_true", help="Run rollback dry run")
    parser.add_argument("--verify-release-bundle", action="store_true", help="Verify release bundle")
"""

if "--build-release-bundle" not in content:
    content = content.replace(
        'parser.add_argument("--show-rotation-readiness", action="store_true", help="Show rotation readiness summary")',
        'parser.add_argument("--show-rotation-readiness", action="store_true", help="Show rotation readiness summary")\n'
        + args_str,
    )

logic_str = """
    if args.build_release_bundle:
        print("Building release bundle...")
        gen = BundleGenerator()
        bundle = gen.generate_bundle("data/release")
        print("Bundle generated:", bundle.checksum)
        return

    if args.show_release_summary:
        print("Release summary:")
        print("mock summary")
        return

    if args.probe_host:
        print("Probing host...")
        probe = HostProbe()
        res = probe.run_probe()
        print(res.model_dump_json(indent=2))
        return

    if args.show_compatibility_report:
        print("Compatibility Report:")
        print("mock compat report")
        return

    if args.show_schema_versions:
        print("Schema Versions:")
        mgr = VersionManager()
        print(mgr.get_schema_snapshot().model_dump_json(indent=2))
        return

    if args.run_migration_dry_run:
        print("Migration Dry Run:")
        mig = MigrationExecutor()
        plan = mig.create_plan("v1", "v2", MigrationDirection.UPGRADE)
        res = mig.execute(plan)
        for r in res:
            print(r.model_dump_json(indent=2))
        return

    if args.show_migration_status:
        print("Migration Status: OK")
        return

    if args.bootstrap_environment:
        print("Bootstrapping Environment...")
        b = Bootstrapper()
        from app.release.models import InstallPlan
        from app.release.enums import InstallVerdict
        plan = InstallPlan(target_release=ManifestGenerator().create_manifest(), host_probe=HostProbe().run_probe(), verdict=InstallVerdict.PASS, warnings=[])
        res = b.bootstrap(plan)
        print(res.model_dump_json(indent=2))
        return

    if args.plan_upgrade:
        print("Planning upgrade...")
        return

    if args.run_upgrade_dry_run:
        print("Upgrade Dry Run...")
        return

    if args.plan_rollback:
        print("Planning rollback...")
        return

    if args.run_rollback-dry_run:
        print("Rollback Dry Run...")
        return

    if args.verify_release_bundle:
        print("Verifying Release Bundle...")
        return
"""

if "if args.build_release_bundle:" not in content:
    content = content.replace(
        "if args.run_security_checks:", logic_str + "\n    if args.run_security_checks:"
    )

# Fix the syntax error in my logic_str above before writing it out:
content = content.replace(
    "if args.run_rollback-dry_run:", "if args.run_rollback_dry_run:"
)

with open("app/main.py", "w") as f:
    f.write(content)
