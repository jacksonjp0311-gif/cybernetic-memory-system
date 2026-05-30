# Cybernetic Memory System

![CMS-SA](https://img.shields.io/badge/CMS--SA-v0.1-blue)
![RCC-N](https://img.shields.io/badge/RCC--N-ready-purple)
![Status](https://img.shields.io/badge/status-architecture--anchored-brightgreen)
![Non-Claim](https://img.shields.io/badge/non--claim--locks-active-black)

Repository: `cybernetic-memory-system`  
Package / CLI: `cms`  
Current checkpoint: **CMS-SA v0.1 — Software Architecture Genesis Layer**

Cybernetic Memory System is a local-first Python/RCC architecture for repository memory that observes state, measures drift, emits lifecycle-tracked feedback, plans next versions, validates corrections, promotes only control-useful memory, audits README/RCC/public surfaces, and emits release/evidence packages.

Core law:

- No metric contract, no improvement claim.
- No lifecycle, no feedback control.
- No validation, no release.
- No control utility, no memory promotion.
- No surface alignment, no release.

## Current State

This repository is currently at the **architecture-anchored scaffold** stage.

| Surface | Current status |
|---|---|
| CMS-SA document | `docs/architecture/cms_sa_v0_1_software_architecture.tex` |
| Runtime package | `src/cms/` scaffolded |
| RCC Nexus | `rcc/nexus/` scaffolded |
| AI contract | `AGENTS.md` |
| State output | `outputs/state/latest_cms_state.json` |
| Release report | `outputs/release/latest_release_readiness.md` |
| Evidence package | `outputs/evidence/latest_evidence_package.json` |

## Human Director Box

### What this repository is

This repo is a governed cybernetic-memory workbench:

repository state -> observation -> metric contracts -> drift report -> feedback lifecycle -> next-version plan -> validation -> control-utility memory promotion -> correction records -> surface alignment -> release seal -> evidence package

### What this repository is not

This repo does **not** prove AGI, consciousness, sentience, autonomous self-modification, empirical truth, production safety, code correctness, provenance, or real-world validation.

## Quick Start

```powershell
cd "$env:USERPROFILE\OneDrive\Desktop\cybernetic-memory-system"
$env:PYTHONPATH = ".\src"
python -m cms cycle --repo . --profile CMS-Core
python scripts\validate_release.py
```

## PART I — Human README

CMS-SA v0.1 defines the architecture and local scaffold for executable cybernetic repository memory.

Primary architecture file:

```text
docs/architecture/cms_sa_v0_1_software_architecture.tex
```

## PART II — RCC Nexus README

RCC tells the agent what the repository means.  
RCC-N tells the agent where it is.  
CMS tells the agent what the repository learned from itself.

Primary route files:

```text
rcc/nexus/README.md
rcc/nexus/route_map.json
rcc/nexus/task_routing_matrix.md
docs/context/repository_context_index.json
```

## PART III — AI Agent README

Before editing, an AI agent must read:

1. `README.md`
2. `README_90_SECONDS.md`
3. `AGENTS.md`
4. `rcc/nexus/route_map.json`
5. target folder `README.md`
6. relevant source and tests

After editing, run the validation command associated with the changed surface.

## Required Validation

```powershell
$env:PYTHONPATH = ".\src"
python -m py_compile src/cms/core/runtime.py
python -c "from cms.core.runtime import CMSRuntime; print('CMSRuntime import OK')"
python scripts/validate_release.py
python -m unittest discover -s tests
```

## AI Failure Learning Ledger

| Lesson ID | Failure observed | Root cause | Permanent rule |
|---|---|---|---|
| CMS-L-001 | Feedback can become commentary. | Missing lifecycle state. | Every feedback item needs lifecycle and resolution target. |
| CMS-L-002 | README/RCC can lag behind state. | Generated artifacts advanced without narrative update. | Narrative-surface drift is repository drift. |
| CMS-L-003 | Local state can differ from public state. | Public surface not verified. | Public-surface drift is release drift. |
| CMS-L-004 | Memory can accumulate without control value. | No promotion score. | No control utility, no memory promotion. |

## Non-Claim Locks

- Feedback is not truth.
- Memory is not consciousness.
- Self-improvement is versioned artifact improvement.
- Validation is repository-bound unless external evidence is supplied.
- Surface alignment is not code correctness.
- Public-surface alignment is not empirical validation.
---

## CMS-SA v0.1.1 — Lineage / Injection Recorder Patch

Every CMS version must now be recorded as:

1. canonical document,
2. injection record,
3. version registry entry,
4. lineage ledger entry,
5. release seal,
6. roadmap next-anchor.

Primary registry:

```text
outputs/version_registry/cms_version_registry.json
```

Primary next anchor:

```text
docs/roadmap/CMS_ROADMAP.md
```

Non-claim lock:

```text
Version recording improves traceability. It does not prove correctness, truth, AGI, consciousness, or external validation.
```
