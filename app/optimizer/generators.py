import itertools
import random
import hashlib
import json
from typing import List, Dict, Any, Union
from app.optimizer.base import BaseGenerator
from app.optimizer.models import SearchSpace, ParameterCandidate
from app.optimizer.search_space import SearchSpaceEvaluator
from app.optimizer.enums import SearchMode


class DeterministicGenerator(BaseGenerator):
    def __init__(self, mode: SearchMode, seed: int = 42):
        self.mode = mode
        self.seed = seed

    def _hash_values(self, values: Dict[str, Any]) -> str:
        s = json.dumps(values, sort_keys=True)
        return hashlib.md5(s.encode("utf-8")).hexdigest()[:12]

    def generate(
        self, space: SearchSpace, max_candidates: int
    ) -> List[ParameterCandidate]:
        SearchSpaceEvaluator.validate_space(space)

        param_names = [p.name for p in space.parameters]
        expanded_values = [
            SearchSpaceEvaluator.expand_parameter(p) for p in space.parameters
        ]

        candidates: List[ParameterCandidate] = []
        seen_hashes = set()

        if (
            self.mode == SearchMode.GRID
            or self.mode == SearchMode.BOUNDED_COMBINATIONAL
        ):
            for combo in itertools.product(*expanded_values):
                val_dict = dict(zip(param_names, combo))

                if not SearchSpaceEvaluator.is_valid_combination(
                    val_dict, space.constraints
                ):
                    continue

                cand_id = self._hash_values(val_dict)
                if cand_id not in seen_hashes:
                    candidates.append(
                        ParameterCandidate(candidate_id=cand_id, values=val_dict)
                    )
                    seen_hashes.add(cand_id)

                if len(candidates) >= max_candidates:
                    break

        elif self.mode == SearchMode.RANDOM_SEEDED:
            rng = random.Random(self.seed)
            max_attempts = max_candidates * 100
            attempts = 0

            while len(candidates) < max_candidates and attempts < max_attempts:
                attempts += 1
                val_dict = {}
                for i, name in enumerate(param_names):
                    val_dict[name] = rng.choice(expanded_values[i])

                if not SearchSpaceEvaluator.is_valid_combination(
                    val_dict, space.constraints
                ):
                    continue

                cand_id = self._hash_values(val_dict)
                if cand_id not in seen_hashes:
                    candidates.append(
                        ParameterCandidate(candidate_id=cand_id, values=val_dict)
                    )
                    seen_hashes.add(cand_id)

        return candidates
