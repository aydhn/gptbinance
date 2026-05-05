# Experiment Governance & Controlled Research Loop

This module provides a disciplined, offline-first framework for translating operational findings into hypotheses, conducting controlled experiments (with baselines, ablations, and sensitivity scans), and evaluating candidates for promotion to paper/shadow environments.

**Key Principles:**
1. **No Live Optimization:** Experiments never mutate live configuration automatically.
2. **Baseline Discipline:** Every candidate must be compared against a frozen baseline.
3. **Evidence-Based Promotion:** Success in an offline experiment only qualifies a candidate for further review (e.g., paper trading), not live deployment.
4. **Fragility Awareness:** Improvements must be robust across regimes and time splits. Overfitting and small sample sizes are explicitly flagged.
