class QualityEvaluator:
    @staticmethod
    def evaluate(portfolio_objects: list, wip_limits: list) -> dict:
        warnings = []
        top_priorities = [obj for obj in portfolio_objects if obj.commitment_class.name in ("PRIORITIZED", "COMMITTED")]
        if len(top_priorities) > 10:
            warnings.append("too_many_top_priorities")

        # simplified check for unfunded committed
        # assumes external linkage checks would feed this
        return {
            "status": "PASS" if not warnings else "WARN",
            "warnings": warnings
        }
