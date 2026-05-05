# Remediation Orchestration Layer

## Purpose
This layer provides a structured, safe, and auditable framework for resolving operational findings (drift, orphans, mismatches) across the platform.

**CRITICAL PRINCIPLE: NO SILENT AUTO-FIX.**
The system will never automatically mutate venue state. All remediations are governed by:
1. Explicit compilation into a `RemediationPack`.
2. Mandatory Blast Radius analysis.
3. Preflight and Dry-Run simulations.
4. Approval-bound application for risky actions.
5. Strict verification of outcomes.

## Flow
`Finding` -> `Recipe` -> `Pack` -> `Preflight` -> `Simulation` -> `Apply/Request` -> `Verification` -> `Evidence`

## Why Not Auto-Fix?
Auto-fixing hides underlying issues, can trigger infinite loops (e.g., repeatedly cancelling and recreating orders due to a sync bug), and destroys auditability. By forcing a structured `RemediationPack`, we ensure every action is deliberate, auditable, and reviewed.
