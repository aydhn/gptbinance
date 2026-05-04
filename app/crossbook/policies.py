class CrossBookPolicyManager:
    def get_policy(self, profile: str) -> dict:
        return {"max_directional": 50000}
