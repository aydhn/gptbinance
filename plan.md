1. **Understand Orchestration Requirements**: Review user requirements to implement Orchestration Plane (Phase 137). The goal is to provide a unified orchestration framework separating intent, plan, dispatch, execution, validation, rollback, and final completion.
2. **Setup Domain Skeleton**: Build core files `models.py`, `enums.py`, `exceptions.py` inside `app/orchestration_plane` directory.
3. **Setup Specific Subdomains**: Implement registry, intents, action_graphs, plans, dependencies, handoffs, retries, compensation, rollback, completions, testing domains under `app/orchestration_plane/`.
4. **Hook into External Planes**: Adjust existing planes (`incentive`, `accountability`, `drift`, etc.) to require explicit references from the orchestration plane (creating caution responses otherwise). Add updates to observability, postmortem, and telegram planes.
5. **Add CLI Utilities**: Implement arguments and reporting functionality into `app/main.py`.
6. **Documentation**: Add docs `docs/695_*.md` to `docs/699_*.md` explaining architecture and definitions.
7. **Testing**: Write baseline unit tests `tests/test_orchestration_plane_*.py` for validations.
8. **Pre-commit**: Complete pre-commit step using `pre_commit_instructions` to ensure testing and review.
9. **Final Submission**: Provide detailed summary report back to the user covering executed tasks, file modifications, commands, test outcomes, deferred items, and the proposal for Phase 138.
