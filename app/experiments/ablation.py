from app.experiments.models import AblationPlan


class AblationManager:
    def create_plan(self, plan_id: str, components: list[str]) -> AblationPlan:
        # A simple method mapping for ablation tests
        methods = {c: f"disable_{c}" for c in components}
        return AblationPlan(
            plan_id=plan_id, target_components=components, disable_methods=methods
        )
