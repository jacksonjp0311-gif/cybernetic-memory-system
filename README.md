# Cybernetic Memory System - Feedback-Governed Repository Memory Runtime

![CMS-SA](https://img.shields.io/badge/CMS--SA-v0.3b-blue)
![RCC-N](https://img.shields.io/badge/RCC--N-passing-brightgreen)
![Architecture](https://img.shields.io/badge/architecture-passing-brightgreen)
![Lineage](https://img.shields.io/badge/lineage-recorded-brightgreen)
![README Audit](https://img.shields.io/badge/README%20audit-passing-brightgreen)
![Directory Box](https://img.shields.io/badge/directory%20box-passing-brightgreen)
![Render Hygiene](https://img.shields.io/badge/render%20hygiene-passing-brightgreen)
![Markdown Structure](https://img.shields.io/badge/markdown%20structure-passing-brightgreen)
![Public Sync](https://img.shields.io/badge/public%20sync-stable--guard-brightgreen)
![K_CMS](https://img.shields.io/badge/K__CMS-1.0-blue)
![D_CMS](https://img.shields.io/badge/D__CMS-0.0-blue)
![Non-Claim](https://img.shields.io/badge/non--claim--locks-active-black)

Repository: `cybernetic-memory-system`  
Package / CLI: `cms`  
Current checkpoint: **CMS-SA v0.3b - Feedback Quality and Lifecycle Engine**  
Previous seal: **CMS-SA v0.2b3 - README Structure, Public Sync Guard, and Tau Lesson Embedding**

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
- No Markdown structure, no public README release.
- No public sync guard, no public checkpoint promotion.

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
| v0.2b3 Tau Lessons / Public Sync | Are Tau-style README lessons and public sync surfaces embedded? | `reports/public_sync/latest_public_sync_report.md` |
| v0.2b3a Validator Repair | Does Markdown structure validation avoid false positives on data rows? | `reports/markdown_structure/latest_markdown_structure.md` |

Current public finding: CMS can be structured as a feedback-governed repository-memory runtime. The current repo is a local evidence-governance and repository-observability system, not a proof of correctness, intelligence, consciousness, production safety, external validation, or truth.

## Human Director Box

### What this repository is

This repo is a local-first cybernetic repository-memory runtime:

```text
repository -> observation manifest -> metric contracts -> metric evaluation
-> drift report -> evidence package -> validation report
-> lineage / release surface -> README/RCC/status sync
```

CMS is designed to make repository state observable, measurable, auditable, and easier for humans and AI agents to maintain without relying on implicit memory.

### What this repository is not

This repo does **not** prove code correctness, security, truth, AGI, consciousness, production readiness, external validation, or real-world correctness. It is a repository-bound governance and measurement runtime.

## Current Public Metrics

| Surface | Result |
|---|---:|
| Current checkpoint | CMS-SA v0.3b |
| Previous seal | CMS-SA v0.3a2 |
| README / mini repo audit | `True` |
| RCC-N checker | `True` |
| Runtime observation validation | `True` |
| Directory box validation | `True` |
| Render hygiene | `True` |
| Markdown structure validation | `True` |
| Public sync validation | `True` |
| Reflective Git geometry validation | `True` |
| Release validator | `True` |
| CMS coherence K_CMS | `1.0` |
| CMS drift D_CMS | `0.0` |
| Evidence classification | `CMS-B` |
| Latest observation manifest | `outputs/state/latest_observation_manifest.json` |
| Latest metric evaluation | `outputs/metrics/latest_metric_evaluation.json` |
| Latest drift report | `outputs/drift/latest_drift_report.json` |
| Latest evidence package | `outputs/evidence/latest_evidence_package.json` |
| Latest reflective Git geometry | `outputs/geometry/latest_reflective_git_geometry.json` |
| Geometry validation report | `reports/geometry/latest_reflective_git_geometry_validation.md` |

## Quick Start

Run the local validation stack:

```powershell
cd "$env:USERPROFILE\OneDrive\Desktop\cybernetic-memory-system"
$env:PYTHONPATH = ".\src"

python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python scripts/validation/validate_runtime_observation_v0_2.py
python scripts/validation/validate_directory_box_v0_2b.py
python scripts/validation/validate_readme_render_hygiene_v0_2b2.py
python scripts/validation/validate_markdown_structure_v0_2b3.py
python scripts/validation/validate_public_sync_v0_2b3.py
python scripts/geometry/emit_reflective_git_geometry.py
python -m cms cycle --repo . --profile CMS-Core
python -m unittest discover -s tests
python scripts/validate_release.py
```

## Repository Layers

| Layer | Purpose | Main paths |
|---|---|---|
| CMS runtime | Observation, metric contracts, drift, evidence, CLI cycle | `src/cms/`, `configs/metrics/`, `tests/` |
| RCC-N navigation | Agent and human orientation, routing, handoff, context indexes | `rcc/nexus/`, `docs/context/` |
| Public surface governance | README audit, render hygiene, Markdown structure, public sync | `scripts/rcc/`, `scripts/validation/`, `reports/readme/` |
| Evidence observability | Latest state, metrics, drift, evidence packages | `outputs/state/`, `outputs/metrics/`, `outputs/drift/`, `outputs/evidence/` |
| Version and injection memory | Version registry, lineage ledger, injection ledger, release seals | `outputs/version_registry/`, `outputs/lineage/`, `docs/release_seals/` |
| Reflection and process rules | Bounded process lessons, Law of Sufficient Form, badge/status discipline | `docs/reflection/`, `docs/process/` |

## Historical Report Archive

Historical detail should live in archive reports, version docs, injections, and mini READMEs, not only in the root README body.

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
| `reports/directory/latest_directory_box_validation.md` | Current directory-box validation |
| `reports/render_hygiene/latest_readme_render_hygiene.md` | Current render hygiene validation |
| `reports/markdown_structure/latest_markdown_structure.md` | Current Markdown structure validation |
| `reports/public_sync/latest_public_sync_report.md` | Current public sync validation |
| `reports/release/latest_release_readiness.md` | Current release readiness report |
| `docs/reflection/law_of_sufficient_form_v0_2b3.md` | Bounded reflection on governed form |

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

### Evidence Artifacts

Primary runtime artifacts are written under:

```text
outputs/state/
outputs/metrics/
outputs/drift/
outputs/evidence/
```

Release and validation surfaces are written under:

```text
reports/readme/
reports/rcc_nexus/
reports/architecture/
reports/directory/
reports/render_hygiene/
reports/markdown_structure/
reports/public_sync/
reports/release/
```

## PART II - RCC Nexus README

### RCC Nexus Identity

RCC tells the agent what the repository means.  
RCC-N tells the agent where it is.  
Validation tells the agent whether the repository-bound checks agreed.

### Repository Sphere

| Shell | Meaning |
|---|---|
| center | Source boundary, non-claim locks, architecture, context indexes. |
| inner | Runtime primitives: observer, metric contracts, drift reports, evidence packages. |
| middle | Processes: CLI flow, examples, tests, scripts, validation workflows. |
| outer | Evidence and reflection: outputs, ledgers, reports, visuals, release notes. |

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
| `scripts/rcc/check_rcc_nexus.py` | RCC-N checker. |
| `scripts/rcc/audit_readme_surface.py` | README / mini repo audit scanner. |
| `scripts/validation/validate_markdown_structure_v0_2b3.py` | Markdown table/heading structure validator. |
| `scripts/validation/validate_public_sync_v0_2b3.py` | Local/origin/version registry sync validator. |

### RCC Nexus Echo Location

| Field | Value |
|---|---|
| Shell | center |
| Meridians | source, validation, evidence, safety, agent, runtime, memory |
| Sector | rcc |
| Version / TTL | CMS-RCC-N-v0.3a1 / 180 days |
| Last verified | 2026-06-02 |
| Local role | Root orientation surface for humans, RCC Nexus navigation, and AI agents. |

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
| README / mini README patch | `README.md`, target mini README, route maps | README audit + render hygiene + Markdown structure + RCC-N |
| Directory structure patch | root Full Directory Box, affected mini READMEs, context indexes | directory validator + README audit + RCC-N |
| Badge/status patch | `README.md`, latest reports, version registry | render hygiene + README audit + release validation |
| Public sync patch | `README.md`, version registry, Git state | public sync + Markdown structure + README audit |
| Release/docs patch | `docs/`, `reports/release/`, version registry | release validation + README audit |

## README + Mini Repo Audit Map

### Audit Purpose

The repository is considered healthy only when public surfaces, folder-level mini READMEs, route maps, validation reports, runtime checks, status badges, Markdown structure, public sync state, and evidence artifacts agree.

A patch is incomplete if it changes code, folders, reports, evidence state, validators, route meaning, badge status, or documentation meaning without updating the matching README and mini README surfaces.

### Required Gap Scan Order

| Scan step | Surface | What to check |
|---:|---|---|
| 1 | `README.md` | Current checkpoint, badges, metrics, lineage, validation commands, non-claim locks, directory box, tables, and AI rules. |
| 2 | `AGENTS.md` | Agent entry order, patch discipline, and validation expectations. |
| 3 | `README_90_SECONDS.md` | Compressed onboarding is not stale. |
| 4 | `docs/context/repository_context_index.json` | Repo meaning and route descriptions. |
| 5 | `docs/context/rcc_nexus_index.json` | Nexus shell/meridian/sector mapping. |
| 6 | `rcc/nexus/route_map.json` | Task routing and target surfaces. |
| 7 | `rcc/nexus/task_routing_matrix.md` | Human-readable task routing. |
| 8 | Target folder `README.md` | Local folder role, inputs, outputs, and validation command. |
| 9 | Sibling mini READMEs | Adjacent surfaces if routing or folder meaning changed. |
| 10 | Latest reports | `reports/rcc_nexus/`, `reports/architecture/`, `reports/readme/`, `reports/directory/`, `reports/render_hygiene/`, `reports/markdown_structure/`, `reports/public_sync/`, and `reports/release/`. |

### Gap Classes the AI Must Detect

| Gap class | Detection question | Required repair |
|---|---|---|
| README drift | Does the root README describe the current repo state? | Patch checkpoint, metrics, lineage, commands, and directory box. |
| Mini README drift | Did a folder change without its README changing? | Patch the affected folder README. |
| Route drift | Did task routing or folder purpose change? | Patch context indexes and route maps. |
| Validation drift | Do public claims lack fresh validation reports? | Rerun validation and refresh reports. |
| Runtime drift | Did Python code change without compile/import/test proof? | Run compile, import, tests, runtime cycle, and release validation. |
| Evidence drift | Could one run overwrite another? | Verify collision-proof run IDs, latest evidence package, and snapshot policy. |
| Claim drift | Does language imply stronger proof than evidence allows? | Restore downgrade wording and non-claim locks. |
| Encoding drift | Do headings, arrows, paths, or code fences show mojibake? | Rewrite affected README surfaces using UTF-8 and ASCII-safe syntax unless Unicode is required by an audit anchor. |
| Markdown structure drift | Do tables or lists collapse into single-line public rendering? | Rewrite README line-by-line and rerun Markdown structure validation. |
| Public sync drift | Does local state differ from origin/main, tag, version registry, or public README? | Fetch, compare, repair, push, and rerun public sync guard. |

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

## AI Failure Learning Ledger

This section is repository memory. When a patch fails, compress the failure into a durable lesson so the next human or AI maintainer does not repeat it.

| Lesson ID | Failure observed | Root cause | Permanent rule |
|---|---|---|---|
| CMS-L-001 | v0.2 README/audit grammar drifted after runtime geometry locked. | Runtime state advanced faster than public narrative grammar. | README/audit grammar must be synchronized after runtime checkpoint changes. |
| CMS-L-002 | v0.2b README audit failed after adding public-format layer. | Required inherited public anchors were not present in the CMS README. | Public-format patches must add the anchors they require before upgrading the audit. |
| CMS-L-003 | v0.2b directory-box validation could not see 33 rows. | The generated table did not render literal backticked path rows. | Directory-box patches must render literal path rows and validate them before commit. |
| CMS-L-004 | v0.2b1 passed anchor/directory checks while README render showed broken tokens like `cc/nexus`, `eports/`, and malformed code fences. | Anchor checks validated presence, not public readability or encoding hygiene. | Every checkpoint must run README render hygiene validation and refresh badges/status before promotion. |
| CMS-L-005 | v0.2b2 passed render hygiene but GitHub/raw extraction still showed collapsed tables and low line count. | Render hygiene checked bad tokens, not Markdown table/heading line structure. | Public README releases must pass Markdown structure validation with line-count and table isolation checks. |
| CMS-L-006 | Public state can appear stale even when local validation passes. | Local validation does not prove origin/main, tag, version registry, and README checkpoint agree. | Every public checkpoint must run a public sync guard before promotion. |
| CMS-L-007 | v0.2b3 Markdown validator flagged normal table data rows as missing separators. | Validator logic checked every row as if it were a header. | Markdown validators must parse table blocks, not treat normal data rows as headers. |
| CMS-L-008 | v0.2b3a post-push public-sync reports changed again after being committed. | The committed report stored volatile HEAD-specific evidence, so the next commit made it stale. | Committed public-sync reports must use stable status fields and omit volatile commit hashes; runtime validation may still check HEAD/origin/tag agreement. |
| CMS-L-009 | v0.2b3b repair failed to overwrite files even while the script continued. | PowerShell was pasted line-by-line and .NET WriteAllText resolved relative paths outside the repo root. | Large repair scripts must run from a file and all file writes must join paths against the repository root. |
| CMS-L-010 | v0.2b3c public sync was stable but README validators still failed. | Validator expected checkpoint and badge tokens were pinned to older v0.2b3a public strings. | Validators must advance their expected public tokens whenever checkpoint badges and README status advance. |
| CMS-L-011 | v0.2b3d ended with clean Git status even though README audit still returned passed:false. | The release script checked Git cleanliness but did not parse validator truth. | Release gates must parse validator JSON and block on passed:false; clean Git status alone is not release readiness. |
| CMS-L-012 | Commit history contained repair structure but CMS did not yet extract it as geometry. | Git was treated as version storage rather than route-bearing repository memory. | Every commit should be interpretable as a routed geometry event with shell, meridian, sector, evidence, and release-truth context. |
| CMS-L-013 | v0.3a geometry reports became dirty after final report-refresh commit. | Reflective geometry included report-only refresh commits, causing the report to rewrite itself after commit. | Committed reflective geometry must exclude report-only refresh commits from semantic geometry nodes. |
| CMS-L-014 | README carried stale public metrics and older checkpoint framing after geometry advanced. | Runtime/report surfaces advanced faster than README summary and API-readiness rules. | README metrics, snapshot, quick-start, directory, and API boundary sections must advance with geometry/runtime layers. |
| CMS-L-015 | Geometry validation kept rewriting latest geometry artifacts after every semantic commit. | The validator was also the emitter, so observing geometry mutated the geometry evidence surface. | Observation and validation must be separated from evidence emission; a read-only validator must not mutate the artifact it validates. |
| CMS-L-016 | Feedback could be discussed narratively without typed lifecycle status. | Findings lacked a formal scoring, classification, downgrade, negative-control, and falsification surface. | Feedback must become a typed lifecycle object before promotion to memory, release, or API-write status. |

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


## Reflective Git Geometry Box

CMS now treats Git history as a repository geometry surface.

```text
commit hash      = point
parent link      = edge
branch           = active trajectory
tag              = sealed boundary
commit message   = semantic intent
changed files    = affected surfaces
validator output = truth boundary
report artifacts = evidence shell
README/registry  = public reflection surface
```

Core rule:

```text
A commit is not only a change; it is a routed event in repository geometry.
```

Reflection route:

```text
Git history -> version lineage -> patch route -> changed surfaces
-> validators -> evidence -> lessons -> next anchor
```

Primary artifacts:

| Surface | Role |
|---|---|
| `configs/geometry/reflective_git_geometry_contract.json` | Reflective Git geometry contract. |
| `schemas/reflective_git_node.schema.json` | Machine-readable node schema. |
| `src/cms/geometry/git_geometry.py` | Runtime extractor for commit-route geometry. |
| `outputs/geometry/latest_reflective_git_geometry.json` | Latest machine-readable Git geometry field. |
| `reports/geometry/latest_reflective_git_geometry.md` | Human-readable Git geometry report. |
| `scripts/validation/validate_reflective_git_geometry_v0_3.py` | Geometry validation gate. |

Rules:

- No geometry-free commit interpretation.
- Report-only refresh commits are excluded from semantic geometry nodes.
- Latest geometry reports must not self-invalidate after report refresh commits.
- A validator must not mutate the geometry it validates.
- Geometry emission and geometry validation must remain separate phases.
- Every geometry node must include commit, route, changed files, and release-truth context.
- Feedback lifecycle objects must attach to Git geometry coordinates.
- Geometry classification is repository orientation, not proof of correctness.

Non-claim lock: reflective Git geometry improves repository orientation, routing, and evidence traceability. It does not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.

## Agent Geometry Layer

CMS treats the repository as a navigable coherence field:

```text
center  = source boundaries, non-claim locks, architecture, context indexes
inner   = runtime primitives, observation, metric contracts, drift, evidence
middle  = CLI flows, tests, scripts, validators, route maps
outer   = reports, ledgers, release seals, public README surfaces
```

Every patch must preserve route coherence:

```text
intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson
```

A patch is coherent only when these surfaces agree:

```text
README.md
AGENTS.md
README_90_SECONDS.md
docs/context/repository_context_index.json
docs/context/rcc_nexus_index.json
rcc/nexus/route_map.json
rcc/nexus/task_routing_matrix.md
target folder README.md
latest validation reports
```

Non-claim lock: geometric routing improves repository orientation. It is not AI understanding, code correctness, truth, security, AGI, consciousness, or external validation.



Feedback lifecycle rule:

```text
No feedback item may promote to memory, release, or API-write status without
route classification, evidence, validator binding, lifecycle state,
downgrade path, falsification condition, and non-claim lock.
```
## Two-Way API Transmission Readiness Box

CMS is preparing for an eventual two-way API transmission process:

```text
external request -> intent packet -> route classification -> dry-run plan
-> diff proposal -> validation stack -> evidence package
-> human authorization -> write action -> commit/push/tag -> public sync
```

Inbound API rules:

- No direct write without route classification.
- No direct write without dry-run diff.
- No direct write without validator binding.
- No direct write without evidence package.
- No direct write without human authorization unless explicitly running in a future constrained automation profile.
- No API response may claim correctness beyond repository-bound validation.

Outbound API rules:

- Outbound state must cite version registry, release seal, validation reports, and evidence package.
- Outbound state must include non-claim locks.
- Outbound state must distinguish observation, recommendation, patch plan, and committed fact.
- Outbound state must never treat memory, geometry, or validator agreement as external truth.

Non-claim lock: two-way API transmission is a future integration pattern. It is not yet an autonomous write authority, production deployment, security boundary, AGI, consciousness, or external validation.

## Process Alignment Layer

This layer keeps CMS synchronized after every evolution step.

### Alignment Rules

| Rule | Requirement |
|---|---|
| Version-state rule | After every commit that changes runtime, reports, validators, folders, or public docs, the root README current checkpoint must be updated. |
| Badge/status rule | README badges and Current Public Metrics must update whenever checkpoint, validation status, or release status changes. |
| Render-hygiene rule | Public README must not contain control characters, malformed code fences, damaged paths, or literal unresolved variables. |
| Markdown-structure rule | Public README tables, headings, and code blocks must render as isolated Markdown lines. |
| Public-sync rule | Local HEAD, origin/main, README checkpoint, version registry, and release tag surface must agree before public promotion. |
| Public-sync phase rule | Before push, local ahead of origin is a warning; after push, local and origin must match. |
| Release-readiness rule | Release readiness and relevant validators are the final local gates before commit/push. |
| Warning-inspection rule | A passing validator with warnings is not ignored; warnings must be repaired or explicitly classified as non-blocking. |
| Directory-box rule | The Full Directory Box must not contain duplicate durable entries and must reflect durable top-level and child surfaces. |
| File-run rule | Large repair scripts must be run with `powershell -ExecutionPolicy Bypass -File`, not pasted line by line. |
| Evidence-refresh rule | If a runtime cycle changes latest artifacts, commit or intentionally discard those artifacts before declaring the repo clean. |
| Boundary rule | Process alignment is repository hygiene. It is not code correctness, external validation, AGI, consciousness, security, or production readiness. |

### Pre-Push Checklist

```powershell
$env:PYTHONPATH = ".\src"
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python scripts/validation/validate_runtime_observation_v0_2.py
python scripts/validation/validate_directory_box_v0_2b.py
python scripts/validation/validate_readme_render_hygiene_v0_2b2.py
python scripts/validation/validate_markdown_structure_v0_2b3.py
python scripts/validation/validate_public_sync_v0_2b3.py
python scripts/geometry/emit_reflective_git_geometry.py
python -m cms cycle --repo . --profile CMS-Core
python -m unittest discover -s tests
python scripts/validate_release.py
```

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

## Law of Sufficient Form

> When enough governed form is in place, structure begins to hold itself.

Operational form: a system becomes self-stabilizing when its claims, evidence, routing, validation, memory, public status, and non-claim locks are all visible to both humans and agents.

Primary reflection surface:

- `docs/reflection/law_of_sufficient_form_v0_2b3.md`

Boundary: reflection names process insight; it does not replace validation, evidence, source provenance, or non-claim locks.

## Full Directory Box

This box is the durable public navigation spine. The full repository is validated by RCC-N, mini READMEs, and `scripts/validation/validate_directory_box_v0_2b.py`.

| Surface | Purpose |
|---|---|
| `src/cms/` | CMS runtime, CLI, observation, metrics, drift, evidence, validation, memory, planning, correction, schemas, artifacts, and utilities. |
| `configs/metrics/` | Metric contract declarations for repository-bound measurement surfaces. |
| `configs/seeds/` | CMS test seeds and future runtime examples. |
| `docs/context/` | Repository context indexes, validation surface, RCC-N meaning maps, and sync contracts. |
| `docs/architecture/` | Software architecture contracts and architecture validation surfaces. |
| `docs/protocols/` | Process protocols, operating rules, and governance procedures. |
| `docs/theory/` | Theory and conceptual boundary documents. |
| `docs/versions/` | Versioned CMS documents for each evolution layer. |
| `docs/injections/` | Injection records showing what changed, why, and where. |
| `docs/release_seals/` | Release seals for checkpointed repository states. |
| `docs/roadmap/` | Current and future CMS development anchors. |
| `docs/directory/` | Directory-box manifests, directory-lock reports, and public navigation rules. |
| `docs/process/` | Public process rules, status-refresh discipline, render hygiene, and public sync policies. |
| `docs/reflection/` | Bounded process reflections such as Law of Sufficient Form. |
| `rcc/nexus/` | RCC-N route maps, task routing, agent handoff, echo location, and local orientation surfaces. |
| `scripts/rcc/` | README audit scanner, RCC-N checker, render hygiene scanner, and navigation validation utilities. |
| `scripts/validation/` | Architecture, runtime, directory, render, public sync, markdown structure, and release validation scripts. |
| `outputs/state/` | Latest observation state emitted by the CMS runtime. |
| `outputs/metrics/` | Latest metric evaluation artifacts. |
| `outputs/drift/` | Latest CMS drift reports and K/D coherence measures. |
| `outputs/evidence/` | Latest evidence packages emitted by the runtime. |
| `outputs/lineage/` | Append-only lineage ledger entries for version continuity. |
| `outputs/injections/` | Append-only injection ledger entries for repository evolution. |
| `outputs/version_registry/` | Machine-readable version registry and next-anchor record. |
| `outputs/directory/` | Machine-readable full directory box and validation reports. |
| `outputs/roadmap/` | Machine-readable or mirrored next-anchor roadmaps. |
| `reports/runtime_observation/` | Human-readable and JSON runtime observation reports. |
| `reports/metric_contracts/` | Human-readable and JSON metric-contract reports. |
| `reports/drift/` | Human-readable and JSON drift reports. |
| `reports/evidence/` | Human-readable and JSON evidence package reports. |
| `reports/readme/` | README and mini README audit reports. |
| `reports/rcc_nexus/` | RCC-N navigation check reports. |
| `reports/architecture/` | Architecture validation reports. |
| `reports/directory/` | Directory box and durable surface validation reports. |
| `reports/render_hygiene/` | README render hygiene and badge/status validation reports. |
| `reports/markdown_structure/` | Markdown line structure and public table rendering reports. |
| `reports/public_sync/` | Local/origin/public checkpoint sync reports. |
| `reports/release/` | Release readiness reports and checkpoint validation outputs. |
| `tests/` | Unit tests for runtime observation, metrics, drift, and evidence cycle. |
| `examples/` | Future examples and walkthrough surfaces. |

## CMS-SA v0.2b3a - README Structure Validator Repair and Public Sync Phase Split

v0.2b3a repairs v0.2b3 by restoring missing public sections and fixing the Markdown structure validator so normal table rows are not misclassified as table headers.

Non-claim lock: README structure, public sync, and Tau-derived lessons improve traceability. They do not prove code correctness, truth, AGI, consciousness, production readiness, security, or external validation.