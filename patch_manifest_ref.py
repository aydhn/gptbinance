with open("app/release_plane/manifests.py", "r") as f:
    content = f.read()

new_content = content.replace(
"""            candidate_ref=candidate.candidate_id, # Simplified ref usage for demo""",
"""            candidate_ref={"candidate_id": candidate.candidate_id},"""
)

with open("app/release_plane/manifests.py", "w") as f:
    f.write(new_content)
