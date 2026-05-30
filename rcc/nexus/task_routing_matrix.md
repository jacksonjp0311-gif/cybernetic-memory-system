# CMS Task Routing Matrix

| Task | Read first | Validate |
|---|---|---|
| Runtime patch | `src/cms/core/README.md`, `src/cms/core/runtime.py` | `python -m py_compile src/cms/core/runtime.py` |
| CLI patch | `src/cms/cli.py` | `python -m cms cycle --repo . --profile CMS-Core` |
| Architecture patch | `docs/architecture/` | README/RCC review |
| RCC patch | `rcc/nexus/` | `python scripts/validate_release.py` |
| README patch | `README.md`, `AGENTS.md` | surface alignment review |
| Memory patch | `src/cms/memory/` | memory promotion tests |
| Release patch | `outputs/release/` | `python scripts/validate_release.py` |