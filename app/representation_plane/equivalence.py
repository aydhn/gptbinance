class RepresentationEquivalenceAnalyzer:
    @staticmethod
    def compare_environments(replay_rep, paper_rep, probation_rep, live_rep):
        divergences = []
        if live_rep.content != replay_rep.content:
            divergences.append("Content mismatch between replay and live.")
        if live_rep.audience != paper_rep.audience:
            divergences.append("Audience mismatch across environments.")

        is_equivalent = len(divergences) == 0
        return {
            "equivalent": is_equivalent,
            "divergences": divergences
        }
