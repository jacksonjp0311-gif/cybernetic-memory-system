from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]


REQUIRED_LAYER_PATHS = {
    "root_readme": ["README.md"],
    "mini_readmes": [
        "configs/alignment/README.md",
        "src/cms/alignment/README.md",
        "scripts/alignment/README.md",
        "outputs/alignment/README.md",
        "reports/alignment/README.md",
        "configs/feedback/README.md",
        "src/cms/feedback/README.md",
        "scripts/feedback/README.md",
        "outputs/feedback/README.md",
        "reports/feedback/README.md",
    ],
    "route_maps": [
        "rcc/nexus/route_map.json",
        "rcc/nexus/task_routing_matrix.md",
        "docs/context/repository_context_index.json",
        "docs/context/rcc_nexus_index.json",
    ],
    "validators": [
        "scripts/validation/validate_reflective_git_geometry_v0_3.py",
        "scripts/validation/validate_feedback_lifecycle_v0_3b.py",
        "scripts/validation/validate_surface_alignment_v0_3b2.py",
        "scripts/validation/validate_multilevel_alignment_v0_3b2.py",
        "scripts/validation/validate_public_sync_v0_2b3.py",
    ],
    "reports": [
        "reports/geometry/latest_reflective_git_geometry_validation.json",
        "reports/feedback/latest_feedback_lifecycle_validation.json",
        "reports/surface_alignment/latest_surface_alignment_report.json",
        "reports/public_sync/latest_public_sync_report.json",
        "outputs/release/latest_release_readiness.md",
    ],
    "reflective_git_geometry": [
        "outputs/geometry/latest_reflective_git_geometry.json",
        "reports/geometry/latest_reflective_git_geometry.json",
    ],
    "feedback_lifecycle": [
        "outputs/feedback/latest_feedback_lifecycle_report.json",
        "reports/feedback/latest_feedback_lifecycle_report.json",
    ],
    "version_registry": [
        "outputs/version_registry/cms_version_registry.json",
    ],
    "public_sync": [
        "reports/public_sync/latest_public_sync_report.json",
    ],
    "release_seal": [
        "docs/release_seals/cms_sa_v0_3b2_release_seal.md",
        "outputs/release_seals/cms_sa_v0_3b2_release_seal.md",
    ],
}


def load_json(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def exists(relative: str) -> bool:
    return (ROOT / relative).exists()


def current_version(registry: dict[str, Any]) -> str:
    for key in ("current_version", "latest_version", "version"):
        value = registry.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    versions = registry.get("versions")
    if isinstance(versions, list) and versions:
        last = versions[-1]
        if isinstance(last, dict) and isinstance(last.get("version"), str):
            return last["version"]
    return "unknown"


def all_geometry_files(geometry: dict[str, Any]) -> set[str]:
    files: set[str] = set()
    for node in geometry.get("nodes", []):
        for path in node.get("changed_files", []):
            files.add(str(path).replace("\\", "/"))
    return files


def all_geometry_validators(geometry: dict[str, Any]) -> set[str]:
    files: set[str] = set()
    for node in geometry.get("nodes", []):
        for path in node.get("validator_reports_touched", []):
            files.add(str(path).replace("\\", "/"))
    return files


def bind_feedback_item(item: dict[str, Any], geometry_files: set[str], geometry_validators: set[str]) -> dict[str, Any]:
    route = item.get("route", {})
    route_files = [str(p).replace("\\", "/") for p in route.get("files", [])]
    validators = [str(p).replace("\\", "/") for p in item.get("validator_binding", [])]
    evidence = [str(p).replace("\\", "/") for p in item.get("evidence", [])]

    route_files_existing = [p for p in route_files if exists(p)]
    validators_existing = []
    for command in validators:
        # Validator bindings may include full commands. Extract script-ish tokens.
        parts = command.split()
        matched = False
        for part in parts:
            normalized = part.replace("\\", "/")
            if normalized.endswith(".py") and exists(normalized):
                validators_existing.append(normalized)
                matched = True
        if not matched and exists(command):
            validators_existing.append(command)

    evidence_existing = [p for p in evidence if exists(p)]
    geometry_hits = sorted((set(route_files) | set(validators_existing)) & (geometry_files | geometry_validators))

    observables = {
        "route_present": bool(route.get("shell") and route.get("meridian") and route.get("sector")),
        "route_files_exist": len(route_files_existing) == len(route_files) and len(route_files) > 0,
        "validator_binding_exists": len(validators_existing) > 0,
        "evidence_exists": len(evidence_existing) > 0,
        "geometry_binding_present": len(geometry_hits) > 0,
        "classification_present": bool(item.get("classification")),
        "lifecycle_state_present": bool(item.get("lifecycle_state")),
        "downgrade_path_present": bool(item.get("downgrade_path")),
        "falsification_present": bool(item.get("falsification_condition")),
        "non_claim_lock_present": bool(item.get("non_claim_lock")),
    }
    score = sum(1 for value in observables.values() if value) / len(observables)

    return {
        "id": item.get("id"),
        "classification": item.get("classification"),
        "lifecycle_state": item.get("lifecycle_state"),
        "route": route,
        "route_files": route_files,
        "route_files_existing": route_files_existing,
        "validators_existing": sorted(set(validators_existing)),
        "evidence_existing": evidence_existing,
        "geometry_hits": geometry_hits,
        "observables": observables,
        "alignment_score": score,
        "aligned": score == 1.0,
    }


def build_multilevel_alignment_report() -> dict[str, Any]:
    registry = load_json("outputs/version_registry/cms_version_registry.json")
    version = current_version(registry)
    readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace") if exists("README.md") else ""
    public_sync = load_json("reports/public_sync/latest_public_sync_report.json")
    geometry = load_json("outputs/geometry/latest_reflective_git_geometry.json")
    feedback = load_json("outputs/feedback/latest_feedback_lifecycle_report.json")

    layer_results: dict[str, Any] = {}
    for layer, paths in REQUIRED_LAYER_PATHS.items():
        missing = [path for path in paths if not exists(path)]
        layer_results[layer] = {
            "required_paths": paths,
            "missing_paths": missing,
            "passed": len(missing) == 0,
        }

    geometry_files = all_geometry_files(geometry)
    geometry_validators = all_geometry_validators(geometry)
    feedback_bindings = [
        bind_feedback_item(item, geometry_files, geometry_validators)
        for item in feedback.get("items", [])
    ]

    binding_failures = [
        binding["id"]
        for binding in feedback_bindings
        if not binding["aligned"]
    ]

    version_checks = {
        "registry_current_version": version,
        "readme_contains_current_version": version != "unknown" and version in readme,
        "public_sync_report_present": bool(public_sync),
        "public_sync_report_last_passed": public_sync.get("passed") is True,
        "geometry_registry_version_matches": geometry.get("current_registry_version") == version,
        "feedback_report_present": feedback.get("schema") == "CMS-SA-v0.3b-feedback-lifecycle-report",
    }

    findings: list[str] = []
    for layer, result in layer_results.items():
        if not result["passed"]:
            findings.append(f"layer_missing:{layer}:{','.join(result['missing_paths'])}")
    for item_id in binding_failures:
        findings.append(f"feedback_binding_failed:{item_id}")
    for key, value in version_checks.items():
        if key != "registry_current_version" and value is not True:
            findings.append(f"version_check_failed:{key}")

    return {
        "schema": "CMS-SA-v0.3b2a2-multilevel-alignment-report",
        "version": "v0.3b2a2",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "current_registry_version": version,
        "layers": layer_results,
        "feedback_bindings": feedback_bindings,
        "version_checks": version_checks,
        "passed": len(findings) == 0,
        "findings": findings,
        "feedback_items_checked": len(feedback_bindings),
        "feedback_items_aligned": sum(1 for binding in feedback_bindings if binding["aligned"]),
        "core_rule": "No feedback item is valid unless it can be located in repository geometry and tied to evidence, validators, and current public surfaces.",
        "api_boundary": "API remains inactive; this is internal runtime alignment only.",
        "temporal_boundary": "Public sync registry/tag agreement is validated after commit/tag/push by the public-sync validator; multi-level alignment requires the public-sync report surface to exist but does not require it to already contain the new version before release.",
        "non_claim_lock": "Multi-level alignment improves repository-bound cybernetic runtime coherence. It does not prove code correctness, truth, AGI, consciousness, production readiness, security, external validation, or real-world correctness.",
    }


def report_to_markdown(report: dict[str, Any]) -> str:
    rows = [
        "# CMS-SA v0.3b2a2 Multi-Level Alignment Report",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| schema | `{report['schema']}` |",
        f"| version | `{report['version']}` |",
        f"| passed | `{str(report['passed']).lower()}` |",
        f"| current registry version | `{report['current_registry_version']}` |",
        f"| feedback items checked | `{report['feedback_items_checked']}` |",
        f"| feedback items aligned | `{report['feedback_items_aligned']}` |",
        "",
        "## Layer Results",
        "",
        "| Layer | Passed | Missing paths |",
        "|---|---|---|",
    ]
    for layer, result in report["layers"].items():
        missing = ", ".join(result["missing_paths"]) if result["missing_paths"] else ""
        rows.append(f"| `{layer}` | `{str(result['passed']).lower()}` | {missing} |")

    rows.extend([
        "",
        "## Feedback Bindings",
        "",
        "| ID | Class | State | Score | Geometry hits | Aligned |",
        "|---|---|---|---:|---|---|",
    ])
    for binding in report["feedback_bindings"]:
        hits = ", ".join(binding["geometry_hits"])
        rows.append(
            f"| `{binding['id']}` | `{binding['classification']}` | `{binding['lifecycle_state']}` | `{binding['alignment_score']}` | {hits} | `{str(binding['aligned']).lower()}` |"
        )

    rows.extend([
        "",
        "## Core Rule",
        "",
        report["core_rule"],
        "",
        "## API Boundary",
        "",
        report["api_boundary"],
        "",
        "## Temporal Boundary",
        "",
        report.get("temporal_boundary", ""),
        "",
        "## Non-claim Lock",
        "",
        report["non_claim_lock"],
        "",
    ])
    return "\n".join(rows)


def write_multilevel_alignment_report() -> dict[str, Any]:
    report = build_multilevel_alignment_report()
    out_json = ROOT / "outputs" / "alignment" / "latest_multilevel_alignment_report.json"
    report_json = ROOT / "reports" / "alignment" / "latest_multilevel_alignment_report.json"
    report_md = ROOT / "reports" / "alignment" / "latest_multilevel_alignment_report.md"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    report_json.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, indent=2) + "\n"
    out_json.write_text(text, encoding="utf-8")
    report_json.write_text(text, encoding="utf-8")
    report_md.write_text(report_to_markdown(report), encoding="utf-8")
    return report


if __name__ == "__main__":
    print(json.dumps(write_multilevel_alignment_report(), indent=2))