# CMS-SA v0.4.3 Loop Repair Recommendation Validation

| Field | Value |
|---|---|
| passed | `true` |
| errors | `0` |
| recommendation count | `3` |
| pressure state | `warning` |
| dominant pressure source | `registry_status_drift` |
| dominant repair class | `REGISTRY_REPAIR` |
| loop drift pressure | `0.168` |

## Primary Lock

No repair recommendation may write, promote, or seal a change unless it declares pressure source, repair class, allowed action, blocked action, required validation, and non-claim boundary.

Non-claim lock: loop repair recommendation validation is repository-bound and does not prove code correctness.
