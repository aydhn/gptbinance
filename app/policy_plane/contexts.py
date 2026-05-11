from app.policy_plane.models import PolicyContext


class ContextBuilder:
    def __init__(self):
        self._context = {}

    def with_environment(self, env: str):
        self._context["environment"] = env
        return self

    def with_stage(self, stage: str):
        self._context["stage"] = stage
        return self

    def build(self) -> PolicyContext:
        return PolicyContext(**self._context)
