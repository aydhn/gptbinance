"""
policies.py
"""


class CrossBookPolicyManager:
    def __init__(self, profile: str = "paper_default"):
        self.profile = profile

    def get_max_combined_exposure(self) -> float:
        if self.profile == "canary_live_caution":
            return 50000.0
        return 100000.0

    def get_max_borrow_dependency_threshold(self) -> float:
        if self.profile in ["canary_live_caution", "derivatives_testnet"]:
            return 10000.0
        return 50000.0
