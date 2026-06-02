# Cybernetic Memory System - Feedback-Governed Repository Memory Runtime

![CMS-SA](https://img.shields.io/badge/CMS--SA-v0.2b2-blue)
![RCC-N](https://img.shields.io/badge/RCC--N-passing-brightgreen)
![Architecture](https://img.shields.io/badge/architecture-passing-brightgreen)
![Lineage](https://img.shields.io/badge/lineage-recorded-brightgreen)
![README Audit](https://img.shields.io/badge/README%20audit-passing-brightgreen)
![Directory Box](https://img.shields.io/badge/directory%20box-passing-brightgreen)
![Render Hygiene](https://img.shields.io/badge/render%20hygiene-passing-brightgreen)
![K_CMS](https://img.shields.io/badge/K__CMS-1.0-blue)
![D_CMS](https://img.shields.io/badge/D__CMS-0.0-blue)
![Non-Claim](https://img.shields.io/badge/non--claim--locks-active-black)

Repository: `cybernetic-memory-system`  
Package / CLI: `cms`  
Current checkpoint: **CMS-SA v0.2b2 - README Render Hygiene and Badge Status Guard**  
Previous seal: **CMS-SA v0.2b1 - Public Anchor and Directory Table Render Repair**

Cybernetic Memory System is a local-first Python/RCC runtime for executable repository memory. It observes repository state, measures drift, validates public surfaces, records version lineage, emits evidence packages, and keeps README/RCC/directory/status surfaces synchronized.

Core law:

- No metric contract, no improvement claim.
- No lifecycle, no feedback control.
- No validation, no release.
- No control utility, no memory promotion.
- No surface alignment, no release.
- No version without a document.
- No injection without a record.
- No clean render, no public release.
- No badge/status refresh, no checkpoint promotion.

## Current CMS Snapshot

| Layer | What it answers | Primary output |
|---|---|---|
| v0.1 Architecture Scaffold | What is the CMS software architecture? | `docs/architecture/cms_sa_v0_1_software_architecture.tex` |
| v0.1 Runtime Scaffold | What package/CLI surfaces exist? | `src/cms/`, `pyproject.toml` |
| v0.1.1 Lineage Recorder | Where are versions and injections recorded? | `outputs/version_registry/cms_version_registry.json` |
| v0.1.2 RCC-N README Enhancement | Are root and mini README surfaces navigable? | `reports/readme/latest_readme_mini_repo_audit.md` |
| v0.2 Runtime Observation and Metric Contracts | Does the runtime emit observation, metric, drift, and evidence artifacts? | `outputs/evidence/latest_evidence_package.json` |
| v0.2a README/Audit Anchor Sync | Does README audit grammar agree with runtime state? | `reports/readme/latest_readme_mini_repo_audit.md` |
| v0.2b Public Format / Directory Lock | Is the public directory contract present? | `docs/directory/cms_full_directory_box_v0_2b.json` |
| v0.2b1 Anchor/Table Repair | Are public anchors and directory rows inspectable? | `reports/directory/latest_directory_box_validation.md` |
| v0.2b2 Render Hygiene / Badge Guard | Are badges, status, and README rendering clean? | `reports/render_hygiene/latest_readme_render_hygiene.md` |

Current public finding: CMS can be structured as a feedback-governed repository-memory runtime. The current repo is a local evidence-governance and repository-observability system, not a proof of correctness, intelligence, consciousness, production safety, external validation, or truth.

## Human Director Box

### What this repository is

This repo is a local-first cybernetic repository-memory runtime:

    repository -> observation manifest -> metric contracts -> metric evaluation
    -> drift report -> evidence package -> validation report
    -> lineage / release surface -> README/RCC/status sync

CMS is designed to make repository state observable, measurable, auditable, and easier for humans and AI agents to maintain without relying on implicit memory.

### What this repository is not

This repo does **not** prove code correctness, security, truth, AGI, consciousness, production readiness, external validation, or real-world correctness. It is a repository-bound governance and measurement runtime.

## Current Public Metrics

| Surface | Result |
|---|---:|
| Current checkpoint | CMS-SA v0.2b2 |
| Previous seal | CMS-SA v0.2b1 |
| Git head before patch | `8793d17` |
| Metric evaluation before patch | `True` |
| README / mini repo audit before patch | `True` |
| RCC-N checker | `True` |
| Runtime observation validation | `True` |
| Directory box validation before patch | `True` |
| Directory rows before patch | `34` |
| CMS coherence K_CMS | `1.0` |
| CMS drift D_CMS | `0.0` |
| Evidence classification | `CMS-B` |
| Release allowed | `True` |
| Latest observation manifest | `outputs/state/latest_observation_manifest.json` |
| Latest metric evaluation | `outputs/metrics/latest_metric_evaluation.json` |
| Latest drift report | `outputs/drift/latest_drift_report.json` |
| Latest evidence package | `outputs/evidence/latest_evidence_package.json` |
| Directory box manifest | `docs/directory/cms_full_directory_box_v0_2b2.json` |
| Directory box validation | `reports/directory/latest_directory_box_validation.md` |
| Render hygiene validation | `reports/render_hygiene/latest_readme_render_hygiene.md` |

## Quick Start

Run the local validation stack:

    cd "$env:USERPROFILE\OneDrive\Desktop\cybernetic-memory-system"
    $env:PYTHONPATH = ".\src"

    python scripts/rcc/audit_readme_surface.py
    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python scripts/validation/validate_runtime_observation_v0_2.py
    python scripts/validation/validate_directory_box_v0_2b.py
    python scripts/validation/validate_readme_render_hygiene_v0_2b2.py
    python -m cms cycle --repo . --profile CMS-Core
    python -m unittest discover -s tests
    python scripts/validate_release.py

## PART I - Human README

### What CMS Does

CMS observes a repository, evaluates declared metric contracts, computes drift, writes evidence packages, validates public surfaces, and records version lineage.

### Primary Human Path

    README -> Human Director Box -> Current Public Metrics -> Full Directory Box -> Quick Start / Validation -> Reports

## PART II - RCC Nexus README

### RCC Nexus Identity

RCC tells the agent what the repository means. RCC-N tells the agent where it is. Validation tells the agent whether the repository-bound checks agreed.

### Repository Sphere

| Shell | Meaning |
|---|---|
| center | Source boundaries, non-claim locks, architecture, context indexes. |
| inner | Runtime primitives: observer, metric contracts, drift, evidence, schemas. |
| middle | CLI flow, scripts, validators, tests, task routing. |
| outer | Reports, ledgers, release seals, README/public surfaces. |

### Nexus Meridians

`source`, `validation`, `evidence`, `drift`, `agent`, `safety`, `runtime`, `release`, `documentation`

## PART III - AI Agent README

### AI Operating Contract

Before editing, an AI agent must read:

1. `README.md`
2. `README_90_SECONDS.md`
3. `AGENTS.md`
4. `docs/context/repository_context_index.json`
5. `docs/context/rcc_nexus_index.json`
6. `rcc/nexus/route_map.json`
7. `rcc/nexus/task_routing_matrix.md`
8. the target folder `README.md`
9. relevant source, tests, and validators

After editing, run the validation command associated with the changed surface.

### Patch Routing Matrix

| Change type | Read first | Validate |
|---|---|---|
| Runtime patch | `src/cms/README.md`, `src/cms/core/`, `tests/` | compile + runtime validation + unit tests |
| Metric patch | `configs/metrics/`, `src/cms/metrics/` | metric evaluation + CMS cycle + tests |
| Drift/evidence patch | `src/cms/comparator/`, `src/cms/evidence/` | CMS cycle + evidence report + tests |
| README / mini README patch | `README.md`, target mini README, route maps | README audit + render hygiene + RCC-N |
| Directory structure patch | root Full Directory Box, affected mini READMEs, context indexes | directory validator + README audit + RCC-N |
| Badge/status patch | `README.md`, latest reports, version registry | render hygiene + README audit + release validation |
| Release/docs patch | `docs/`, `reports/release/`, version registry | release validation + README audit |

## README + Mini Repo Audit Map

### Audit Purpose

The repository is considered healthy only when public surfaces, folder-level mini READMEs, route maps, validation reports, runtime checks, status badges, and evidence artifacts agree.

A patch is incomplete if it changes code, folders, reports, evidence state, validators, route meaning, badge status, or documentation meaning without updating the matching README and mini README surfaces.

### Required Gap Scan Order

| Scan step | Surface | What to check |
|---:|---|---|
| 1 | `README.md` | Current checkpoint, badges, metrics, lineage, validation commands, non-claim locks, directory box, and AI rules. |
| 2 | `AGENTS.md` | Agent entry order, patch discipline, and validation expectations. |
| 3 | `README_90_SECONDS.md` | Compressed onboarding is not stale. |
| 4 | `docs/context/repository_context_index.json` | Repo meaning and route descriptions. |
| 5 | `docs/context/rcc_nexus_index.json` | Nexus shell/meridian/sector mapping. |
| 6 | `rcc/nexus/route_map.json` | Task routing and target surfaces. |
| 7 | `rcc/nexus/task_routing_matrix.md` | Human-readable task routing. |
| 8 | Target folder `README.md` | Local folder role, inputs, outputs, and validation command. |
| 9 | Sibling mini READMEs | Adjacent surfaces if routing or folder meaning changed. |
| 10 | Latest reports | `reports/rcc_nexus/`, `reports/architecture/`, `reports/readme/`, `reports/directory/`, `reports/render_hygiene/`, and `reports/release/`. |

### Executable README / Mini Repo Audit

Run:

    python scripts/rcc/audit_readme_surface.py

Expected pass:

    passed: true
    errors: 0
    warnings: 0

Primary outputs:

    reports/readme/latest_readme_mini_repo_audit.json
    reports/readme/latest_readme_mini_repo_audit.md

## AI Failure Learning Ledger

This section is repository memory. When a patch fails, compress the failure into a durable lesson so the next human or AI maintainer does not repeat it.

| Lesson ID | Failure observed | Root cause | Permanent rule |
|---|---|---|---|
| CMS-L-001 | v0.2 README/audit grammar drifted after runtime geometry locked. | Runtime state advanced faster than public narrative grammar. | README/audit grammar must be synchronized after runtime checkpoint changes. |
| CMS-L-002 | v0.2b README audit failed after adding public-format layer. | Required inherited public anchors were not present in the CMS README. | Public-format patches must add the anchors they require before upgrading the audit. |
| CMS-L-003 | v0.2b directory-box validation could not see 33 rows. | The generated table did not render literal backticked path rows. | Directory-box patches must render literal path rows and validate them before commit. |
| CMS-L-004 | v0.2b1 passed anchor/directory checks while README render showed broken tokens like `cc/nexus`, `eports/`, and malformed code fences. | Anchor checks validated presence, not public readability or encoding hygiene. | Every checkpoint must run README render hygiene validation and refresh badges/status before promotion. |

### Failure Response Protocol

1. Stop promotion.
2. Locate the failing surface.
3. Patch minimally.
4. Run the full validation set.
5. Log the lesson.
6. Commit only after the passing repair.

### AI Patch Rule

Any AI patch that causes a failure must update this section before the repair is considered complete. Failure logs are repository memory, not blame records.

<!-- MINI_README_UPDATE_RULE_START -->
Mini README update rule: if a patch changes a folder purpose, folder contents, routing meaning, validation command, evidence surface, or public interpretation, the affected folder-level README must be updated in the same commit.
<!-- MINI_README_UPDATE_RULE_END -->

## Agent Geometry Layer

CMS treats the repository as a navigable coherence field:

    center  = source boundaries, non-claim locks, architecture, context indexes
    inner   = runtime primitives, observation, metric contracts, drift, evidence
    middle  = CLI flows, tests, scripts, validators, route maps
    outer   = reports, ledgers, release seals, public README surfaces

Every patch must preserve route coherence:

    intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson

A patch is coherent only when these surfaces agree:

    README.md
    AGENTS.md
    README_90_SECONDS.md
    docs/context/repository_context_index.json
    docs/context/rcc_nexus_index.json
    rcc/nexus/route_map.json
    rcc/nexus/task_routing_matrix.md
    target folder README.md
    latest validation reports

Non-claim lock: geometric routing improves repository orientation. It is not AI understanding, code correctness, truth, security, AGI, consciousness, or external validation.

## Process Alignment Layer

This layer keeps CMS synchronized after every evolution step.

### Alignment Rules

| Rule | Requirement |
|---|---|
| Version-state rule | After every commit that changes runtime, reports, validators, folders, or public docs, the root README current checkpoint must be updated. |
| Badge/status rule | README badges and Current Public Metrics must update whenever checkpoint, validation status, or release status changes. |
| Render-hygiene rule | Public README must not contain control characters, malformed code fences, damaged paths, or literal unresolved variables. |
| Release-readiness rule | Release readiness and relevant validators are the final local gates before commit/push. |
| Warning-inspection rule | A passing validator with warnings is not ignored; warnings must be repaired or explicitly classified as non-blocking. |
| Directory-box rule | The Full Directory Box must not contain duplicate durable entries and must reflect durable top-level and child surfaces. |
| File-run rule | Large repair scripts must be run with `powershell -ExecutionPolicy Bypass -File`, not pasted line by line. |
| Evidence-refresh rule | If a runtime cycle changes latest artifacts, commit or intentionally discard those artifacts before declaring the repo clean. |
| Boundary rule | Process alignment is repository hygiene. It is not code correctness, external validation, AGI, consciousness, security, or production readiness. |

### Pre-Push Checklist

    $env:PYTHONPATH = ".\src"
    python scripts/rcc/audit_readme_surface.py
    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python scripts/validation/validate_runtime_observation_v0_2.py
    python scripts/validation/validate_directory_box_v0_2b.py
    python scripts/validation/validate_readme_render_hygiene_v0_2b2.py
    python -m cms cycle --repo . --profile CMS-Core
    python -m unittest discover -s tests
    python scripts/validate_release.py

Expected minimum state:

    README audit: passed
    RCC-N: passed
    architecture validation: passed
    runtime validation: passed
    directory box validation: passed
    render hygiene: passed
    unit_tests: OK
    release validation: passed
    K_CMS: 1.0
    D_CMS: 0.0

## AI Rule - Directory Box and Mini README Synchronization

CMS uses RCC-N style navigation. Repository structure is part of the public interface.

Any AI or human patch that adds, removes, renames, or repurposes a folder must update these surfaces in the same commit:

1. The root README Full Directory Box.
2. The affected folder-level mini `README.md`.
3. `docs/context/repository_context_index.json` if route meaning changes.
4. `docs/context/rcc_nexus_index.json` if Nexus position changes.
5. `rcc/nexus/route_map.json` if task routing changes.
6. `rcc/nexus/task_routing_matrix.md` if agent workflow changes.
7. Relevant validation reports after rerunning checks.

Non-claim lock: directory navigation is not correctness, but stale navigation is repository drift.

## Full Directory Box

This box is the durable public navigation spine. The full repository is validated by RCC-N, mini READMEs, and `scripts/validation/validate_directory_box_v0_2b.py`.

| Surface | Purpose |
|---|---|
| `src/cms/` | CMS runtime, CLI, observation, metrics, drift, evidence, validation, memory, planning, correction, schemas, artifacts, and utilities. |
| `configs/metrics/` | Metric contract declarations for repository-bound measurement surfaces. |
| `configs/seeds/` | Future seed/configuration inputs for CMS scenarios and runtime examples. |
| `docs/context/` | Repository context indexes and RCC-N meaning/navigation maps. |
| `docs/architecture/` | Software architecture contracts and architecture validation surfaces. |
| `docs/protocols/` | Process protocols, operating rules, and governance procedures. |
| `docs/theory/` | Theory and conceptual boundary documents. |
| `docs/versions/` | Versioned CMS documents for each evolution layer. |
| `docs/injections/` | Injection records showing what changed, why, and where. |
| `docs/release_seals/` | Release seals for checkpointed repository states. |
| `docs/roadmap/` | Current and future CMS development anchors. |
| `docs/directory/` | Directory-box manifests, directory-lock reports, and public navigation rules. |
| `docs/process/` | Public process rules, status-refresh discipline, and render hygiene policies. |
| `rcc/nexus/` | RCC-N route maps, task routing, agent handoff, and local orientation surfaces. |
| `scripts/rcc/` | README audit scanner, RCC-N checker, render hygiene scanner, and navigation validation utilities. |
| `scripts/validation/` | Architecture, runtime, directory, render, and release validation scripts. |
| `outputs/state/` | Latest observation state emitted by the CMS runtime. |
| `outputs/metrics/` | Latest metric evaluation artifacts. |
| `outputs/drift/` | Latest CMS drift reports and K/D coherence measures. |
| `outputs/evidence/` | Latest evidence packages emitted by the runtime. |
| `outputs/lineage/` | Append-only lineage ledger entries for version continuity. |
| `outputs/injections/` | Append-only injection ledger entries for repository evolution. |
| `outputs/version_registry/` | Machine-readable version registry and next-anchor record. |
| `outputs/directory/` | Machine-readable full directory box and validation reports. |
| `reports/runtime_observation/` | Human-readable and JSON runtime observation reports. |
| `reports/metric_contracts/` | Human-readable and JSON metric-contract reports. |
| `reports/drift/` | Human-readable and JSON drift reports. |
| `reports/evidence/` | Human-readable and JSON evidence package reports. |
| `reports/readme/` | README and mini README audit reports. |
| `reports/rcc_nexus/` | RCC-N navigation check reports. |
| `reports/architecture/` | Architecture validation reports. |
| `reports/directory/` | Directory box and durable surface validation reports. |
| `reports/render_hygiene/` | README render hygiene and badge/status validation reports. |
| `reports/release/` | Release readiness reports and checkpoint validation outputs. |
| `tests/` | Unit tests for runtime observation, metrics, drift, and evidence cycle. |
| `examples/` | Future examples and walkthrough surfaces. |

## CMS-SA v0.2b2 - README Render Hygiene and Badge Status Guard

v0.2b2 repairs public readability and badge drift. It adds a render-hygiene validator that rejects broken code-fence text, control-character residue, damaged paths, stale badges, and unresolved status variables.

Non-claim lock: README render hygiene and badges improve traceability. They do not prove code correctness, truth, AGI, consciousness, production readiness, security, or external validation.