with open("app/evidence_graph/dependencies.py", "r") as f:
    content = f.read()

# Fix dependency forward issue as well
# For dependency fanout (forward), we want things that depend on the current node.
# If A -> DEPENDS_ON -> B, A depends on B. B's dependents is A.
# So we want edges where current_id is the TARGET.

content = content.replace(
"""            edges = self.relation_registry.get_relations_for_source(curr)
            for edge in edges:
                target_node = self.artefact_registry.get_artefact(edge.target_id)""",
"""            edges = self.relation_registry.get_relations_for_target(curr)
            for edge in edges:
                target_node = self.artefact_registry.get_artefact(edge.source_id)"""
)

with open("app/evidence_graph/dependencies.py", "w") as f:
    f.write(content)
