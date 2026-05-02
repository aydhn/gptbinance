# Release Engineering Module

This module is responsible for:
- Versioning and manifest generation
- Creating reproducible build bundles with dependency locks
- Probing the host for suitability
- Checking compatibility and registering/executing migrations
- Planning upgrades and rollbacks (dry-run first)
- Bootstrapping the environment safely

**Why Dry-Run?**
Destructive migrations or live runtime upgrades can corrupt data. Dry-runs are mandatory before applying.

**Live Runtime Upgrades**
Silent live upgrades are prohibited. The runtime must be drained and stopped.
