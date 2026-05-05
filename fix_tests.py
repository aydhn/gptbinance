import os

with open("app/order_lifecycle/client_ids.py", "r") as f:
    content = f.read()

content = content.replace(
    """        short_plan = plan_id[-6:] if len(plan_id) > 6 else plan_id
        short_leg = leg_id[-6:] if len(leg_id) > 6 else leg_id""",
    """        short_plan = plan_id[-7:] if len(plan_id) > 7 else plan_id
        short_leg = leg_id[-7:] if len(leg_id) > 7 else leg_id""",
)

with open("app/order_lifecycle/client_ids.py", "w") as f:
    f.write(content)

with open("app/order_lifecycle/state_machine.py", "r") as f:
    content = f.read()

content = content.replace(
    """        if to_state not in allowed_next and to_state not in cls.TERMINAL_STATES and current_state.current_state != LifecycleState.TIMEOUT_UNKNOWN:
             raise InvalidLifecycleTransitionError(f"Invalid transition {current_state.current_state} -> {to_state}")""",
    """        if to_state not in allowed_next and current_state.current_state != LifecycleState.TIMEOUT_UNKNOWN:
             raise InvalidLifecycleTransitionError(f"Invalid transition {current_state.current_state} -> {to_state}")""",
)

with open("app/order_lifecycle/state_machine.py", "w") as f:
    f.write(content)
