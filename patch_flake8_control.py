import os

files_to_fix = [
    "app/control_plane/apply.py",
    "app/control_plane/approvals.py",
    "app/control_plane/divergence.py",
    "app/control_plane/dry_runs.py",
    "app/control_plane/enums.py",
    "app/control_plane/equivalence.py",
    "app/control_plane/exceptions.py",
    "app/control_plane/exceptions_tokens.py",
    "app/control_plane/freezes.py",
    "app/control_plane/killswitch.py",
    "app/control_plane/manifests.py",
    "app/control_plane/models.py",
    "app/control_plane/pauses.py",
    "app/control_plane/previews.py",
    "app/control_plane/registry.py",
    "app/control_plane/repository.py",
    "app/control_plane/revoke.py",
    "app/control_plane/rollback.py",
    "app/control_plane/scopes.py",
    "app/control_plane/trust.py",
    "app/control_plane/unfreezes.py"
]

for f in files_to_fix:
    if os.path.exists(f):
        os.system(f"python -m black {f}")
