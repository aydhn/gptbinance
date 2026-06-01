# Adaptation Plane Architecture

## 1. Introduction
The Adaptation Plane provides a canonical governance framework for managing fixes, countermeasures, hardening, rebaselines, and fitness restoration across the platform.

## 2. Core Concepts
*   **Triggers / Hypotheses:** Why is an adaptation needed and what is the root cause?
*   **Packages / Hardening:** What exactly is changing?
*   **Verification / Side-effects / Rebaseline:** Did the change work, what else did it affect, and is it the new normal?
*   **Trust:** Can we trust the adaptation state based on the evidence?

## 3. Key Distinctions
*   **Deployed != Verified:** A change in production is not automatically a verified fix.
*   **Verified != Fit:** A verified change might not restore the original fitness or might introduce unacceptable side effects.
*   **No Patch Theater:** Superficial fixes or threshold changes that mask underlying problems are not valid adaptations.
