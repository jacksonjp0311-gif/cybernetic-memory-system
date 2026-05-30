# CMS Roadmap

## Current

CMS-SA v0.2b — Public Format Alignment and Directory Box Lock.

## Current Lock State

```text
runtime geometry      = locked
metric geometry       = locked
drift geometry        = locked
evidence geometry     = locked
version geometry      = locked
RCC-N navigation      = locked
README/audit grammar  = locked
directory box         = locked by v0.2b
public process rules  = locked by v0.2b
```

## Next

CMS-SA v0.3 — Feedback Quality and Lifecycle Engine.

### v0.3 Goal

Turn drift findings into typed feedback items with quality scores and lifecycle
states.

Planned v0.3 surfaces:

1. feedback item model,
2. feedback generator,
3. feedback quality scorer,
4. lifecycle state machine,
5. orphan feedback detector,
6. feedback report writer,
7. tests and validation command.

## Later

| Version | Target |
|---|---|
| v0.3 | Feedback quality + lifecycle engine |
| v0.4 | Memory promotion + correction ledger |
| v0.5 | README/RCC/public drift guard |
| v0.6 | Baseline utility harness + dashboards |
| v1.0 | Stable CMS runtime |