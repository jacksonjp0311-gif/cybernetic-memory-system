# CMS Validation Surface

Run from repo root:

```powershell
$env:PYTHONPATH = ".\src"
python -m py_compile src/cms/core/runtime.py
python -c "from cms.core.runtime import CMSRuntime; print('CMSRuntime import OK')"
python scripts/rcc/check_rcc_nexus.py
python scripts/rcc/audit_readme_surface.py
python scripts/validation/validate_architecture_contracts.py
python scripts/validate_release.py
python -m unittest discover -s tests
```

Claim boundary:

Validation is local repository-bound evidence. It does not prove truth, AGI,
consciousness, production readiness, code correctness, or external validation.