# Policy Kernel & Safety Constitution Architecture

This document outlines the Phase 45 implementation of the Policy Kernel.

## What is the Policy Kernel?

The Policy Kernel serves as the ultimate safety constitution of the trading platform. It ensures that disparate rules from risk, capital, event-risk, cross-book, and other modules are evaluated in a unified context.

## Rules vs. Invariants

- **Rules** are policy declarations that can result in varying verdicts (e.g., `ADVISORY`, `CAUTION`, `BLOCK`). Rules may be *waivable* under specific conditions and scopes.
- **Invariants** are fundamental, non-bypassable truths. An invariant violation always results in a `HARD_BLOCK`. Invariants cannot be waived.

## Why Approval is not a Bypass

Having control approval to perform an action does not exempt that action from policy kernel evaluation. If an invariant is violated, the action is blocked regardless of the approval status. The policy kernel separates "is this authorized?" from "is this fundamentally safe according to our constitution?".

## Centralized Unification

By centralizing evaluation, the platform guarantees that conflict resolution (e.g., when risk says ALLOW but capital says BLOCK) is deterministic and that all decisions produce auditable proofs. This architecture exposes "policy drift" when the actual behavior of a module deviates from the declared policy.
