# Alignment Outputs

Echo Location:

| Field | Value |
|---|---|
| Shell | center |
| Meridian | geometry, feedback, validation, evidence |
| Sector | alignment |
| Version / TTL | CMS-RCC-N-v0.3b2 / 180 days |
| Last verified | 2026-06-02 |

## Purpose

Stores latest machine-readable multi-level alignment outputs emitted by the CMS alignment runtime.

## Inputs

scripts/alignment/emit_multilevel_alignment_v0_3b2.py

## Outputs

latest_multilevel_alignment_report.json

## Validation

``powershell
python scripts/validation/validate_multilevel_alignment_v0_3b2.py
``

## Alignment Rule

This mini README must update when this folder's purpose, files, routing meaning, evidence role, validation command, or public interpretation changes.

## Non-claim Lock

This folder supports repository-bound multi-level geometric alignment. It does not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.