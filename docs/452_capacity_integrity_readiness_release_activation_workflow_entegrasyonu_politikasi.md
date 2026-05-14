# Capacity Integrity: Readiness, Release, Activation, and Workflow Integration Policy

The Capacity Plane does not exist in a vacuum. It provides evidence and guards for other planes.

## Integrations
* **Workflow Plane**: Critical workflows check capacity gates. If the required queue lanes are saturated, the workflow cannot start.
* **Release Plane**: Rollouts require headroom. A canary release cannot proceed if the live environment is already at 95% saturation.
* **Activation**: Moving from Paper to Live requires a clean capacity trust verdict. If live isolation is breached, activation is blocked.
* **Reliability Plane**: Chronic saturation or repeated emergency shedding feeds directly into Reliability SLOs and readiness.
* **Evidence Graph**: All capacity reports (saturation, shedding, fairness) are exported as artifacts to the Evidence Graph for postmortem and readiness board reviews.
