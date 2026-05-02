import re

with open('app/observability/slo.py', 'r') as f:
    content = f.read()

# Fix SLO status evaluation logic to support different inequality directions
patch = """    def _evaluate_related_slos(self, sli_id: str, current_sli_value: float) -> None:
        for slo in self._slos.values():
            if slo.sli_id == sli_id:
                status = SloStatus.HEALTHY
                explanation = "SLO is healthy."

                # Check if lower is better (e.g. lag) or higher is better (e.g. success rate)
                if slo.breach_threshold > slo.warning_threshold:
                    # Lower is better (e.g. lag)
                    if current_sli_value > slo.breach_threshold:
                        status = SloStatus.BREACH
                        explanation = f"SLI value {current_sli_value} above breach threshold {slo.breach_threshold}"
                    elif current_sli_value > slo.warning_threshold:
                        status = SloStatus.CAUTION
                        explanation = f"SLI value {current_sli_value} above warning threshold {slo.warning_threshold}"
                else:
                    # Higher is better (e.g. success rate)
                    if current_sli_value < slo.breach_threshold:
                        status = SloStatus.BREACH
                        explanation = f"SLI value {current_sli_value} below breach threshold {slo.breach_threshold}"
                    elif current_sli_value < slo.warning_threshold:
                        status = SloStatus.CAUTION
                        explanation = f"SLI value {current_sli_value} below warning threshold {slo.warning_threshold}"
"""

content = re.sub(
    r"    def _evaluate_related_slos\(self, sli_id: str, current_sli_value: float\) -> None:\n        for slo in self._slos.values\(\):\n            if slo.sli_id == sli_id:\n                status = SloStatus.HEALTHY\n                explanation = \"SLO is healthy.\"\n                \n                # Assuming higher is better \(e\.g\. success rate\)\n                if current_sli_value < slo.breach_threshold:\n                    status = SloStatus.BREACH\n                    explanation = f\"SLI value \{current_sli_value\} below breach threshold \{slo.breach_threshold\}\"\n                elif current_sli_value < slo.warning_threshold:\n                    status = SloStatus.CAUTION\n                    explanation = f\"SLI value \{current_sli_value\} below warning threshold \{slo.warning_threshold\}\"",
    patch,
    content
)

with open('app/observability/slo.py', 'w') as f:
    f.write(content)
