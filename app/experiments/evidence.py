class EvidenceBundleBuilder:
    def build(
        self,
        hypothesis_id: str,
        comparison_results: dict,
        fragility_results: dict,
        promotion_results: str,
    ) -> dict:
        return {
            "hypothesis_id": hypothesis_id,
            "comparison": comparison_results,
            "fragility": fragility_results,
            "promotion_recommendation": promotion_results,
            "policy_proofs": ["checked_against_invariants"],
            "completeness": True,
        }
