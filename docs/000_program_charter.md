# Program Charter

## Project Mission
To build a resilient, Python-only, zero-budget Binance trading infrastructure capable of transitioning seamlessly from research to live execution. The system must support spot, margin, and futures trading, prioritizing risk management, operational robustness, and statistical discipline over high-frequency performance or theoretical profitability.

## Hard Constraints
1.  **Zero Budget:** No paid APIs, databases, message buses, SaaS tools, or proprietary services. Only free, open-source, or local tools.
2.  **No HTML Scraping/Browser Automation:** Interaction must be strictly through official Binance APIs or documented Python libraries.
3.  **Python-Only System:** The core architecture and business logic must be implemented in Python.
4.  **No Dashboard:** Operator interaction and monitoring will be handled exclusively via CLI, logs, and Telegram. No web UI.
5.  **Binance-Only Execution Scope:** The initial scope is strictly limited to Binance.
6.  **Realistic Hardware/Network Assumptions:** Designed to run reliably on commodity hardware with standard internet connections. Not designed for colocation or specialized hardware.
7.  **Not HFT:** Target operational frequency is low-to-medium (e.g., minutes to hours, not microseconds).
8.  **No Blind "AI Magic":** ML components are optional, must be benchmarked against naive baselines, and are strictly subordinate to rigid risk controls.
9.  **Operator Experience:** Telegram is the primary interface for alerts, health checks, and critical interventions.

## Design Philosophy
*   **Risk-First, Execution-Second, Alpha-Third:** The system must survive above all else. Execution must be reliable before strategies are deployed. Strategies are the final, most replaceable component.
*   **Safety Over Cleverness:** Prefer explicit, deterministic logic over implicit, complex abstractions.
*   **Auditability:** Every significant action, state change, and error must be logged and traceable.
*   **Idempotency:** Operational workflows (startup, recovery) should be safely repeatable.

## Definition of Success
*   A stable, reliable infrastructure that can run unattended for days, correctly handling edge cases (disconnects, partial fills, API rate limits) without operator intervention.
*   A clean separation of concerns allowing researchers to backtest and deploy strategies without touching execution or risk code.
*   A system that fails safely (e.g., halting trading and alerting the operator) when an unrecoverable error occurs.

## Definition of Failure
*   Loss of funds due to software bugs, unhandled exceptions, or bypassed risk controls.
*   "Silent failures" where the system stops functioning but does not alert the operator.
*   A codebase that is too complex to understand, test, or modify safely.

## Expectancy and Edge
This system explicitly seeks robust statistical expectancy, not fantasy guarantees. It is a tool for executing disciplined strategies, not a magical money-printing machine. Any future strategy deployed on this system must demonstrate edge through rigorous out-of-sample validation and walk-forward analysis.

## Future Feature Justification
Every future feature must justify its added complexity. If a feature does not directly improve risk management, operational resilience, or demonstrably enhance statistical edge, it should be rejected.
