#!/bin/bash
git config --global user.email "jules@example.com"
git config --global user.name "Jules"
git add app/immunity_plane/ tests/test_immunity_plane_*.py docs/67*_*.md app/main.py FINAL_OUTPUT.md
for f in $(git diff --name-only HEAD | grep -v "app/immunity_plane" | grep -v "tests/test_immunity_plane"); do git add $f; done
git commit --allow-empty -m "feat(immunity_plane): Implement Canonical Immunity Registry and Recurrence-Prevention Governance (Phase 133)"
