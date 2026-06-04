# CMS-SA v0.4.7 Authorized Apply Packet Schema and Diff Manifest

| Field | Value |
|---|---|
| passed | `true` |
| source pressure state | `warning` |
| source apply gate count | `3` |
| apply packet count | `3` |
| diff manifest count | `3` |
| target writes performed | `0` |
| api writes performed | `0` |
| git commits performed | `0` |
| git pushes performed | `0` |
| release tags created | `0` |
| manifest hash | `27ac517cac12026fc458930ee5c5b78f5084cee0266753c9ddf63a45d554a8a8` |

## Primary Lock

No apply packet may authorize a repair unless it references a validated apply gate, includes a human authorization artifact, declares exact diff entries for every target write, binds rollback entries one-to-one with diff entries, preserves blocked actions, and passes pre-apply validation.

## Packets

### CMS-APPLY-PACKET-ce28b07cd7

- source apply gate: `CMS-APPLY-GATE-a6643e0259`
- packet state: `blocked_missing_human_authorization_packet`
- apply authority: `false`
- human authorization artifact present: `false`
- diff entries: `0`
- rollback entries: `0`
- rollback binds every diff: `true`
- target writes requested: ``

### CMS-APPLY-PACKET-60de55c00a

- source apply gate: `CMS-APPLY-GATE-465e02de46`
- packet state: `blocked_missing_human_authorization_packet`
- apply authority: `false`
- human authorization artifact present: `false`
- diff entries: `0`
- rollback entries: `0`
- rollback binds every diff: `true`
- target writes requested: ``

### CMS-APPLY-PACKET-889d035eec

- source apply gate: `CMS-APPLY-GATE-6319f003ce`
- packet state: `blocked_missing_human_authorization_packet`
- apply authority: `false`
- human authorization artifact present: `false`
- diff entries: `0`
- rollback entries: `0`
- rollback binds every diff: `true`
- target writes requested: ``

## Non-Claim Lock

Authorized apply packets and diff manifests are repository-bound authorization evidence and do not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, autonomous repair authority, or real-world correctness.

