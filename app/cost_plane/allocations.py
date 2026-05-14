from app.cost_plane.models import AllocationPolicy, AllocationRecord, SpendRecord
from app.cost_plane.enums import AllocationClass
from app.cost_plane.base import AllocationEvaluatorBase
from app.cost_plane.exceptions import InvalidAllocationPolicyError
import uuid

class AllocationManager(AllocationEvaluatorBase):
    def __init__(self):
        self._policies: dict[str, AllocationPolicy] = {}
        self._records: list[AllocationRecord] = []

    def define_policy(self, allocation_class: AllocationClass, rules: dict, lineage_refs: list[str]) -> AllocationPolicy:
        policy = AllocationPolicy(
            policy_id=str(uuid.uuid4()),
            allocation_class=allocation_class,
            rules=rules,
            lineage_refs=lineage_refs
        )
        self._policies[policy.policy_id] = policy
        return policy

    def evaluate(self, allocation_policy: AllocationPolicy, target_spend: SpendRecord) -> list[AllocationRecord]:
        if not allocation_policy.rules:
             raise InvalidAllocationPolicyError("Allocation policy must have rules")

        records = []
        if allocation_policy.allocation_class == AllocationClass.DIRECT:
             target = allocation_policy.rules.get("target")
             record = AllocationRecord(
                 allocation_id=str(uuid.uuid4()),
                 spend_id=target_spend.spend_id,
                 policy_id=allocation_policy.policy_id,
                 allocated_to=target,
                 amount=target_spend.amount,
                 currency=target_spend.currency
             )
             records.append(record)
             self._records.append(record)
        return records

    def list_policies(self) -> list[AllocationPolicy]:
        return list(self._policies.values())

    def list_records(self) -> list[AllocationRecord]:
        return self._records
