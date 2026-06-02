from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "outputs" / "alignment" / "latest_multilevel_alignment_report.json"
REPORT_COPY = ROOT / "reports" / "alignment" / "latest_multilevel_alignment_report.json"
VALIDATION_JSON = ROOT / "reports" / "alignment" / "latest_multilevel_alignment_validation.json"
VALIDATION_MD = ROOT / "reports" / "alignment" / "latest_multilevel_alignment_validation.md"


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    findings: list[str] = []
    report = load_json(REPORT)
    report_copy = load_json(REPORT_COPY)

    if not report:
        findings.append("missing_multilevel_alignment_report")

    if report != report_copy:
        findings.append("alignment_report_copy_mismatch")

    if report.get("schema") != "CMS-SA-v0.3b2a3-multilevel-alignment-report":
        findings.append("schema_mismatch")

    if report.get("version") != "v0.3b2a3":
        findings.append("version_mismatch")

    if report.get("passed") is not True:
        findings.append("alignment_report_not_passing")

    if report.get("current_registry_version") != "v0.3b2a3":
        findings.append(f"registry_version_mismatch:{report.get('current_registry_version')}")

    layers = report.get("layers", {})
    for layer_name in (
        "root_readme",
        "mini_readmes",
        "route_maps",
        "validators",
        "reports",
        "reflective_git_geometry",
        "feedback_lifecycle",
        "version_registry",
        "public_sync",
        "release_seal",
    ):
        layer = layers.get(layer_name)
        if not layer:
            findings.append(f"missing_layer:{layer_name}")
        elif layer.get("passed") is not True:
            findings.append(f"layer_not_passing:{layer_name}")

    bindings = report.get("feedback_bindings", [])
    if not bindings:
        findings.append("no_feedback_bindings")

    for binding in bindings:
        if binding.get("aligned") is not True:
            findings.append(f"feedback_not_aligned:{binding.get('id')}")
        if not binding.get("geometry_hits"):
            findings.append(f"feedback_missing_geometry_hits:{binding.get('id')}")
        if not binding.get("validators_existing"):
            findings.append(f"feedback_missing_validators:{binding.get('id')}")
        if not binding.get("evidence_existing"):
            findings.append(f"feedback_missing_evidence:{binding.get('id')}")

    version_checks = report.get("version_checks", {})
    for key in (
        "readme_contains_current_version",
        "public_sync_report_present",
        "public_sync_report_last_passed",
        "geometry_registry_version_matches",
        "feedback_report_present",
    ):
        if version_checks.get(key) is not True:
            findings.append(f"version_check_failed:{key}")

    validation = {
        "schema": "CMS-SA-v0.3b2a3-multilevel-alignment-validation",
        "passed": len(findings) == 0,
        "errors": len(findings),
        "warnings": 0,
        "findings": findings,
        "feedback_items_checked": report.get("feedback_items_checked", 0),
        "feedback_items_aligned": report.get("feedback_items_aligned", 0),
        "layer_count": len(layers),
        "non_claim_lock": "Multi-level alignment validation checks repository-bound alignment only. It does not prove code correctness.",
    }

    VALIDATION_JSON.parent.mkdir(parents=True, exist_ok=True)
    VALIDATION_JSON.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")

    md = [
        "# CMS-SA v0.3b2a3 Multi-Level Alignment Validation",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| passed | `{str(validation['passed']).lower()}` |",
        f"| errors | `{validation['errors']}` |",
        f"| warnings | `0` |",
        f"| feedback items checked | `{validation['feedback_items_checked']}` |",
        f"| feedback items aligned | `{validation['feedback_items_aligned']}` |",
        f"| layer count | `{validation['layer_count']}` |",
        "",
        "Non-claim lock: multi-level alignment validation checks repository-bound alignment only. It does not prove code correctness.",
        "",
    ]
    if findings:
        md.extend(["## Findings", ""])
        for finding in findings:
            md.append(f"- `{finding}`")
        md.append("")
    VALIDATION_MD.write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(validation, indent=2))
    return 0 if validation["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())