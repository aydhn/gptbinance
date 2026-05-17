from app.environment_plane.models import EnvironmentObject

def generate_environment_summary(env: EnvironmentObject) -> str:
    lines = [
        f"Environment ID: {env.environment_id}",
        f"Class: {env.record.environment_class.name}",
        f"Owner: {env.record.owner}",
        f"Description: {env.record.description}",
        f"Topology: {env.topology.topology_class.name if env.topology else 'None'}",
        f"Parity: {env.parity.parity_class.name if env.parity else 'None'}",
        f"Trust Verdict: {env.trust_verdict.verdict.name if env.trust_verdict else 'None'}"
    ]
    return "\n".join(lines)
