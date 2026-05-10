with open("app/release_plane/rollouts.py", "r") as f:
    content = f.read()

# We need to return a new instance instead of modifying the frozen one
new_content = content.replace(
"""        plan.current_stage = next_stage_id
        return plan""",
"""        # Create a new instance because models are frozen
        new_plan = plan.model_copy(update={"current_stage": next_stage_id})
        return new_plan""")

with open("app/release_plane/rollouts.py", "w") as f:
    f.write(new_content)
