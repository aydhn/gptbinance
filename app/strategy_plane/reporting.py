from typing import List
from app.strategy_plane.repository import StrategyPlaneRepository
from app.strategy_plane.models import StrategyDefinition


class StrategyReporting:
    def __init__(self, repository: StrategyPlaneRepository):
        self.repository = repository

    def show_strategy_registry(self) -> str:
        out = ["=== Canonical Strategy Registry ==="]
        for strategy_id, definition in self.repository.storage.definitions.items():
            out.append(
                f"- {strategy_id} | Class: {definition.strategy_class.name} | Family: {definition.family.name} | Prod: {definition.is_production_grade}"
            )
        return "\n".join(out)

    def show_strategy(self, strategy_id: str) -> str:
        definition = self.repository.get_definition(strategy_id)
        if not definition:
            return f"Strategy {strategy_id} not found."

        manifest = self.repository.storage.manifests.get(strategy_id)
        trust = manifest.trust_verdict.name if manifest else "UNKNOWN"
        state = manifest.lifecycle_state.name if manifest else "UNKNOWN"

        out = [
            f"=== Strategy: {strategy_id} ===",
            f"Class: {definition.strategy_class.name}",
            f"Family: {definition.family.name}",
            f"Hypothesis Ref: {definition.hypothesis_ref}",
            f"Thesis Ref: {definition.thesis_ref}",
            f"Lifecycle State: {state}",
            f"Trust Verdict: {trust}",
            "Dependencies:",
            f"  Data: {definition.dependencies.data_manifests}",
            f"  Features: {definition.dependencies.feature_manifests}",
            f"  Models: {definition.dependencies.model_manis}",
        ]
        return "\n".join(out)

    def show_strategy_hypotheses(self) -> str:
        out = ["=== Strategy Hypotheses ==="]
        for hypothesis_id, hypothesis in self.repository.storage.hypotheses.items():
            out.append(
                f"- {hypothesis_id} | Claim: {hypothesis.behavioral_claim} | Regimes: {hypothesis.expected_regimes}"
            )
        return "\n".join(out)

    def show_strategy_theses(self) -> str:
        out = ["=== Strategy Theses ==="]
        for thesis_id, thesis in self.repository.storage.theses.items():
            out.append(
                f"- {thesis_id} v{thesis.version} | Claim: {thesis.concrete_claim} | Hold Time: {thesis.expected_hold_time}"
            )
        return "\n".join(out)

    def show_strategy_lifecycle(self) -> str:
        out = ["=== Strategy Lifecycle ==="]
        for strategy_id, records in self.repository.storage.lifecycle_records.items():
            current_state = records[-1].state.name if records else "UNKNOWN"
            out.append(
                f"- {strategy_id} | Current State: {current_state} | Transitions: {len(records)}"
            )
        return "\n".join(out)

    def show_strategy_promotions(self) -> str:
        return "=== Strategy Promotions ===\n[Reporting not fully implemented in this phase]"

    def show_strategy_freezes(self) -> str:
        return (
            "=== Strategy Freezes ===\n[Reporting not fully implemented in this phase]"
        )

    def show_strategy_retirements(self) -> str:
        return "=== Strategy Retirements ===\n[Reporting not fully implemented in this phase]"

    def show_strategy_fit(self) -> str:
        return "=== Strategy Fit ===\n[Reporting not fully implemented in this phase]"

    def show_strategy_overlap(self) -> str:
        return (
            "=== Strategy Overlap ===\n[Reporting not fully implemented in this phase]"
        )

    def show_strategy_decay(self) -> str:
        return "=== Strategy Decay ===\n[Reporting not fully implemented in this phase]"

    def show_strategy_equivalence(self) -> str:
        return "=== Strategy Equivalence ===\n[Reporting not fully implemented in this phase]"

    def show_strategy_trust(self) -> str:
        out = ["=== Strategy Trust ==="]
        for strategy_id, trust in self.repository.storage.trust_verdicts.items():
            out.append(
                f"- {strategy_id} | Verdict: {trust.verdict.name} | Factors: {trust.factors}"
            )
        return "\n".join(out)

    def show_strategy_review_packs(self) -> str:
        return "=== Strategy Review Packs ===\n[Reporting not fully implemented in this phase]"
