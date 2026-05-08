class OrderIntentContext:
    def compile_intent(self, allocation_intent_ref: str):
        # Tie allocation manifest to order intent lineage
        pass


class CompileContext:
    def __init__(self):
        self.execution_plan_refs = []
        self.compile_blockers = []

    def add_execution_plan(self, plan_id: str):
        self.execution_plan_refs.append(plan_id)

    def add_blocker(self, blocker: str):
        self.compile_blockers.append(blocker)
