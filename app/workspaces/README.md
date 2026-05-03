# Workspaces and Profile Isolation

This module provides a robust framework for managing multiple operation contexts (profiles) within identical codebases.

## Why Workspace/Profile Isolation?

As the platform evolves, running `paper`, `testnet`, and `live` strategies within the same codebase risks cross-contamination.
A single shared `data/` or `config/` directory can easily lead to executing a testnet order on a live account or restoring a live backup into a testnet environment.

## Core Concepts

1. **Workspace**: A logical grouping of configuration, representing a single tenant or project (e.g., `research_lab`, `live_ops`).
2. **Profile**: A specific execution context within a workspace (e.g., `paper_default`, `canary_live_caution`). Each profile carries strict rules about risk, capability, and scope.
3. **Context**: The active `Workspace` + `Profile` combination. Explicit context switching is required; there is no implicit fallback.
4. **Scoped Paths**: Every profile has dedicated paths for state, config, artifacts, etc. Sharing paths across profiles, especially if one is live-affecting, triggers severe blockers.

## Policies
- **Explicit Context Switching**: You cannot execute a live action without explicitly loading and confirming the live context.
- **Shared Mutable Roots are Dangerous**: State and artifact sharing is flagged by the contamination checker.
- **Local-first Isolation**: This is not a multi-tenant SaaS. This is a local-first safety boundary.
