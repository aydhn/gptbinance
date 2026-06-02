class AccountabilityRegistryBase:
    pass

class DutyEvaluatorBase:
    pass

class ConsequenceEvaluatorBase:
    pass

class TrustEvaluatorBase:
    pass

class AccountabilityMetadata:
    def __init__(self, owner: str = None, scope: str = None):
        self.owner = owner
        self.scope = scope
