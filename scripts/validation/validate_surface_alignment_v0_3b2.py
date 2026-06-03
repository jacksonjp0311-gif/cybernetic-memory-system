from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
REGISTRY = ROOT / "outputs" / "version_registry" / "cms_version_registry.json"
REPORT_JSON = ROOT / "reports" / "surface_alignment" / "latest_surface_alignment_report.json"
REPORT_MD = ROOT / "reports" / "surface_alignment" / "latest_surface_alignment_report.md"

CURRENT_VERSION = "v0.4.0"
PREVIOUS_VERSION = "v0.3b5"

ROOT_REQUIRED_TOKENS = [
    "CMS--SA-v0.4.0-blue",
    "Current checkpoint: **CMS-SA v0.4.0 - Cybernetic Memory Loop Genesis**",
    "| Current checkpoint | CMS-SA v0.4.0 |",
    "| Previous seal | CMS-SA v0.3b5 |",
    "Multi-level alignment report",
    "reports/alignment/latest_multilevel_alignment_report.md",
    "reports/alignment/latest_multilevel_alignment_validation.md",
    "scripts/alignment/emit_multilevel_alignment_v0_3b2.py",
    "scripts/validation/validate_multilevel_alignment_v0_3b2.py",
    "scripts/validation/validate_surface_alignment_v0_3b2.py",
    "CMS-RCC-N-v0.4.0 / 180 days",
    "Pre-API Transmission Constraint Box",
    "API is not active in v0.4.0",
    "CMS-L-019",
    "CMS-L-026",
    "Negative control harness",
    "scripts/controls/emit_negative_control_harness_v0_3b4.py",
    "scripts/validation/validate_negative_control_harness_v0_3b4.py",
    "Memory promotion kernel",
    "scripts/memory/emit_memory_promotion_v0_3b5.py",
    "scripts/validation/validate_memory_promotion_v0_3b5.py",
    "CMS-L-028",
]

STALE_FORBIDDEN_TOKENS = [
    "CMS--SA-v0.3b11",
    "Current checkpoint: **CMS-SA v0.3b1a - Surface Alignment Repair and File-Run Guard**",
    "Current checkpoint: **CMS-SA v0.3b1 - README and Mini README Reflective Feedback Alignment Lock**",
]

MINI_README_EXPECTED = {
    "configs/alignment/README.md": ["CMS-RCC-N-v0.4.0", "Multi-Level Alignment Contracts"],
    "src/cms/alignment/README.md": ["CMS-RCC-N-v0.4.0", "Multi-Level Alignment Runtime"],
    "scripts/alignment/README.md": ["CMS-RCC-N-v0.4.0", "Alignment Emitters"],
    "outputs/alignment/README.md": ["CMS-RCC-N-v0.4.0", "Alignment Outputs"],
    "reports/alignment/README.md": ["CMS-RCC-N-v0.4.0", "Alignment Reports"],
    "configs/controls/README.md": ["CMS-RCC-N-v0.4.0", "Control Contracts"],
    "src/cms/controls/README.md": ["CMS-RCC-N-v0.4.0", "Control Runtime"],
    "scripts/controls/README.md": ["CMS-RCC-N-v0.4.0", "Control Emitters"],
    "outputs/controls/README.md": ["CMS-RCC-N-v0.4.0", "Control Outputs"],
    "reports/controls/README.md": ["CMS-RCC-N-v0.4.0", "Control Reports"],
    "configs/memory/README.md": ["CMS-RCC-N-v0.4.0", "Memory Contracts"],
    "src/cms/memory/README.md": ["CMS-RCC-N-v0.4.0", "CMS Memory Runtime"],
    "scripts/memory/README.md": ["CMS-RCC-N-v0.4.0", "Memory Emitters"],
    "outputs/memory/README.md": ["CMS-RCC-N-v0.4.0", "Memory Outputs"],
    "reports/memory/README.md": ["CMS-RCC-N-v0.4.0", "Memory Reports"],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def main() -> int:
    findings: list[str] = []
    readme = read(README)

    for token in ROOT_REQUIRED_TOKENS:
        if token not in readme:
            findings.append(f"root_missing:{token}")

    for token in STALE_FORBIDDEN_TOKENS:
        if token in readme:
            findings.append(f"root_stale_token_present:{token}")

    if not REGISTRY.exists():
        findings.append("missing_version_registry")
        registry = {}
    else:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    if registry.get("current_version") != CURRENT_VERSION:
        findings.append(f"registry_current_version_mismatch:{registry.get('current_version')}")

    if registry.get("latest_version") != CURRENT_VERSION:
        findings.append(f"registry_latest_version_mismatch:{registry.get('latest_version')}")

    if CURRENT_VERSION not in str(registry.get("current_checkpoint", "")):
        findings.append("registry_current_checkpoint_mismatch")

    for relative, tokens in MINI_README_EXPECTED.items():
        text = read(ROOT / relative)
        if not text:
            findings.append(f"missing_mini_readme:{relative}")
            continue
        for token in tokens:
            if token not in text:
                findings.append(f"mini_readme_missing:{relative}:{token}")

    report = {
        "schema": "CMS-SA-v0.4.0-surface-alignment-validation",
        "passed": len(findings) == 0,
        "errors": len(findings),
        "warnings": 0,
        "findings": findings,
        "warning_findings": [],
        "current_version": CURRENT_VERSION,
        "previous_version": PREVIOUS_VERSION,
        "root_tokens_checked": len(ROOT_REQUIRED_TOKENS),
        "mini_readmes_checked": len(MINI_README_EXPECTED),
        "stale_tokens_checked": len(STALE_FORBIDDEN_TOKENS),
        "non_claim_lock": "Surface alignment validates README and mini README currentness only. It does not prove code correctness.",
    }

    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    md = [
        "# CMS-SA v0.4.0 Surface Alignment Validation",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| passed | `{str(report['passed']).lower()}` |",
        f"| errors | `{report['errors']}` |",
        f"| warnings | `0` |",
        f"| current version | `{CURRENT_VERSION}` |",
        f"| previous version | `{PREVIOUS_VERSION}` |",
        f"| root tokens checked | `{report['root_tokens_checked']}` |",
        f"| mini READMEs checked | `{report['mini_readmes_checked']}` |",
        f"| stale tokens checked | `{report['stale_tokens_checked']}` |",
        "",
        "Non-claim lock: surface alignment validates README and mini README currentness only. It does not prove code correctness.",
        "",
    ]
    if findings:
        md.extend(["## Findings", ""])
        md.extend(f"- `{finding}`" for finding in findings)
        md.append("")
    REPORT_MD.write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
