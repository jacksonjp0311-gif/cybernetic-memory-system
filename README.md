# Cybernetic Memory System - Feedback-Governed Repository Memory Runtime

![CMS-SA](https://img.shields.io/badge/CMS--SA-v0.1.2-blue)
![RCC-N](https://img.shields.io/badge/RCC--N-scaffolded-purple)
![Architecture](https://img.shields.io/badge/architecture-anchored-brightgreen)
![Lineage](https://img.shields.io/badge/lineage-recorded-brightgreen)
![README Audit](https://img.shields.io/badge/README%20audit-local--ready-yellow)
![Non-Claim](https://img.shields.io/badge/non--claim--locks-active-black)

Repository: `cybernetic-memory-system`  
Package / CLI: `cms`  
Current checkpoint: **CMS-SA v0.1.2 - RCC-N README and Mini README Enhancement**  
Previous seal: **CMS-SA v0.1.1 - Lineage / Injection Recorder Patch**

Cybernetic Memory System is a local-first Python/RCC runtime scaffold for executable repository memory. It observes repository state, measures drift, emits lifecycle-tracked feedback, plans next versions, validates corrections, promotes only control-useful memory, audits README/RCC/public surfaces, and emits release/evidence packages.

Core law:

- No metric contract, no improvement claim.
- No lifecycle, no feedback control.
- No validation, no release.
- No control utility, no memory promotion.
- No surface alignment, no release.
- No version without a document.
- No injection without a record.

## Current CMS Snapshot

| Layer | What it answers | Primary output |
|---|---|---|
| v0.1 Architecture Scaffold | What is the CMS software architecture? | `docs/architecture/cms_sa_v0_1_software_architecture.tex` |
| v0.1 Runtime Scaffold | What minimal package/CLI surfaces exist? | `src/cms/`, `pyproject.toml` |
| v0.1 RCC Genesis | Where does an agent route itself? | `rcc/nexus/route_map.json` |
| v0.1.1 Lineage Recorder | Where are versions and injections recorded? | `outputs/version_registry/cms_version_registry.json` |
| v0.1.1 Release Seal | What was sealed and what remains bounded? | `docs/release_seals/cms_sa_v0_1_1_release_seal.md` |
| v0.1.2 RCC-N README Enhancement | Are root and mini README surfaces navigable? | `reports/readme/latest_readme_mini_repo_audit.md` |
| v0.1.2 Context Indexes | What is the repo context and route map? | `docs/context/repository_context_index.json`, `docs/context/rcc_nexus_index.json` |

Current public finding: CMS can be structured as a feedback-governed repository-memory system. The current repo is an architecture scaffold plus RCC-N navigation layer, not a mature runtime.

| Surface | Current result |
|---|---:|
| Current checkpoint | CMS-SA v0.1.2 |
| Previous seal | CMS-SA v0.1.1 |
| Runtime package | scaffolded |
| RCC-N mini README coverage | target 1.0 |
| Version registry | active |
| Injection ledger | active |
| Release seal discipline | active |
| Claim status | architecture + local scaffold only |

Interpretation: CMS is becoming a self-traceable repository control surface. It does not prove intelligence, consciousness, correctness, production safety, external validation, or truth.

## Human Director Box

### What this repository is

This repo is a governed cybernetic-memory workbench:

```text
repo state -> observation -> metric contracts -> drift report -> feedback lifecycle
-> next-version plan -> validation -> control-utility memory promotion
-> correction records -> surface alignment -> release seal -> evidence package
```

### What this repository is not

This repo does **not** prove AGI, consciousness, sentience, autonomous self-modification, empirical truth, production safety, code correctness, provenance, or real-world validation.

## Current Public Metrics

| Surface | Result |
|---|---:|
| Current checkpoint | CMS-SA v0.1.2 |
| Version registry | `outputs/version_registry/cms_version_registry.json` |
| Lineage ledger | `outputs/lineage/cms_lineage_ledger.jsonl` |
| Injection ledger | `outputs/injections/cms_injection_ledger.jsonl` |
| Roadmap | `docs/roadmap/CMS_ROADMAP.md` |
| Root architecture | `docs/architecture/cms_sa_v0_1_software_architecture.tex` |
| RCC route map | `rcc/nexus/route_map.json` |
| RCC Nexus index | `docs/context/rcc_nexus_index.json` |
| Repository context index | `docs/context/repository_context_index.json` |
| README audit report | `reports/readme/latest_readme_mini_repo_audit.md` |
| RCC-N report | `reports/rcc_nexus/latest_rcc_nexus_check.md` |
| Architecture validation | `reports/architecture/latest_architecture_contract_validation.md` |
| Release readiness | `reports/release/latest_release_readiness.md` |

## Quick Start

```powershell
cd "$env:USERPROFILE\OneDrive\Desktop\cybernetic-memory-system"
$env:PYTHONPATH = ".\src"

python -m cms cycle --repo . --profile CMS-Core
python scripts\rcc\check_rcc_nexus.py
python scripts\rcc\audit_readme_surface.py
python scripts\validation\validate_architecture_contracts.py
python scripts\validate_release.py
python -m unittest discover -s tests
```

## Repository Layers

| Layer | Purpose | Main paths |
|---|---|---|
| CMS runtime scaffold | Minimal Python package and CLI surfaces | `src/cms/`, `tests/`, `configs/` |
| CMS architecture | Canonical CMS-SA document and protocols | `docs/architecture/`, `docs/protocols/` |
| RCC-N navigation | Makes the repo self-locating for humans and AI agents | `rcc/nexus/`, `docs/context/`, folder `README.md` files |
| Version memory | Records version documents, injections, seals, next anchors | `docs/versions/`, `docs/injections/`, `docs/release_seals/` |
| Evidence observability | Stores state, metrics, drift, feedback, validation, evidence | `outputs/` |
| Reports | Human-readable validation, RCC, README, architecture surfaces | `reports/` |
| Scripts | Local validators and patch helpers | `scripts/` |

## Historical Report Archive

| Archive surface | Use |
|---|---|
| `docs/versions/` | Canonical version documents |
| `docs/injections/` | Version injection records |
| `docs/release_seals/` | Release boundary seals |
| `docs/roadmap/CMS_ROADMAP.md` | Current and next anchors |
| `outputs/version_registry/cms_version_registry.json` | Machine-readable version registry |
| `outputs/lineage/cms_lineage_ledger.jsonl` | Append-only lineage ledger |
| `outputs/injections/cms_injection_ledger.jsonl` | Append-only injection ledger |
| `reports/readme/latest_readme_mini_repo_audit.md` | Current README/mini README audit |
| `reports/rcc_nexus/latest_rcc_nexus_check.md` | Current RCC-N navigation check |
| `reports/architecture/latest_architecture_contract_validation.md` | Current architecture contract validation |
| `reports/release/latest_release_readiness.md` | Current release readiness report |

Historical detail should live in archive reports, version docs, injections, and mini READMEs, not only in the root README body.

## PART I - Human README

### What CMS Tests

| Seed / surface | Purpose |
|---|---|
| `cms_lite_self_audit_seed.json` | Tests minimal CMS governance surfaces. |
| `readme_rcc_drift_seed.json` | Tests README/RCC surface drift. |
| `feedback_lifecycle_seed.json` | Tests feedback lifecycle closure. |
| `memory_promotion_seed.json` | Tests control-utility memory promotion. |
| `baseline_utility_seed.json` | Tests CMS against a baseline workflow. |
| `public_surface_drift_seed.json` | Tests local/public surface mismatch. |

CMS rewards bounded evidence emission, not confident overclaiming.

## PART II - RCC Nexus README

### RCC Nexus Identity

RCC tells the agent what the repository means.  
RCC-N tells the agent where it is.  
Validation tells the agent whether the local repository agreed.

### Repository Sphere

| Shell | Meaning |
|---|---|
| center | Source boundary, non-claim locks, architecture, context indexes. |
| inner | Runtime primitives: state, metric contracts, drift reports, feedback items. |
| middle | Processes: CLI flow, examples, tests, scripts, validation workflows. |
| outer | Evidence / reflection: outputs, ledgers, reports, visuals, release notes. |

### Nexus Meridians

`source`, `validation`, `evidence`, `drift`, `agent`, `safety`, `runtime`, `memory`, `release`, `documentation`

### Nexus Sectors

`core`, `schemas`, `runtime`, `validation`, `evidence`, `rcc`, `agent`, `examples`, `release`, `memory`

### Primary Nexus Files

| File | Role |
|---|---|
| `docs/context/repository_context_index.json` | Repository meaning map. |
| `docs/context/rcc_nexus_index.json` | Nexus route and coverage index. |
| `docs/context/validation_surface.md` | Validation commands and claim boundaries. |
| `rcc/nexus/README.md` | RCC-N local orientation. |
| `rcc/nexus/route_map.json` | Machine-readable routing map. |
| `rcc/nexus/task_routing_matrix.md` | Task-to-validation routing. |
| `rcc/nexus/echo_location_template.md` | Mini README Echo Location template. |
| `rcc/nexus/agent_handoff_contract.md` | Agent handoff rules. |
| `scripts/rcc/check_rcc_nexus.py` | RCC-N checker. |
| `scripts/rcc/audit_readme_surface.py` | README / mini repo audit scanner. |
| `scripts/validation/validate_architecture_contracts.py` | Architecture validator. |
| `scripts/validate_release.py` | Release-readiness validator. |

### RCC-N Status

The Nexus is working when the following command passes:

```powershell
python scripts/rcc/check_rcc_nexus.py
```

RCC-N checks repository navigation and context integrity. It does not prove code correctness, patch safety, empirical validation, AI understanding, or production readiness.

## PART III - AI Agent README

### AI Operating Contract

Before editing, an AI agent must read:

1. `README.md`
2. `README_90_SECONDS.md`
3. `AGENTS.md`
4. `docs/context/repository_context_index.json`
5. `docs/context/rcc_nexus_index.json`
6. `rcc/nexus/route_map.json`
7. the target folder `README.md`
8. relevant source and tests

After editing, run the validation command associated with the changed surface.

### Patch Routing Matrix

| Change type | Read first | Validate |
|---|---|---|
| Runtime patch | `src/cms/README.md`, `src/cms/core/README.md`, `tests/` | compile + import + unit tests |
| Metric contract patch | `src/cms/metrics/README.md`, latest evidence | architecture validator + tests |
| Feedback lifecycle patch | `src/cms/feedback/README.md`, outputs/feedback | runtime cycle + tests |
| Memory promotion patch | `src/cms/memory/README.md`, outputs/memory | memory promotion tests |
| RCC docs patch | `README.md`, `docs/context/`, `rcc/nexus/` | `python scripts/rcc/check_rcc_nexus.py` |
| README / mini README patch | `README.md`, target mini README, route maps | `python scripts/rcc/audit_readme_surface.py` |
| Architecture docs patch | `docs/architecture/`, `docs/protocols/` | `python scripts/validation/validate_architecture_contracts.py` |
| Directory structure patch | root README directory box, affected mini READMEs, context indexes | RCC-N + README audit + architecture + tests |
| Release patch | `docs/release_seals/`, `reports/release/`, `outputs/release/` | release validator |

## README + Mini Repo Audit Map

The repository is considered healthy only when its public surfaces, folder-level mini READMEs, route maps, validation reports, runtime checks, and evidence packages agree.

A patch is incomplete if it changes code, folders, reports, release state, or documentation meaning without updating the matching README and mini README surfaces.

### Required Gap Scan Order

| Scan step | Surface | What to check |
|---:|---|---|
| 1 | `README.md` | Current checkpoint, metrics, lineage, validation commands, non-claim locks, directory box, and AI rules. |
| 2 | `AGENTS.md` | Agent entry order, patch discipline, and validation expectations. |
| 3 | `README_90_SECONDS.md` | Compressed onboarding is not stale. |
| 4 | `docs/context/repository_context_index.json` | Repo meaning and route descriptions. |
| 5 | `docs/context/rcc_nexus_index.json` | Nexus shell/meridian/sector mapping. |
| 6 | `rcc/nexus/route_map.json` | Task routing and target surfaces. |
| 7 | `rcc/nexus/task_routing_matrix.md` | Human-readable task routing. |
| 8 | Target folder `README.md` | Local folder role, inputs, outputs, and validation command. |
| 9 | Sibling mini READMEs | Adjacent surfaces if routing or folder meaning changed. |
| 10 | Latest reports | `reports/rcc_nexus/`, `reports/architecture/`, `reports/readme/`, and `reports/release/`. |

### Gap Classes the AI Must Detect

| Gap class | Detection question | Required repair |
|---|---|---|
| README drift | Does the root README describe the current repo state? | Patch checkpoint, metrics, lineage, commands, and directory box. |
| Mini README drift | Did a folder change without its README changing? | Patch the affected folder README. |
| Route drift | Did task routing or folder purpose change? | Patch context indexes and route maps. |
| Validation drift | Do public claims lack fresh validation reports? | Rerun validation and refresh reports. |
| Runtime drift | Did Python code change without compile/import/test proof? | Run compile, import, tests, and CLI cycle. |
| Evidence drift | Could one run overwrite another? | Verify run IDs and latest evidence package. |
| Claim drift | Does language imply stronger proof than evidence allows? | Restore downgrade wording and non-claim locks. |
| Encoding drift | Do headings, arrows, paths, or code fences show mojibake? | Rewrite affected README surfaces using UTF-8 and ASCII-safe syntax unless Unicode is required by an audit anchor. |

### Executable README / Mini Repo Audit

Run:

```powershell
python scripts/rcc/audit_readme_surface.py
```

Expected pass:

```text
passed: true
errors: 0
warnings: 0
```

Primary outputs:

```text
reports/readme/latest_readme_mini_repo_audit.json
reports/readme/latest_readme_mini_repo_audit.md
```

## AI Failure Learning Ledger

| Lesson ID | Failure observed | Root cause | Permanent rule |
|---|---|---|---|
| CMS-L-001 | PowerShell `#requires` failed when pasted line-by-line. | `#requires` belongs in a `.ps1` file. | Large scripts must be run with `powershell -ExecutionPolicy Bypass -File script.ps1`. |
| CMS-L-002 | Version changed without durable version memory risk. | No mandatory document/injection record. | Every version gets document, injection, ledger, seal, and next-anchor. |
| CMS-L-003 | Mini README surfaces were too generic. | Folder-local RCC contract missing. | Every major folder needs S/H/A/T/I/E and Echo Location. |
| CMS-L-004 | README/RCC drift can occur even when scripts run. | Narrative surfaces lag behind generated outputs. | README/RCC/public surfaces must update with versioned state. |

Non-claim lock: README audits and mini repo audits improve context alignment. They do not prove runtime correctness, production readiness, AGI, consciousness, or empirical truth.

### Required Validation

```powershell
$env:PYTHONPATH = ".\src"
python -m py_compile src/cms/core/runtime.py
python -c "from cms.core.runtime import CMSRuntime; print('CMSRuntime import OK')"
python scripts/rcc/check_rcc_nexus.py
python scripts/rcc/audit_readme_surface.py
python scripts/validation/validate_architecture_contracts.py
python scripts/validate_release.py
python -m unittest discover -s tests
```

<!-- MINI_README_UPDATE_RULE_START -->
## AI Update Rule - Mini README and Directory Box Synchronization

This repository is part of the RCC-N navigable repository surface.

When any folder purpose, files, routes, evidence surfaces, validation commands, or claim boundaries change, update the matching mini README in the same commit. Also update this root README if any folder is added, removed, renamed, or repurposed.

Non-claim lock: navigation is not validation, but stale navigation is repository drift.
<!-- MINI_README_UPDATE_RULE_END -->