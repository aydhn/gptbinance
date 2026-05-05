# Policy Kernel & Invariant Engine

This module serves as the **Safety Constitution Layer** of the trading platform. It unifies the various rules scattered across risk, capital, event-risk, cross-book, and other modules into a single, declarative policy evaluation engine.

## Core Concepts

*   **Rules vs. Invariants:** Rules are general guidelines that can produce `ADVISORY`, `CAUTION`, or `BLOCK` verdicts and may be waivable. Invariants are non-bypassable, non-waivable fundamental safety truths that only produce `HARD_BLOCK` or `ALLOW`.
*   **Approval vs. Bypass:** Having control authorization (an approval) does *not* mean safety checks are bypassed. The policy kernel evaluates the action independently.
*   **Waivers:** Exceptions can only be granted to explicitly waivable rules, with strict scopes and TTLs. Invariants cannot be waived.
*   **Decision Proofs:** Every policy decision generates an auditable proof containing the evaluated rules, used evidence, precedence logic, and the final verdict.
*   **Policy Drift:** The kernel detects when actual behavior deviates from declared policy (e.g., a module allows an action that the policy constitution blocks).

## Why a Centralized Constitution?

Without a unified kernel, safety checks are distributed. A capital module might block an action while a risk module allows it. The policy kernel aggregates these checks, resolves conflicts deterministically, and provides a single, auditable "Why did this happen?" record.
