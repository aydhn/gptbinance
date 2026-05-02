# Qualification & Certification Architecture and Profile Design

## Overview
This document describes the qualification and certification layer. The goal is not to automatically promote to live, but to provide a verifiable, evidence-backed "Go/No-Go" decision.

## Profile Logic
We separate qualification into distinct profiles:
- **paper_ready**
- **shadow_ready**
- **testnet_exec_ready**
- **canary_live_caution_ready**
- **full_live**

Each profile enforces specific test suites, evidence requirements, and mandatory negative tests. This ensures we don't apply mainnet rigor to paper trading, but we absolutely enforce it before touching real funds.

## Why Certification is not Auto-Deploy
Certification provides a verdict and a recommendation. A human (or a distinct, highly-privileged ops gate) must make the final active switch to a live target. This prevents accidental live deployments due to "green tests".
