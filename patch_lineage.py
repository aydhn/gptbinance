with open("app/evidence_graph/lineage.py", "r") as f:
    content = f.read()

# Fix traversal direction issue
# When going BACKWARD, we look for relations where the target is the current node
# Wait, if A -> (FOLLOWS_INCIDENT) -> B, source=A, target=B
# A is postmortem, B is incident
# Backward from A should find B
# So we need edges where A is the SOURCE, and the edge points to an older/parent thing!
# E.g., POSTMORTEM (source) --FOLLOWS--> INCIDENT (target)
# Actually, if A depends on B, source=A, target=B.
# So traversing backward means following edges from A to B.

content = content.replace(
"""                if direction == TraversalClass.BACKWARD:
                    # Look for relations where current_id is the target (it depends on source)
                    edges = self.relation_registry.get_relations_for_target(current_id)
                    for edge in edges:
                        visited_edges.append(edge)
                        queue.append((edge.source_id, depth + 1))
                else: # FORWARD
                    # Look for relations where current_id is the source (it leads to target)
                    edges = self.relation_registry.get_relations_for_source(current_id)
                    for edge in edges:
                        visited_edges.append(edge)
                        queue.append((edge.target_id, depth + 1))""",
"""                if direction == TraversalClass.BACKWARD:
                    # Look for relations where current_id is the source (it depends on target)
                    edges = self.relation_registry.get_relations_for_source(current_id)
                    for edge in edges:
                        visited_edges.append(edge)
                        queue.append((edge.target_id, depth + 1))
                else: # FORWARD
                    # Look for relations where current_id is the target (it is depended on by source)
                    edges = self.relation_registry.get_relations_for_target(current_id)
                    for edge in edges:
                        visited_edges.append(edge)
                        queue.append((edge.source_id, depth + 1))"""
)
with open("app/evidence_graph/lineage.py", "w") as f:
    f.write(content)
