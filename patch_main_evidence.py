import re

with open("app/main.py", "r") as f:
    content = f.read()

imports = """
from app.evidence_graph.models import EvidenceGraphConfig, ArtefactScope
from app.evidence_graph.enums import CaseFileClass, ScopeClass, QueryClass
from app.evidence_graph.repository import EvidenceGraphRepository
from app.evidence_graph.reporting import GraphReporter
"""

if "from app.evidence_graph" not in content:
    content = content.replace("from typing import", imports + "\nfrom typing import")


args_patch = """
    # Evidence Graph options
    parser.add_argument("--show-evidence-graph-summary", action="store_true", help="Show evidence graph summary")
    parser.add_argument("--show-artefact", type=str, help="Show artefact metadata")
    parser.add_argument("--show-lineage", type=str, help="Show artefact lineage")
    parser.add_argument("--show-dependencies", type=str, help="Show downstream dependencies")
    parser.add_argument("--build-case-file", type=str, help="Build case file by ID")
    parser.add_argument("--case-class", type=str, help="Case file class (e.g. incident_case)")
    parser.add_argument("--show-case-file", type=str, help="Show existing case file")
    parser.add_argument("--build-evidence-pack", type=str, help="Build evidence pack by ID")
    parser.add_argument("--pack-class", type=str, help="Evidence pack class")
    parser.add_argument("--show-evidence-pack", type=str, help="Show evidence pack")
    parser.add_argument("--query-evidence-by-symbol", type=str, help="Query evidence graph by symbol")
    parser.add_argument("--query-evidence-by-candidate", type=str, help="Query evidence graph by candidate ID")
    parser.add_argument("--show-graph-gaps", action="store_true", help="Show graph gaps")
    parser.add_argument("--show-redaction-summary", action="store_true", help="Show redaction summary")
"""

if "--show-evidence-graph-summary" not in content:
    content = content.replace("parser.parse_args()", args_patch + "\n    args = parser.parse_args()")
    content = content.replace("args = parser.parse_args()", "") # clean up duplicate if any


logic_patch = """
    if args.show_evidence_graph_summary:
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        # Provide mock data or query actual registry
        arts = repo.artefact_registry.list_artefacts()
        rels = repo.relation_registry.get_all_relations()
        gaps = repo.gap_detector.find_gaps()
        print(GraphReporter.generate_summary(arts, rels, gaps, []))
        return

    if args.show_artefact:
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        art = repo.artefact_registry.get_artefact(args.show_artefact)
        if art:
            rels = repo.relation_registry.get_all_relations()
            print(GraphReporter.format_artefact(art, rels))
        else:
            print("Artefact not found or repository empty in mock.")
        return

    if args.show_lineage:
        print(f"Lineage for {args.show_lineage}: [Mock: Backward trace: COMPLETE]")
        return

    if args.show_dependencies:
        print(f"Dependencies for {args.show_dependencies}: [Mock: Fanout: 0]")
        return

    if args.build_case_file and args.case_class:
        print(f"Building {args.case_class} for {args.build_case_file}...")
        print("Case File Assembled: [Mock: COMPLETE]")
        return

    if args.show_case_file:
        print(f"Case File {args.show_case_file}: [Mock: 3 sections, COMPLETE]")
        return

    if args.build_evidence_pack and args.pack_class:
        print(f"Building {args.pack_class} for {args.build_evidence_pack}...")
        print("Evidence Pack Built: [Mock: 5 artefacts, COMPLETE]")
        return

    if args.show_evidence_pack:
        print(f"Evidence Pack {args.show_evidence_pack}: [Mock: Freshness: GOOD]")
        return

    if args.query_evidence_by_symbol:
        print(f"Querying evidence for symbol {args.query_evidence_by_symbol}: [Mock: 0 artefacts found]")
        return

    if args.query_evidence_by_candidate:
        print(f"Querying evidence for candidate {args.query_evidence_by_candidate}: [Mock: 0 artefacts found]")
        return

    if args.show_graph_gaps:
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        gaps = repo.gap_detector.find_gaps()
        print(f"Graph Gaps Detected: {len(gaps)}")
        return

    if args.show_redaction_summary:
        print("Redaction Summary: [Mock: 0 restricted records]")
        return
"""

if "args.show_evidence_graph_summary" not in content:
    content = re.sub(r'(if args\.run_live:)', logic_patch + r'\n    \1', content)

with open("app/main.py", "w") as f:
    f.write(content)
