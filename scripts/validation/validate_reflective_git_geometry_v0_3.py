from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from cms.geometry.git_geometry import write_geometry  # noqa: E402


def main() -> int:
    findings: list[str] = []

    geometry = write_geometry(limit=12)

    if geometry.get("schema") != "CMS-SA-v0.3a-reflective-git-geometry":
        findings.append("schema_mismatch")

    if geometry.get("node_count", 0) < 1:
        findings.append("no_geometry_nodes")

    truth = geometry.get("release_truth", {})
    if truth.get("head_origin_match") is not True:
        findings.append("head_origin_mismatch")

    if truth.get("readme_checkpoint_present") is not True:
        findings.append("readme_checkpoint_missing")

    nodes = geometry.get("nodes", [])
    for index, node in enumerate(nodes):
        for key in ("commit_hash", "short_hash", "message", "changed_files", "surface_classes", "shells", "meridians", "sectors", "release_truth"):
            if key not in node:
                findings.append(f"node_{index}_missing_{key}")

    report = {
        "schema": "CMS-SA-v0.3a-reflective-git-geometry-validation",
        "passed": len(findings) == 0,
        "errors": len(findings),
        "warnings": 0,
        "findings": findings,
        "node_count": geometry.get("node_count", 0),
        "current_registry_version": geometry.get("current_registry_version"),
        "core_law_present": geometry.get("core_law") == "A commit is not only a change; it is a routed event in repository geometry.",
        "non_claim_lock": "Reflective Git geometry validation checks repository-route artifacts only. It does not prove runtime correctness."
    }

    out_json = ROOT / "reports" / "geometry" / "latest_reflective_git_geometry_validation.json"
    out_md = ROOT / "reports" / "geometry" / "latest_reflective_git_geometry_validation.md"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    md = [
        "# CMS-SA v0.3a Reflective Git Geometry Validation",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| passed | `{str(report['passed']).lower()}` |",
        f"| errors | `{report['errors']}` |",
        f"| warnings | `0` |",
        f"| node count | `{report['node_count']}` |",
        f"| current registry version | `{report['current_registry_version']}` |",
        f"| core law present | `{str(report['core_law_present']).lower()}` |",
        "",
        "Non-claim lock: reflective Git geometry validation checks repository-route artifacts only. It does not prove runtime correctness.",
        "",
    ]
    out_md.write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())