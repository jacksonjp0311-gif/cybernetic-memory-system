# Alignment Reports

Echo Location:

| Field | Value |
|---|---|
| Shell | center |
| Meridian | geometry, feedback, validation, evidence |
| Sector | alignment |
| Version / TTL | CMS-RCC-N-v0.3b2a3 / 180 days |
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
Current checkpoint: CMS-SA v0.3b2a3
