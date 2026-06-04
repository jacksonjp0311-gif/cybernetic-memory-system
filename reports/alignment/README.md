# Alignment Reports

Echo Location:

| Field | Value |
|---|---|
| Shell | center |
| Meridian | geometry, feedback, validation, evidence |
| Sector | alignment |
| Version / TTL | CMS-RCC-N-v0.4.2 / 180 days |
| Last verified | 2026-06-02 |

## Purpose

Stores human-readable and JSON validation surfaces for multi-level geometric feedback alignment.

## Inputs

outputs/alignment/latest_multilevel_alignment_report.json

## Outputs

latest_multilevel_alignment_report.md and latest_multilevel_alignment_validation.md

## Validation

``powershell
python scripts/validation/validate_multilevel_alignment_v0_3b2.py
``

## Alignment Rule

This mini README must update when this folder's purpose, files, routing meaning, evidence role, validation command, or public interpretation changes.

## Non-claim Lock

This folder supports repository-bound multi-level geometric alignment. It does not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.
Current checkpoint: CMS-SA v0.3b3

## CMS-RCC-N-v0.4.2 Surface Alignment

Role: Alignment Reports

Current checkpoint: CMS-SA v0.4.2 - Loop Drift Pressure Metrics

Current version: v0.4.2

Previous version: v0.4.1

Update rule: when the version registry advances, this mini README must either refresh to the current RCC-N token or explicitly mark itself as historical.

Preseal boundary: public-sync tag absence is pressure, not local alignment failure.

Postseal boundary: public-sync must pass after commit, tag, and push.

Non-claim lock: Registry-derived alignment is repository-bound and does not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.
