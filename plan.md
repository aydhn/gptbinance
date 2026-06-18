1. **Setup & Verification**:
   - Call `pre_commit_instructions` tool to understand constraints (this serves the "ensure proper testing, verification, review, and reflection are done" requirement).
2. **Create Core Netting Plane Models & Enums**:
   - `app/netting_plane/enums.py`, `exceptions.py`, `models.py`
3. **Build Framework Components**:
   - Base definitions, registry, objects, nettings, subjects, counterparties, capacities, obligations, sets.
4. **Implement Eligibility & Mutuality Policies**:
   - Eligibility, mutuality, maturity, due/payable, contingent, disputed, stayed conditions.
5. **Implement Valuation & Setoff Mechanisms**:
   - Conversions, valuations, closeouts, setoff rights (contractual, statutory, equitable).
6. **Implement Execution & Audit Modules**:
   - Payment, settlement, closeout netting, novation, cross-product, insolvency, stay blocks, partials, residuals.
   - Mistaken setoffs, reversals, anti-duplication, gross leg preservation.
7. **Implement Analytics & Trust Engines**:
   - Comparisons, forecasting, debt, readiness, equivalence, divergence, quality, trust.
8. **Integrate with Existing Planes**:
   - Escrow, waterfall, collateral, insurance, indemnity, warranty, reliance, etc.
   - Update `app/main.py`, `app/readiness_board`, `app/reliability`, `app/observability`, `app/policy_kernel`, `app/evidence_graph`, `app/telegram`, etc.
9. **Write Tests & Documentation**:
   - `tests/test_netting_plane_*.py`
   - `docs/820_...`, `docs/821_...`, `docs/822_...`, `docs/823_...`, `docs/824_...`
10. **Final Validation**:
    - Run `pytest` or basic import checks to ensure syntax and structure are sound.
