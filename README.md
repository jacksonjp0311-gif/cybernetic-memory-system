# Cybernetic Memory System - Feedback-Governed Repository Memory Runtime

![CMS-SA](https://img.shields.io/badge/CMS--SA-v0.1.2-blue)
![RCC-N](https://img.shields.io/badge/RCC--N-scaffolded-purple)
![Architecture](https://img.shields.io/badge/architecture-anchored-brightgreen)
![Lineage](https://img.shields.io/badge/lineage-recorded-brightgreen)
![README Audit](https://img.shields.io/badge/README%20audit-local--ready-yellow)
![Non-Claim](https://img.shields.io/badge/non--claim--locks-active-black)

Repository: `cybernetic-memory-system`  
Package / CLI: `cms`  
Current checkpoint: **CMS-SA v0.2b - Public Format Alignment and Directory Box Lock**  
Previous seal: **CMS-SA v0.2a - README / Audit Anchor Synchronization**

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
| Current checkpoint | CMS-SA v0.2a |
| Previous seal | CMS-SA v0.1.1 |
| Runtime package | scaffolded |
| RCC-N mini README coverage | target 1.0 |
| Version registry | active |
| Injection ledger | active |
| Release seal discipline | active |
| Claim status | architecture + local scaffold only |

Interpretation: CMS is becoming a self-traceable repository control surface. It does not prove intelligence, consciousness, correctness, production safety, external validation, or truth.
---

## Human Director Box

### What this repository is

This repo is a local-first cybernetic repository-memory runtime:

`	ext
repository -> observation manifest -> metric contracts -> metric evaluation -> drift report -> evidence package -> validation report -> lineage / release surface
`

CMS is designed to make repository state observable, measurable, auditable, and easier for humans and AI agents to maintain without relying on implicit memory.

### What this repository is not

This repo does **not** prove code correctness, security, truth, AGI, consciousness, production readiness, external validation, or real-world correctness. It is a repository-bound governance and measurement runtime.

## Current Public Metrics

| Surface | Result |
|---|---:|
| Current checkpoint | CMS-SA v0.2b |
| Previous seal | CMS-SA v0.2a |
| Latest git head before patch | $GitHead |
| Metric evaluation | $MetricPassed |
| README / mini repo audit | $ReadmePassed |
| RCC-N checker | $RccPassed |
| Runtime observation validation | $RuntimePassed |
| CMS coherence K_CMS | $Kcms |
| CMS drift D_CMS | $Dcms |
| Evidence classification | $Class |
| Release allowed | $ReleaseAllowed |
| Latest observation manifest | outputs/state/latest_observation_manifest.json |
| Latest metric evaluation | outputs/metrics/latest_metric_evaluation.json |
| Latest drift report | outputs/drift/latest_drift_report.json |
| Latest evidence package | outputs/evidence/latest_evidence_package.json |
| Directory box manifest | docs/directory/cms_full_directory_box_v0_2b.json |
| Directory box validation | eports/directory/latest_directory_box_validation.md |

## Agent Geometry Layer

CMS treats the repository as a navigable coherence field:

`	ext
center  = source boundaries, non-claim locks, architecture, context indexes
inner   = runtime primitives, observation, metric contracts, drift, evidence
middle  = CLI flows, tests, scripts, validators, route maps
outer   = reports, ledgers, release seals, public README surfaces
`

Every patch must preserve route coherence:

`	ext
intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson
`

A patch is coherent only when these surfaces agree:

`	ext
README.md
AGENTS.md
README_90_SECONDS.md
docs/context/repository_context_index.json
docs/context/rcc_nexus_index.json
rcc/nexus/route_map.json
rcc/nexus/task_routing_matrix.md
target folder README.md
latest validation reports
`

Non-claim lock: geometric routing improves repository orientation. It is not AI understanding, code correctness, truth, security, AGI, consciousness, or external validation.

## Process Alignment Layer

This layer keeps CMS synchronized after every evolution step.

### Alignment Rules

| Rule | Requirement |
|---|---|
| Version-state rule | After every commit that changes runtime, reports, validators, folders, or public docs, the root README current checkpoint must be updated. |
| Release-readiness rule | Release readiness and relevant validators are the final local gates before commit/push. |
| Warning-inspection rule | A passing validator with warnings is not ignored; warnings must be repaired or explicitly classified as non-blocking. |
| Directory-box rule | The Full Directory Box must not contain duplicate durable entries and must reflect durable top-level and child surfaces. |
| File-run rule | Large repair scripts must be run with powershell -ExecutionPolicy Bypass -File, not pasted line by line. |
| Evidence-refresh rule | If a runtime cycle changes latest artifacts, commit or intentionally discard those artifacts before declaring the repo clean. |
| Boundary rule | Process alignment is repository hygiene. It is not code correctness, external validation, AGI, consciousness, security, or production readiness. |

### Pre-Push Checklist

`powershell
$env:PYTHONPATH = ".\src"
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python scripts/validation/validate_runtime_observation_v0_2.py
python scripts/validation/validate_directory_box_v0_2b.py
python -m cms cycle --repo . --profile CMS-Core
python -m unittest discover -s tests
python scripts/validate_release.py
`

Expected minimum state:

`	ext
README audit: passed
RCC-N: passed
architecture validation: passed
runtime validation: passed
directory box validation: passed
unit_tests: OK
release validation: passed
K_CMS: 1.0
D_CMS: 0.0
`

## AI Rule - Directory Box and Mini README Synchronization

CMS uses RCC-N style navigation. Repository structure is part of the public interface.

Any AI or human patch that adds, removes, renames, or repurposes a folder must update these surfaces in the same commit:

1. The root README Full Directory Box.
2. The affected folder-level mini README.md.
3. docs/context/repository_context_index.json if route meaning changes.
4. docs/context/rcc_nexus_index.json if Nexus position changes.
5. cc/nexus/route_map.json if task routing changes.
6. cc/nexus/task_routing_matrix.md if agent workflow changes.
7. Relevant validation reports after rerunning checks.

Non-claim lock: directory navigation is not correctness, but stale navigation is repository drift.

## Full Directory Box

This box is the durable public navigation spine. The full repository is validated by RCC-N, mini READMEs, and scripts/validation/validate_directory_box_v0_2b.py.

| Surface | Purpose |
|---|---|
| $(System.Collections.Hashtable.path) | CMS runtime, CLI, observation, metrics, drift, evidence, validation, memory, planning, correction, schemas, artifacts, and utilities. |
| $(System.Collections.Hashtable.path) | Metric contract declarations for repository-bound measurement surfaces. |
| $(System.Collections.Hashtable.path) | Future seed/configuration inputs for CMS scenarios and runtime examples. |
| $(System.Collections.Hashtable.path) | Repository context indexes and RCC-N meaning/navigation maps. |
| $(System.Collections.Hashtable.path) | Software architecture contracts and architecture validation surfaces. |
| $(System.Collections.Hashtable.path) | Process protocols, operating rules, and governance procedures. |
| $(System.Collections.Hashtable.path) | Theory and conceptual boundary documents. |
| $(System.Collections.Hashtable.path) | Versioned CMS documents for each evolution layer. |
| $(System.Collections.Hashtable.path) | Injection records showing what changed, why, and where. |
| $(System.Collections.Hashtable.path) | Release seals for checkpointed repository states. |
| $(System.Collections.Hashtable.path) | Current and future CMS development anchors. |
| $(System.Collections.Hashtable.path) | Directory-box manifests, directory-lock reports, and public navigation rules. |
| $(System.Collections.Hashtable.path) | RCC-N route maps, task routing, agent handoff, and local orientation surfaces. |
| $(System.Collections.Hashtable.path) | README audit scanner, RCC-N checker, and navigation validation utilities. |
| $(System.Collections.Hashtable.path) | Architecture, runtime, directory, and release validation scripts. |
| $(System.Collections.Hashtable.path) | Latest observation state emitted by the CMS runtime. |
| $(System.Collections.Hashtable.path) | Latest metric evaluation artifacts. |
| $(System.Collections.Hashtable.path) | Latest CMS drift reports and K/D coherence measures. |
| $(System.Collections.Hashtable.path) | Latest evidence packages emitted by the runtime. |
| $(System.Collections.Hashtable.path) | Append-only lineage ledger entries for version continuity. |
| $(System.Collections.Hashtable.path) | Append-only injection ledger entries for repository evolution. |
| $(System.Collections.Hashtable.path) | Machine-readable version registry and next-anchor record. |
| $(System.Collections.Hashtable.path) | Machine-readable full directory box and validation reports. |
| $(System.Collections.Hashtable.path) | Human-readable and JSON runtime observation reports. |
| $(System.Collections.Hashtable.path) | Human-readable and JSON metric-contract reports. |
| $(System.Collections.Hashtable.path) | Human-readable and JSON drift reports. |
| $(System.Collections.Hashtable.path) | Human-readable and JSON evidence package reports. |
| $(System.Collections.Hashtable.path) | README and mini README audit reports. |
| $(System.Collections.Hashtable.path) | RCC-N navigation check reports. |
| $(System.Collections.Hashtable.path) | Architecture validation reports. |
| $(System.Collections.Hashtable.path) | Directory box and durable surface validation reports. |
| $(System.Collections.Hashtable.path) | Release readiness reports and checkpoint validation outputs. |
| $(System.Collections.Hashtable.path) | Unit tests for runtime observation, metrics, drift, and evidence cycle. |
| $(System.Collections.Hashtable.path) | Future examples and walkthrough surfaces. |

## CMS-SA v0.2b — Public Format Alignment and Directory Box Lock

v0.2b imports the mature public README contract pattern into CMS:

`	ext
Human Director Box
Current Public Metrics
Agent Geometry Layer
Process Alignment Layer
AI Directory Synchronization Rule
Full Directory Box
Directory Box Validator
`

Non-claim lock: public format alignment improves traceability. It does not prove code correctness, truth, AGI, consciousness, production readiness, security, or external validation.
