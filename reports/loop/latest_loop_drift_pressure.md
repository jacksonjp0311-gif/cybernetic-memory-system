# CMS-SA v0.4.2 Loop Drift Pressure Metrics

- passed: `True`
- loop_drift_pressure: `0.198`
- threshold: `0.25`
- stability_state: `green_with_repair_recommendation`
- recommended_action: `repair_pressure_findings_before_release_seal`
- pressure_hash: `a41a17c724d43ad73f36926b63a6ca072007d666684efe6da6497f36378147ce`

## Components

| Metric | Value |
|---|---:|
| `memory_action_drift` | `0.0` |
| `rehydration_gap_count` | `0` |
| `rehydration_gap_pressure` | `0.0` |
| `registry_status_drift` | `1.0` |
| `public_surface_delta` | `0.0` |
| `validator_expectation_drift` | `0.2` |
| `non_claim_lock_drift` | `0.0` |
| `report_surface_lag` | `0.25` |

## Findings

- `validation_failures:runtime_decision`

## Primary Lock

No green loop is considered stable if drift pressure exceeds the declared threshold without downgrade, warning, or repair recommendation.

## Non-Claim Lock

Loop drift pressure metrics are repository-bound and do not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.
