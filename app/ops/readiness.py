class OpsReadinessCheck:
    def evaluate_host_posture(self, capacity_report) -> None:
        if capacity_report.available_headroom_percent < 20.0:
            print(
                "[OPS] WARNING: Host headroom is low. Operating near capacity limits."
            )
        else:
            print("[OPS] Host posture healthy.")
