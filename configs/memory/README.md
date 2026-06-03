
# Memory Contracts

CMS-RCC-N-v0.3b5

Purpose: Memory promotion contracts for deciding which repository-bound feedback items may become durable memory, which must downgrade, and which must remain observe-only.

Validation:

```powershell
python scripts/memory/emit_memory_promotion_v0_3b5.py
python scripts/validation/validate_memory_promotion_v0_3b5.py
```

Mini README update rule: if this folder purpose, validation command, evidence surface, or public interpretation changes, update this README in the same commit.

Non-claim lock: memory promotion contracts are repository-bound and do not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.
