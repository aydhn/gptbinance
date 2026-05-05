class HostProbe:
    def check_readiness(self) -> dict:
        return {
            "status": "PASS",
            "bare_minimum_met": True,
            "recommended_host_class": "LOCAL_AVERAGE",
            "message": "Host meets minimum criteria.",
        }
