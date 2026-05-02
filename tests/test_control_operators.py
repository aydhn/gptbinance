from app.control.operators import registry, is_self_approval, has_required_roles
from app.control.enums import OperatorRole
from app.control.models import OperatorIdentity


def test_operator_registry():
    op = registry.resolve_operator("local_ops")
    assert op is not None
    assert OperatorRole.OPS in op.roles


def test_is_self_approval():
    op1 = OperatorIdentity(id="op1", roles=[])
    op2 = OperatorIdentity(id="op2", roles=[])
    assert is_self_approval(op1, op1) is True
    assert is_self_approval(op1, op2) is False


def test_has_required_roles():
    op = OperatorIdentity(id="op", roles=[OperatorRole.OPS])
    assert has_required_roles(op, [OperatorRole.OPS]) is True
    assert has_required_roles(op, [OperatorRole.RISK]) is False

    admin = OperatorIdentity(id="admin", roles=[OperatorRole.ADMIN])
    assert has_required_roles(admin, [OperatorRole.RISK]) is True
