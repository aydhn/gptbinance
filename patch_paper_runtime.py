import re

with open('tests/test_paper_runtime.py', 'r') as f:
    content = f.read()

patch = content.replace('PaperRuntimeOrchestrator(\n            run_id="test_run",\n            config=base_config,\n            notifier_bridge=mock_notifier,\n            storage=mock_storage,\n        )', 'PaperRuntimeOrchestrator()')

with open('tests/test_paper_runtime.py', 'w') as f:
    f.write(patch)
