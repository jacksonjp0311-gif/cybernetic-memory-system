
# Control Runtime

CMS-RCC-N-v0.3b5

Purpose: Runtime control harness for false-promote rejection, downgrade preservation, and observe-only preservation.

Validation:

```powershell
python scripts/controls/emit_negative_control_harness_v0_3b4.py
python scripts/validation/validate_negative_control_harness_v0_3b4.py
```

Mini README update rule: if this folder purpose, validation command, evidence surface, or public interpretation changes, update this README in the same commit.

Non-claim lock: control harness surfaces are repository-bound and do not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.
