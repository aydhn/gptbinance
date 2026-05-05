from app.policy_kernel.enums import PolicyDomain

DOMAIN_GROUPS = {
    PolicyDomain.RISK: "risk_group",
    PolicyDomain.CAPITAL: "capital_group",
    PolicyDomain.EVENT_RISK: "event_group",
    PolicyDomain.STRESS_RISK: "stress_group",
    PolicyDomain.CROSS_BOOK: "cross_book_group",
    PolicyDomain.WORKSPACE: "workspace_group",
    PolicyDomain.CONTROL: "control_group",
    PolicyDomain.LIFECYCLE: "lifecycle_group",
    PolicyDomain.SHADOW: "shadow_group",
    PolicyDomain.QUALIFICATION: "qualification_group",
    PolicyDomain.REMEDIATION: "remediation_group",
    PolicyDomain.ORDER_INTENT: "order_intent_group",
    PolicyDomain.GENERAL: "general_group",
}


def get_domain_group(domain: PolicyDomain) -> str:
    return DOMAIN_GROUPS.get(domain, "unknown_group")


def generate_domain_health_summary(domain_results: dict) -> dict:
    # A simple summary of health per domain based on evaluation outputs
    summary = {}
    for domain, result in domain_results.items():
        summary[domain.name] = {
            "status": "HEALTHY" if result.get("verdict") == "ALLOW" else "UNHEALTHY",
            "findings": result.get("findings", []),
        }
    return summary
