class ReliabilityLinkage:
    def evaluate_cost_vs_reliability(self, cost_saved: float, incident_risk: float):
        if cost_saved > 0 and incident_risk > 0.5:
             return "caution_cheap_but_fragile"
        return "ok"
