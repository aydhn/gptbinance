with open("app/main.py", "r") as f:
    content = f.read()

patch = """
    if args.show_evidence_graph_summary:
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        arts = repo.artefact_registry.list_artefacts()
        rels = repo.relation_registry.get_all_relations()
        gaps = repo.gap_detector.find_gaps()
        print(GraphReporter.generate_summary(arts, rels, gaps, []))
        return

    if getattr(args, 'show_artefact', None):
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        art = repo.artefact_registry.get_artefact(args.show_artefact)
        if art:
            rels = repo.relation_registry.get_all_relations()
            print(GraphReporter.format_artefact(art, rels))
        else:
            print("Artefact not found or repository empty in mock.")
        return

    if getattr(args, 'show_lineage', None):
        print(f"Lineage for {args.show_lineage}: [Mock: Backward trace: COMPLETE]")
        return

    if getattr(args, 'show_dependencies', None):
        print(f"Dependencies for {args.show_dependencies}: [Mock: Fanout: 0]")
        return

    if getattr(args, 'build_case_file', None) and getattr(args, 'case_class', None):
        print(f"Building {args.case_class} for {args.build_case_file}...")
        print("Case File Assembled: [Mock: COMPLETE]")
        return

    if getattr(args, 'show_case_file', None):
        print(f"Case File {args.show_case_file}: [Mock: 3 sections, COMPLETE]")
        return

    if getattr(args, 'build_evidence_pack', None) and getattr(args, 'pack_class', None):
        print(f"Building {args.pack_class} for {args.build_evidence_pack}...")
        print("Evidence Pack Built: [Mock: 5 artefacts, COMPLETE]")
        return

    if getattr(args, 'show_evidence_pack', None):
        print(f"Evidence Pack {args.show_evidence_pack}: [Mock: Freshness: GOOD]")
        return

    if getattr(args, 'query_evidence_by_symbol', None):
        print(f"Querying evidence for symbol {args.query_evidence_by_symbol}: [Mock: 0 artefacts found]")
        return

    if getattr(args, 'query_evidence_by_candidate', None):
        print(f"Querying evidence for candidate {args.query_evidence_by_candidate}: [Mock: 0 artefacts found]")
        return

    if getattr(args, 'show_graph_gaps', None):
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        gaps = repo.gap_detector.find_gaps()
        print(f"Graph Gaps Detected: {len(gaps)}")
        return

    if getattr(args, 'show_redaction_summary', None):
        print("Redaction Summary: [Mock: 0 restricted records]")
        return
"""

import re
content = re.sub(r'args = parser\.parse_args\(\)\n', r'args = parser.parse_args()\n' + patch, content)

with open("app/main.py", "w") as f:
    f.write(content)
