from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set
from datetime import datetime
from app.interpretation_plane.enums import (
    InterpretationClass, TextUnitClass, ReadingClass, AmbiguityClass,
    ClarificationClass, ConflictClass, HierarchyClass, ScopeClass,
    DriftClass, EquivalenceVerdict, InterpretationTrustVerdict
)

@dataclass
class InterpretationPlaneConfig:
    strict_ambiguity_blocker: bool = True
    prevent_silent_reinterpretation: bool = True
    require_beneficiary_safe_construction: bool = True

@dataclass
class TextRecord:
    text_id: str
    content: str
    unit_class: TextUnitClass
    source_ref: str
    is_retired: bool = False

@dataclass
class AmbiguityRecord:
    ambiguity_id: str
    text_id: str
    ambiguity_class: AmbiguityClass
    description: str
    is_resolved: bool = False
    resolution_ref: Optional[str] = None

@dataclass
class ReadingRecord:
    reading_id: str
    text_id: str
    reading_class: ReadingClass
    postulated_meaning: str
    basis_notes: str
    is_beneficiary_safe: bool = False
    is_rejected: bool = False

@dataclass
class ClarificationRecord:
    clarification_id: str
    ambiguity_id: str
    clarification_class: ClarificationClass
    clarified_meaning: str
    is_sufficient: bool = True

@dataclass
class CanonicalMeaningRecord:
    canon_id: str
    text_id: str
    reading_id: str
    meaning: str
    published_at: datetime
    is_authoritative: bool = True
    superseded_by: Optional[str] = None

@dataclass
class InterpretationDebtRecord:
    unresolved_ambiguity_debt: int = 0
    stale_canon_debt: int = 0
    selective_reading_debt: int = 0
    context_overreach_debt: int = 0
    beneficiary_erasing_reading_debt: int = 0

@dataclass
class InterpretationTrustReport:
    verdict: InterpretationTrustVerdict
    text_clarity: str
    ambiguity_discipline: str
    canonical_freshness: str
    conflict_cleanliness: str
    blockers: List[str]

@dataclass
class InterpretationObject:
    interpretation_id: str
    interp_class: InterpretationClass
    texts: Dict[str, TextRecord] = field(default_factory=dict)
    readings: Dict[str, ReadingRecord] = field(default_factory=dict)
    ambiguities: Dict[str, AmbiguityRecord] = field(default_factory=dict)
    clarifications: Dict[str, ClarificationRecord] = field(default_factory=dict)
    canonical_meanings: Dict[str, CanonicalMeaningRecord] = field(default_factory=dict)
    debt: InterpretationDebtRecord = field(default_factory=InterpretationDebtRecord)

    def get_trust_report(self) -> InterpretationTrustReport:
        blockers = []
        if any(not a.is_resolved for a in self.ambiguities.values()):
            blockers.append("Unresolved Material Ambiguity")

        verdict = InterpretationTrustVerdict.TRUSTED
        if blockers:
            verdict = InterpretationTrustVerdict.BLOCKED

        return InterpretationTrustReport(
            verdict=verdict,
            text_clarity="Checked",
            ambiguity_discipline="Clean" if not blockers else "Failed",
            canonical_freshness="Fresh",
            conflict_cleanliness="Clean",
            blockers=blockers
        )
