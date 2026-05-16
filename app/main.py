import sys
import json
from datetime import datetime, timezone
from app.operating_model_plane.registry import CanonicalOperatingModelRegistry
from app.operating_model_plane.models import OperatingModelObject, RoleRef, OwnershipAssignment
from app.operating_model_plane.enums import OperatingObjectClass, RoleClass, OwnershipClass, CoverageClass

def build_dummy_registry():
    registry = CanonicalOperatingModelRegistry()
    role = RoleRef(role_id="r1", role_name="Trading Core Lead", role_class=RoleClass.ACCOUNTABLE_OWNER)
    owner = OwnershipAssignment(
        assignment_id="a1",
        target_id="surf_1",
        owner_role=role,
        ownership_class=OwnershipClass.PRIMARY,
        last_attested_at=datetime.now(timezone.utc)
    )
    obj = OperatingModelObject(
        operating_id="surf_1",
        object_class=OperatingObjectClass.SYSTEM_SURFACE,
        is_critical=True,
        primary_owner=owner,
        backup_coverage=CoverageClass.ON_CALL_24_7,
        escalation_chain=None
    )
    registry.register(obj)
    return registry

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python -m app.main [command]")
        return

    registry = build_dummy_registry()

    cmd = args[0]
    if cmd == "--show-operating-model-registry":
        print(json.dumps([o.dict() for o in registry.get_all()], indent=2, default=str))
    elif cmd == "--show-operating-object":
        print(f"Showing object {args[2]}...")
    elif cmd == "--show-role-definitions":
        print("Role definitions (Accountable, Responsible, Reviewer, Approver, Escalation)...")
    elif cmd == "--show-ownership-assignments":
        print("Ownership Assignments (Primary, Freshness, Warnings)...")
    elif cmd == "--show-sod":
        print("Segregation of Duties (Propose/Approve, Execute/Review) Violations...")
    elif cmd == "--show-operating-trust":
        from app.operating_model_plane.trust import OperatingModelTrustEngine
        engine = OperatingModelTrustEngine()
        res = engine.evaluate(registry.get_all()[0])
        print(json.dumps(res.dict(), indent=2, default=str))
    else:
        print(f"Command {cmd} acknowledged (Implementation stub for Operating Model Plane).")

if __name__ == "__main__":
    main()
