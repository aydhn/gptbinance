from typing import Dict, Any, List

class ReleasePlaneReporter:
    def summarize_registry(self, releases: List[Any]) -> Dict[str, Any]:
        return {
            "total_releases": len(releases),
            "classes": list(set(getattr(r, "release_class", str(r.release_class)) for r in releases))
        }

    def summarize_candidate(self, candidate: Any) -> Dict[str, Any]:
        return {
            "candidate_id": candidate.candidate_id,
            "readiness_class": candidate.readiness_class,
            "bundle_hash": candidate.bundle.bundle_hash if getattr(candidate, "bundle", None) else None
        }

    def format_trust_verdict(self, verdict: Any) -> str:
        return f"Trust Verdict: {verdict.verdict} for Candidate {getattr(verdict.candidate_ref, 'candidate_id', '')}"
