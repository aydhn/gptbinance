# Risk Plane & Limit State Governance Layer

This module provides the canonical, typed risk state generation, limit evaluation, breach classification, and deleveraging governance for the platform.

## Why this exists?
Without a unified Risk Plane, position sizes, limits, and market reality drift silently. Systems implement "hidden limit overrides" or auto-liquidators that obscure systemic risk.

## Core Principles
1. **No Auto-Liquidator**: The risk plane generates intents (`NO_NEW_EXPOSURE`, `EMERGENCY_DELEVERAGE_INTENT`), it does NOT execute trades directly.
2. **Explicit Trust Verdicts**: Risk state must be explicitly graded (`TRUSTED`, `CAUTION`, `DEGRADED`, `BLOCKED`, `REVIEW_REQUIRED`).
3. **Hard limits vs Soft limits**: Breaches are explicitly classified, and their responses strictly categorized.
4. **Cooldowns and Re-entry**: Once blocked by risk, re-entry requires explicit gates to clear (no bypasses).

## Flow
Positions/Ledger -> Canonical `RiskState` -> Evaluation against `RiskLimitRegistry` -> `RiskBreachRecord` -> `RiskResponseIntent` -> `RiskArtifactManifest`.
