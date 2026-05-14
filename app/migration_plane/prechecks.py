def check_migration_capacity_prechecks():
    pass



# Cost plane evaluation integration
def prevent_unbudgeted_migration(has_budget: bool):
    if not has_budget:
        return "blocked"
    return "ready"
