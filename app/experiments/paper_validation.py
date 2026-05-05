class PaperValidationRecommender:
    def recommend_next_step(self, comparison_results: dict) -> str:
        if comparison_results.get("verdict") == "improvement":
            return "qualifies_for_paper_shadow"
        return "keep_researching"
