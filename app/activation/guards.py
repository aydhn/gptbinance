def activation_guard(verdict):
    if verdict.verdict_class.name != "ALLOW":
        raise Exception("Activation blocked")

class ActivationGuardMigrationRef:
    def migration_blocker(self, incomplete_migrations=None):
        pass
