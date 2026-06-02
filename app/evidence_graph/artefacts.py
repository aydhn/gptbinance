def create_assurance_artefact(assurance_record) -> dict:
    return {
        "artefact_type": "assurance_record",
        "id": assurance_record.assurance_obj.assurance_id,
        "relations": ["assured_by", "evidenced_by", "certified_under", "attested_by", "surveilled_by", "downgraded_by", "diverged_assurance_from"]
    }

ACCOUNTABILITY_ARTEFACTS = ['AccountabilityObject', 'DutyRecord', 'BreachRecord']
ACCOUNTABILITY_RELATIONS = ['accountable_for', 'breached_by', 'sanctioned_by', 'remediated_by', 'appealed_by', 'reinstated_by', 'diverged_accountability_from']


# Incentive Plane Evidence Artefacts
INCENTIVE_ARTEFACT_FAMILIES = [
    "incentives", "subjects", "targets", "levers",
    "rewards", "reward_formulas", "delayed_rewards",
    "penalties", "penalty_triggers", "frictions", "clawbacks",
    "escalation", "surveillance", "shared", "conflicts",
    "moral_hazard", "externalities", "gaming", "reviews",
    "recalibration", "comparisons", "equivalence", "trust_reports"
]

INCENTIVE_RELATIONS = [
    "incentivized_by",
    "rewarded_under",
    "penalized_under",
    "clawed_back_by",
    "conflicted_by",
    "gamed_under",
    "diverged_incentive_from"
]
