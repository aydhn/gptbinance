# Venue Shadow State & Account Digital Twin Architecture

This document describes the separation of Venue Truth vs Local Truth.

- **Venue Truth**: The exact snapshot fetched from the exchange.
- **Local Truth**: The assumed state based on the local order lifecycle, ledger, and crossbook.
- **Convergence Engine**: A separate process that checks for divergence (drift) between Venue Truth and Local Truth.

By maintaining this separation, the system can detect discrepancies early without automatically mutating (auto-repairing) the local state, which could hide deeper systemic issues.
