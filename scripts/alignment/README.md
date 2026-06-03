# Alignment Emitters

Echo Location:

| Field | Value |
|---|---|
| Shell | center |
| Meridian | geometry, feedback, validation, evidence |
| Sector | alignment |
| Version / TTL | CMS-RCC-N-v0.3b5 / 180 days |
| Last verified | 2026-06-02 |

## Purpose

Contains explicit write-capable alignment emitters. Emitters are separate from validators.

## Inputs

Alignment runtime module and existing CMS reports.

## Outputs

outputs/alignment/latest_multilevel_alignment_report.json and reports/alignment/latest_multilevel_alignment_report.*

## Validation

``powershell
python scripts/alignment/emit_multilevel_alignment_v0_3b2.py
``

## Alignment Rule

This mini README must update when this folder's purpose, files, routing meaning, evidence role, validation command, or public interpretation changes.

## Non-claim Lock

This folder supports repository-bound multi-level geometric alignment. It does not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.
Current checkpoint: CMS-SA v0.3b3
