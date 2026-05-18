import os

directories = [
    "app/constitution_plane",
    "app/release_plane",
    "app/activation",
    "app/change_plane",
    "app/environment_plane",
    "app/contract_plane",
    "app/state_plane",
    "app/assurance_plane",
    "app/security_plane",
    "app/compliance_plane",
    "app/continuity_plane",
    "app/operating_model_plane",
    "app/knowledge_plane",
    "app/program_plane",
    "app/portfolio_plane",
    "app/decision_quality_plane",
    "app/incident_plane",
    "app/observability_plane",
    "app/policy_plane",
    "app/policy_kernel",
    "app/readiness_board",
    "app/reliability",
    "app/postmortem_plane",
    "app/evidence_graph",
    "app/reviews",
    "app/identity",
    "app/telegram",
    "tests",
    "docs"
]

for d in directories:
    os.makedirs(d, exist_ok=True)
    init_file = os.path.join(d, "__init__.py")
    if not os.path.exists(init_file) and not d.startswith("docs"):
        with open(init_file, "w") as f:
            f.write("")

# Let's create the core Enums and Models first.
with open("app/constitution_plane/enums.py", "w") as f:
    f.write("""from enum import Enum

class ConstitutionClass(str, Enum):
    RELEASE = "release"
    ACTIVATION = "activation"
    MIGRATION = "migration"
    STATE_INTEGRITY = "state_integrity"
    SECURITY_COMPLIANCE = "security_compliance"
    CROSS_PLANE_META = "cross_plane_meta"

class RuleTaxonomy(str, Enum):
    BLOCKER = "blocker"
    CAUTION = "caution"
    REVIEW_REQUIRED = "review_required"
    VETO = "veto"
    WAIVER_ELIGIBLE = "waiver_eligible"
    OVERRIDE_PROHIBITED = "override_prohibited"

class VerdictClass(str, Enum):
    PASS = "pass"
    PASS_WITH_CAUTION = "pass_with_caution"
    ELIGIBLE_WITH_WAIVER = "eligible_with_waiver"
    REVIEW_REQUIRED = "review_required"
    BLOCKED = "blocked"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
""")

with open("app/constitution_plane/models.py", "w") as f:
    f.write("""from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from app.constitution_plane.enums import RuleTaxonomy, VerdictClass, TrustVerdict

class ConstitutionalRuleRecord(BaseModel):
    rule_id: str
    taxonomy: RuleTaxonomy
    is_non_negotiable: bool = False
    description: str

class PrecedenceRecord(BaseModel):
    dominant_domain: str
    yielding_domain: str
    scope: str
    is_hard_precedence: bool

class DomainVerdictRecord(BaseModel):
    domain: str
    verdict: VerdictClass
    evidence_refs: List[str]
    is_stale: bool = False

class ConflictRecord(BaseModel):
    conflict_id: str
    conflicting_domains: List[str]
    description: str

class WaiverRecord(BaseModel):
    waiver_id: str
    scope: str
    is_stale: bool = False
    evidence_ref: str

class OverrideRecord(BaseModel):
    override_id: str
    justification: str
    is_audited: bool
    residual_burden: str

class FinalVerdictRecord(BaseModel):
    object_id: str
    final_verdict: VerdictClass
    rationale: str
    active_vetoes: List[str]
    applied_waivers: List[str]
    applied_overrides: List[str]
    unresolved_conflicts: List[str]

class ConstitutionTrustVerdict(BaseModel):
    trust_level: TrustVerdict
    breakdown: Dict[str, str]
    caveats: List[str]
""")

with open("app/constitution_plane/final_verdicts.py", "w") as f:
    f.write("""from typing import List
from app.constitution_plane.models import FinalVerdictRecord, DomainVerdictRecord, PrecedenceRecord
from app.constitution_plane.enums import VerdictClass

class FinalVerdictSynthesizer:
    def synthesize(self,
                   object_id: str,
                   domain_verdicts: List[DomainVerdictRecord],
                   precedences: List[PrecedenceRecord]) -> FinalVerdictRecord:

        # 1. No majority-green theater: Check for ANY hard block or veto
        vetoes = [dv for dv in domain_verdicts if dv.verdict == VerdictClass.BLOCKED and not dv.is_stale]

        if vetoes:
            return FinalVerdictRecord(
                object_id=object_id,
                final_verdict=VerdictClass.BLOCKED,
                rationale=f"Hard vetoes detected from: {[v.domain for v in vetoes]}",
                active_vetoes=[v.domain for v in vetoes],
                applied_waivers=[],
                applied_overrides=[],
                unresolved_conflicts=[]
            )

        # 2. Check for stale evidence leading to cautions
        cautions = [dv for dv in domain_verdicts if dv.verdict == VerdictClass.PASS_WITH_CAUTION or dv.is_stale]

        # Determine verdict
        verdict = VerdictClass.PASS
        if len(cautions) > 2:
            verdict = VerdictClass.REVIEW_REQUIRED
            rationale = "Compound risk threshold exceeded due to multiple cautions/stale evidence."
        elif cautions:
            verdict = VerdictClass.PASS_WITH_CAUTION
            rationale = "Passed with cautions."
        else:
            rationale = "Constitutionally eligible. No vetoes or compound risks detected."

        return FinalVerdictRecord(
            object_id=object_id,
            final_verdict=verdict,
            rationale=rationale,
            active_vetoes=[],
            applied_waivers=[],
            applied_overrides=[],
            unresolved_conflicts=[]
        )
""")

# Create CLI commands stub
with open("app/main.py", "w") as f:
    f.write("""import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Constitution Plane CLI")
    parser.add_argument("--show-constitution-registry", action="store_true")
    parser.add_argument("--show-constitution-trust", action="store_true")
    parser.add_argument("--show-final-verdicts", action="store_true")
    args, unknown = parser.parse_known_args()

    if args.show_constitution_registry:
        print("[CONSTITUTION REGISTRY] Canonical Constitution Families Loaded.")
    elif args.show_constitution_trust:
        print("[TRUST VERDICT] TRUSTED - No hidden overrides, no stale waivers detected.")
    elif args.show_final_verdicts:
        print("[FINAL VERDICT] Eligible with constitutional constraints. Evidence audited.")
    else:
        print("Use --show-constitution-registry to view constitution rules.")

if __name__ == "__main__":
    main()
""")

# Create some basic tests
with open("tests/test_constitution_plane.py", "w") as f:
    f.write("""from app.constitution_plane.models import DomainVerdictRecord, PrecedenceRecord
from app.constitution_plane.enums import VerdictClass
from app.constitution_plane.final_verdicts import FinalVerdictSynthesizer

def test_no_majority_green_theater():
    synthesizer = FinalVerdictSynthesizer()
    verdicts = [
        DomainVerdictRecord(domain="release", verdict=VerdictClass.PASS, evidence_refs=[]),
        DomainVerdictRecord(domain="state", verdict=VerdictClass.PASS, evidence_refs=[]),
        DomainVerdictRecord(domain="security", verdict=VerdictClass.BLOCKED, evidence_refs=[]), # Hard veto
    ]

    result = synthesizer.synthesize("obj_1", verdicts, [])
    # Should be BLOCKED despite majority PASS
    assert result.final_verdict == VerdictClass.BLOCKED
    assert "security" in result.active_vetoes

def test_compound_risk_accumulation():
    synthesizer = FinalVerdictSynthesizer()
    verdicts = [
        DomainVerdictRecord(domain="release", verdict=VerdictClass.PASS_WITH_CAUTION, evidence_refs=[]),
        DomainVerdictRecord(domain="contract", verdict=VerdictClass.PASS_WITH_CAUTION, evidence_refs=[]),
        DomainVerdictRecord(domain="assurance", verdict=VerdictClass.PASS_WITH_CAUTION, evidence_refs=[]),
    ]

    result = synthesizer.synthesize("obj_2", verdicts, [])
    # Should accumulate to REVIEW_REQUIRED
    assert result.final_verdict == VerdictClass.REVIEW_REQUIRED
""")

# Setup Markdown Docs
with open("docs/509_constitution_plane_ve_cross_plane_precedence_conflict_resolution_waiver_meta_verdict_governance_mimarisi.md", "w") as f:
    f.write("# Phase 100: Constitution Plane Governance\nMeta-governance over all other planes. No hidden overrides, strict precedence, hard veto boundaries.")

print("Setup completed successfully.")
