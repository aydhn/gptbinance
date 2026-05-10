class ControlPlaneRegistry:
    def register_command(self, command_id: str, release_plane_link: dict = None):
        # Link commands like hold, pause, rollback, hotfix_approval to release plane
        pass

    def validate_mutation_path(self, path: str):
        if path == "hidden_release_mutation":
             raise Exception("Hidden release mutation path rejected.")
