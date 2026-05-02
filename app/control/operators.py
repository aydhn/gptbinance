from typing import Dict, Optional, List
from app.control.models import OperatorIdentity
from app.control.enums import OperatorRole


class OperatorRegistry:
    def __init__(self):
        self._operators: Dict[str, OperatorIdentity] = {}
        # Pre-seed for testing/local usage
        self.register(
            OperatorIdentity(
                id="local_admin",
                roles=[
                    OperatorRole.ADMIN,
                    OperatorRole.OPS,
                    OperatorRole.RISK,
                    OperatorRole.SECURITY,
                    OperatorRole.RELEASE,
                ],
                alias="admin",
            )
        )
        self.register(
            OperatorIdentity(id="local_ops", roles=[OperatorRole.OPS], alias="ops")
        )
        self.register(
            OperatorIdentity(id="local_risk", roles=[OperatorRole.RISK], alias="risk")
        )
        self.register(
            OperatorIdentity(
                id="local_security", roles=[OperatorRole.SECURITY], alias="security"
            )
        )
        self.register(
            OperatorIdentity(
                id="local_release", roles=[OperatorRole.RELEASE], alias="release"
            )
        )

    def register(self, op: OperatorIdentity):
        self._operators[op.id] = op

    def get_operator(self, op_id: str) -> Optional[OperatorIdentity]:
        return self._operators.get(op_id)

    def resolve_operator(self, op_id_or_alias: str) -> Optional[OperatorIdentity]:
        if op_id_or_alias in self._operators:
            return self._operators[op_id_or_alias]
        for op in self._operators.values():
            if op.alias == op_id_or_alias:
                return op
        return None


registry = OperatorRegistry()


def is_self_approval(requester: OperatorIdentity, approver: OperatorIdentity) -> bool:
    return requester.id == approver.id


def has_required_roles(
    operator: OperatorIdentity, required_roles: List[OperatorRole]
) -> bool:
    if not required_roles:
        return True
    if OperatorRole.ADMIN in operator.roles:
        return True
    # At least one of the required roles? Or all? Let's say at least one of the required roles is present.
    for r in required_roles:
        if r in operator.roles:
            return True
    return False
