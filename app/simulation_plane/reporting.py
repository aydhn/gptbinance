class SimulationReporter:
    def __init__(self, registry):
        self.registry = registry

    def generate_registry_summary(self) -> str:
        defs = self.registry.list_definitions()
        summary = (
            f"--- Simulation Registry Summary ---\nTotal Definitions: {len(defs)}\n"
        )
        for d in defs:
            summary += f" - {d.sim_id} [{d.sim_class.value}] mode: {d.mode.value}\n"
        return summary

    def generate_run_summary(self, run_id: str) -> str:
        run = self.registry.get_run(run_id)
        if not run:
            return f"Run {run_id} not found."
        return f"--- Simulation Run: {run.run_id} ---\nStrategy: {run.sim_ref.sim_id}\nAssumptions ID: {run.assumption_manifest_id}"
