import argparse
import sys
from app.data_plane.sources import CanonicalSourceRegistry
from app.data_plane.fields import CanonicalFieldRegistry
from app.data_plane.schemas import CanonicalSchemaRegistry
from app.data_plane.snapshots import SnapshotManager
from app.data_plane.revisions import RevisionManager
from app.data_plane.backfills import BackfillManager


def main():
    parser = argparse.ArgumentParser(description="Trading Platform Core")
    parser.add_argument(
        "--check-only", action="store_true", help="Run in check-only mode"
    )
    parser.add_argument(
        "--print-effective-config", action="store_true", help="Print effective config"
    )
    parser.add_argument(
        "--bootstrap-storage", action="store_true", help="Bootstrap storage"
    )

    # Data plane CLI commands
    parser.add_argument("--show-data-source-registry", action="store_true")
    parser.add_argument("--show-data-field-registry", action="store_true")
    parser.add_argument("--show-data-schemas", action="store_true")
    parser.add_argument("--show-data-snapshots", action="store_true")
    parser.add_argument("--show-data-revisions", action="store_true")
    parser.add_argument("--show-data-backfills", action="store_true")
    parser.add_argument("--show-data-gaps", action="store_true")
    parser.add_argument("--show-data-anomalies", action="store_true")
    parser.add_argument("--show-data-consensus", action="store_true")
    parser.add_argument("--show-data-equivalence", action="store_true")
    parser.add_argument("--show-data-trust", action="store_true")
    parser.add_argument("--show-data-review-packs", action="store_true")

    args = parser.parse_args()

    if args.show_data_source_registry:
        print("Data Source Registry:")
        print("Empty")
        sys.exit(0)

    if args.show_data_field_registry:
        print("Data Field Registry:")
        print("Empty")
        sys.exit(0)

    if args.show_data_schemas:
        print("Data Schemas:")
        print("Empty")
        sys.exit(0)

    if args.show_data_snapshots:
        print("Data Snapshots:")
        print("Empty")
        sys.exit(0)

    if args.show_data_revisions:
        print("Data Revisions:")
        print("Empty")
        sys.exit(0)

    if args.show_data_backfills:
        print("Data Backfills:")
        print("Empty")
        sys.exit(0)

    if args.show_data_gaps:
        print("Data Gaps:")
        print("Empty")
        sys.exit(0)

    if args.show_data_anomalies:
        print("Data Anomalies:")
        print("Empty")
        sys.exit(0)

    if args.show_data_consensus:
        print("Data Consensus:")
        print("Empty")
        sys.exit(0)

    if args.show_data_equivalence:
        print("Data Equivalence:")
        print("Empty")
        sys.exit(0)

    if args.show_data_trust:
        print("Data Trust:")
        print("Empty")
        sys.exit(0)

    if args.show_data_review_packs:
        print("Data Review Packs:")
        print("Empty")
        sys.exit(0)

    print("Running main application...")


if __name__ == "__main__":
    main()
