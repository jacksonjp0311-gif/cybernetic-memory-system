from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
from typing import Any


@dataclass
class CMSRunResult:
    repository: str
    profile: str
    k_cms: float
    d_cms: float
    a_cms: float
    release_allowed: bool
    feedback_items: int
    orphan_feedback: int
    promoted_memory: int
    release_hold_reasons: list[str]
    artifacts: str


class CMSRuntime:
    """Minimal CMS-SA v0.1 runtime scaffold.

    This is intentionally conservative. It emits architecture-aligned artifacts
    without claiming code correctness, truth, consciousness, AGI, or external
    validation.
    """

    def __init__(self, repo: str | Path = ".", profile: str = "CMS-Core") -> None:
        self.repo = Path(repo).resolve()
        self.profile = profile
        self.outputs = self.repo / "outputs"

    def _write_json(self, path: Path, payload: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    def _write_md(self, path: Path, text: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _git_head(self) -> str | None:
        try:
            return subprocess.check_output(
                ["git", "rev-parse", "HEAD"],
                cwd=self.repo,
                stderr=subprocess.DEVNULL,
                text=True,
            ).strip()
        except Exception:
            return None

    def observe_repository(self) -> dict[str, Any]:
        files = [str(p.relative_to(self.repo)) for p in self.repo.rglob("*") if p.is_file()]
        state = {
            "schema": "CMS-SA-v0.1-observation-manifest",
            "repository": self.repo.name,
            "profile": self.profile,
            "observed_at": datetime.now(timezone.utc).isoformat(),
            "git_head": self._git_head(),
            "file_count": len(files),
            "required_surfaces": {
                "README.md": (self.repo / "README.md").exists(),
                "README_90_SECONDS.md": (self.repo / "README_90_SECONDS.md").exists(),
                "AGENTS.md": (self.repo / "AGENTS.md").exists(),
                "rcc/nexus/route_map.json": (self.repo / "rcc/nexus/route_map.json").exists(),
                "docs/architecture/cms_sa_v0_1_software_architecture.tex": (
                    self.repo / "docs/architecture/cms_sa_v0_1_software_architecture.tex"
                ).exists(),
            },
        }
        self._write_json(self.outputs / "state" / "latest_cms_state.json", state)
        return state

    def compute_drift(self, state: dict[str, Any]) -> dict[str, Any]:
        missing = [k for k, v in state["required_surfaces"].items() if not v]
        drift_terms = {
            "goal_drift": 0.0,
            "lock_drift": 0.0,
            "route_drift": 1.0 if "rcc/nexus/route_map.json" in missing else 0.0,
            "validation_drift": 0.0,
            "memory_drift": 0.0,
            "correction_drift": 0.0,
            "narrative_surface_drift": 1.0 if any(x in missing for x in ["README.md", "README_90_SECONDS.md", "AGENTS.md"]) else 0.0,
            "public_surface_drift": 0.0,
        }
        d_cms = sum(drift_terms.values()) / len(drift_terms)
        report = {
            "schema": "CMS-SA-v0.1-drift-report",
            "drift": drift_terms,
            "D_CMS": d_cms,
            "K_CMS": 1.0 - d_cms,
            "findings": missing,
        }
        self._write_json(self.outputs / "drift" / "latest_drift_report.json", report)
        return report

    def generate_feedback(self, drift: dict[str, Any]) -> dict[str, Any]:
        items = []
        for finding in drift.get("findings", []):
            items.append({
                "feedback_id": f"FB-{len(items)+1:03d}",
                "diagnosis": f"Missing required surface: {finding}",
                "recommendation": f"Create or repair {finding}.",
                "severity": "repair",
                "target_surface": finding,
                "evidence": ["outputs/drift/latest_drift_report.json"],
                "next_action": "repair_surface",
                "boundary": "surface alignment is not code correctness",
                "quality": {
                    "actionability": 1.0,
                    "evidence_linkage": 1.0,
                    "target_specificity": 1.0,
                    "boundary_awareness": 1.0,
                    "validation_binding": 1.0,
                    "routing_value": 1.0,
                    "Q_F": 1.0,
                },
                "lifecycle": {
                    "state": "emitted",
                    "resolution_target": "surface_repair",
                    "history": ["emitted"],
                },
            })
        report = {
            "schema": "CMS-SA-v0.1-feedback-report",
            "items": items,
            "orphan_feedback": 0,
        }
        self._write_json(self.outputs / "feedback" / "latest_feedback_report.json", report)
        return report

    def validate_release(self, state: dict[str, Any], drift: dict[str, Any], feedback: dict[str, Any]) -> dict[str, Any]:
        release_allowed = drift["D_CMS"] == 0
        reasons = drift.get("findings", [])
        report = {
            "schema": "CMS-SA-v0.1-validation-report",
            "release_allowed": release_allowed,
            "release_hold_reasons": reasons,
            "checks": {
                "required_surfaces_present": len(reasons) == 0,
                "feedback_lifecycle_present": True,
                "non_claim_locks_present": True,
            },
        }
        self._write_json(self.outputs / "validation" / "latest_validation_report.json", report)
        self._write_md(
            self.outputs / "release" / "latest_release_readiness.md",
            "# CMS Release Readiness\n\n"
            f"- Release allowed: `{release_allowed}`\n"
            f"- Release hold reasons: `{reasons}`\n"
            "- Non-claim lock: validation is repository-bound.\n",
        )
        return report

    def run_cycle(self) -> CMSRunResult:
        state = self.observe_repository()
        drift = self.compute_drift(state)
        feedback = self.generate_feedback(drift)
        validation = self.validate_release(state, drift, feedback)

        a_cms = 1.0 if validation["release_allowed"] else max(0.0, 1.0 - drift["D_CMS"])
        result = CMSRunResult(
            repository=self.repo.name,
            profile=self.profile,
            k_cms=drift["K_CMS"],
            d_cms=drift["D_CMS"],
            a_cms=a_cms,
            release_allowed=validation["release_allowed"],
            feedback_items=len(feedback["items"]),
            orphan_feedback=feedback["orphan_feedback"],
            promoted_memory=0,
            release_hold_reasons=validation["release_hold_reasons"],
            artifacts=str(self.outputs),
        )
        self._write_json(self.outputs / "evidence" / "latest_evidence_package.json", asdict(result))
        self._write_json(self.outputs / "runs" / "latest" / "cms_run_result.json", asdict(result))
        return result