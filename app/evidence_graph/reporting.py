from typing import List
from app.evidence_graph.models import (
    ArtefactRecord,
    RelationEdge,
    EvidenceCaseFile,
    GraphGapFinding,
    RedactionRecord,
)


class GraphReporter:
    @staticmethod
    def generate_summary(
        artefacts: List[ArtefactRecord],
        relations: List[RelationEdge],
        gaps: List[GraphGapFinding],
        redactions: List[RedactionRecord],
    ) -> str:
        report = []
        report.append("=== EVIDENCE GRAPH SUMMARY ===")
        report.append(f"Total Artefacts: {len(artefacts)}")
        report.append(f"Total Relations: {len(relations)}")
        report.append(f"Graph Gaps Detected: {len(gaps)}")
        report.append(f"Redaction Events: {len(redactions)}")
        return "\n".join(report)

    @staticmethod
    def format_artefact(artefact: ArtefactRecord, relations: List[RelationEdge]) -> str:
        report = []
        report.append(f"ARTEFACT: {artefact.id}")
        report.append(f"Type: {artefact.type.name}")
        report.append(f"Domain: {artefact.owner_domain}")
        report.append(f"Scope: {artefact.scope.scope_class.name}")
        report.append(f"Created: {artefact.created_at}")
        report.append(f"Immutable Ref: {artefact.immutable_ref}")
        report.append("Relations:")
        for r in relations:
            if r.source_id == artefact.id:
                report.append(f"  -> {r.relation_type.name} -> {r.target_id}")
            else:
                report.append(f"  <- {r.relation_type.name} <- {r.source_id}")
        return "\n".join(report)

    @staticmethod
    def format_case_file(case_file: EvidenceCaseFile) -> str:
        report = []
        report.append(f"CASE FILE: {case_file.case_id} ({case_file.case_class.name})")
        report.append(f"Completeness: {case_file.completeness.name}")
        report.append(f"Summary: {case_file.executive_summary}")
        report.append("Sections:")
        for s in case_file.sections:
            report.append(f"  - {s.title}: {len(s.artefact_refs)} refs")
        return "\n".join(report)
