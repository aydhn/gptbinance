import os

# Update app/readiness_board/domains.py
readiness_domains_path = 'app/readiness_board/domains.py'
if os.path.exists(readiness_domains_path):
    with open(readiness_domains_path, 'r') as f:
        content = f.read()
    if 'EXPERIMENT_INTEGRITY' not in content:
        content = content.replace(
            'class ReadinessDomain(str, Enum):',
            'class ReadinessDomain(str, Enum):\n    EXPERIMENT_INTEGRITY = "EXPERIMENT_INTEGRITY"'
        )
        with open(readiness_domains_path, 'w') as f:
            f.write(content)

# Update app/reliability/domains.py
reliability_domains_path = 'app/reliability/domains.py'
if os.path.exists(reliability_domains_path):
    with open(reliability_domains_path, 'r') as f:
        content = f.read()
    if 'EXPERIMENT_INTEGRITY' not in content:
        content = content.replace(
            'class ReliabilityDomain(str, Enum):',
            'class ReliabilityDomain(str, Enum):\n    EXPERIMENT_INTEGRITY = "EXPERIMENT_INTEGRITY"'
        )
        with open(reliability_domains_path, 'w') as f:
            f.write(content)

# Update app/evidence_graph/artefacts.py
evidence_artefacts_path = 'app/evidence_graph/artefacts.py'
if os.path.exists(evidence_artefacts_path):
    with open(evidence_artefacts_path, 'r') as f:
        content = f.read()
    if 'EXPERIMENT_MANIFEST' not in content:
        content = content.replace(
            'class ArtefactFamily(str, Enum):',
            'class ArtefactFamily(str, Enum):\n    EXPERIMENT_MANIFEST = "EXPERIMENT_MANIFEST"\n    FAIRNESS_REPORT = "FAIRNESS_REPORT"\n    TRUST_VERDICT = "TRUST_VERDICT"'
        )
        content = content.replace(
            'class ArtefactRelation(str, Enum):',
            'class ArtefactRelation(str, Enum):\n    EXPERIMENTED_UNDER = "EXPERIMENTED_UNDER"\n    COMPARED_AGAINST = "COMPARED_AGAINST"\n    CONTROLLED_BY = "CONTROLLED_BY"'
        )
        with open(evidence_artefacts_path, 'w') as f:
            f.write(content)

# Update app/reviews/requests.py
reviews_requests_path = 'app/reviews/requests.py'
if os.path.exists(reviews_requests_path):
    with open(reviews_requests_path, 'r') as f:
        content = f.read()
    if 'EXPERIMENT_INTEGRITY_REVIEW' not in content:
        content = content.replace(
            'class ReviewClass(str, Enum):',
            'class ReviewClass(str, Enum):\n    EXPERIMENT_INTEGRITY_REVIEW = "EXPERIMENT_INTEGRITY_REVIEW"\n    FAIRNESS_REVIEW = "FAIRNESS_REVIEW"\n    BASELINE_CONTROL_REVIEW = "BASELINE_CONTROL_REVIEW"\n    STOPPING_RULE_REVIEW = "STOPPING_RULE_REVIEW"\n    EXPERIMENT_EQUIVALENCE_REVIEW = "EXPERIMENT_EQUIVALENCE_REVIEW"\n    PROMOTION_RECOMMENDATION_REVIEW = "PROMOTION_RECOMMENDATION_REVIEW"'
        )
        with open(reviews_requests_path, 'w') as f:
            f.write(content)

# Update app/identity/capabilities.py
identity_caps_path = 'app/identity/capabilities.py'
if os.path.exists(identity_caps_path):
    with open(identity_caps_path, 'r') as f:
        content = f.read()
    if 'INSPECT_EXPERIMENT_MANIFEST' not in content:
        content = content.replace(
            'class Capability(str, Enum):',
            'class Capability(str, Enum):\n    INSPECT_EXPERIMENT_MANIFEST = "INSPECT_EXPERIMENT_MANIFEST"\n    REVIEW_EXPERIMENT_FAIRNESS = "REVIEW_EXPERIMENT_FAIRNESS"\n    REVIEW_BASELINE_CONTROL_INTEGRITY = "REVIEW_BASELINE_CONTROL_INTEGRITY"\n    REVIEW_STOPPING_RULES = "REVIEW_STOPPING_RULES"\n    REVIEW_EXPERIMENT_RECOMMENDATION = "REVIEW_EXPERIMENT_RECOMMENDATION"'
        )
        with open(identity_caps_path, 'w') as f:
            f.write(content)
