class ControlPlaneRegistry:

    def register_manual_intervention(self, command_id: str, related_postmortem_action_id: str = None):
        pass


    def register_command(self, command_id: str, release_plane_link: dict = None):
        # Link commands like hold, pause, rollback, hotfix_approval to release plane
        pass

    def validate_mutation_path(self, path: str):
        if path == "hidden_release_mutation":
             raise Exception("Hidden release mutation path rejected.")

class ControlRegistryMigrationRef:
    def migration_approval_commands(self, registry=None):
        pass

    def register_security_intervention(self, command_id: str, related_security_action_id: str = None):
        if command_id in ["emergency_revoke", "boundary_isolation", "secret_rotation_request"]:
             pass
        else:
             raise Exception("Hidden security-impacting control path rejected.")
