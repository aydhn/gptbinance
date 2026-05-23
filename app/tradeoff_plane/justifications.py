class JustificationIntegration:
    def justify_tradeoff(self):
        # harm-cost tradeoffs remedy-plane proportionality ve affected-party remedy refs gerektirsin
        pass


def check_tradeoff_rights_erosion(tradeoff_decision: dict, rights_registry) -> str:
    if rights_registry.detects_rights_stripping(tradeoff_decision):
        return "explicit caution: tradeoff justified while silently stripping rights"
    return "trusted"
