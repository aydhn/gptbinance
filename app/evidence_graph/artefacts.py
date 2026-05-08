class EvidenceArtefact:
    def add_allocation_artefact(self, type: str, artefact_id: str):
        # type in [allocated_by, budgeted_under, netted_with, clipped_by, deferred_by, diverged_allocation_from]
        pass

class ExecutionArtefactFamily:
    FAMILIES = ["venue_defs", "execution_plans", "manifests", "attempts"]
    RELATIONS = ["executed_under", "routed_by", "retried_under", "replaced_by", "filled_with", "diverged_execution_from"]
