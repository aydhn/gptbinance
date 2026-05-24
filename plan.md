1. **Read Core Files**: Explore `app/main.py` and a couple of existing planes (e.g., `app/interpretation_plane/policy.py`) using `run_in_bash_session` to understand how to correctly append new commands and integrations without causing syntax errors.
2. **Execute Python Scaffolding Script**: Create and run the Python scaffolding script (`scaffold_phase121.py`) using `run_in_bash_session` to generate the 180+ required files for the Obligation Plane (Phase 121), including models, lifecycle rule engines, and integrations.
3. **Verify File Generation**: Use `run_in_bash_session` with `ls -la app/obligation_plane/` and `pytest` to confirm that the generated files exist and that there are no syntax errors.
4. **Execute Testing and Docs Script**: Create and run the `scaffold_tests_docs_cli.py` script to generate tests, docs, and update `app/main.py`.
5. **Run Tests**: Execute `pytest tests/test_obligation_plane_*.py` using `run_in_bash_session` to verify that the generated structure is sound and correctly implemented.
6. **Complete Pre-commit Steps**: Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
7. **Finalize output**: Create the `FINAL_OUTPUT.md` file with the required summary, tree, commands, and next phase plan.
