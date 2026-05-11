class ReportingManager:
    @staticmethod
    def generate_registry_summary(registry) -> str:
        migrations = registry.list_all()
        summary = "Migration Registry Summary:\n"
        for m in migrations:
            summary += f"- {m.migration_id}: {m.migration_class.value} ({m.version_pair.source_version} -> {m.version_pair.target_version})\n"
        return summary

    @staticmethod
    def generate_migration_report(migration_id: str, details: dict) -> str:
        return f"Migration Report for {migration_id}:\n{details}"
