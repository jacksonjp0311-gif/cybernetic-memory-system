from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
REGISTRY = ROOT / "outputs" / "version_registry" / "cms_version_registry.json"

def run(cmd):
    try:
        return subprocess.check_output(cmd, cwd=ROOT, text=True, stderr=subprocess.STDOUT).strip()
    except Exception as exc:
        return f"ERROR:{exc}"

readme = README.read_text(encoding="utf-8", errors="replace") if README.exists() else ""
registry = json.loads(REGISTRY.read_text(encoding="utf-8")) if REGISTRY.exists() else {}
head = run(["git", "rev-parse", "HEAD"])
origin = run(["git", "rev-parse", "origin/main"])
short_head = run(["git", "rev-parse", "--short", "HEAD"])
tags = run(["git", "tag", "--list"])
errors, warnings = [], []

if head.startswith("ERROR"):
    errors.append("git_head_unavailable")
if origin.startswith("ERROR"):
    errors.append("origin_main_unavailable")
if not head.startswith("ERROR") and not origin.startswith("ERROR") and head != origin:
    errors.append("local_head_not_equal_origin_main")
if "CMS-SA v0.2b3" not in readme:
    errors.append("readme_missing_v0.2b3_checkpoint")
if registry.get("current_version") != "v0.2b3":
    errors.append(f"registry_current_version_mismatch:{registry.get('current_version')}")
if "CMS--SA-v0.2b3" not in readme:
    errors.append("badge_missing_v0.2b3")
for stale in ["CMS--SA-v0.1.2", "CMS-SA v0.2a", "CMS-SA v0.2b2 - README Render Hygiene and Badge Status Guard**  \nPrevious seal"]:
    if stale in readme:
        errors.append(f"stale_public_surface:{stale}")
if "v0.2b3" not in tags:
    warnings.append("tag_v0.2b3_not_created_yet")

passed = not errors
report = {
    "schema": "CMS-SA-v0.2b3-public-sync",
    "passed": passed,
    "errors": len(errors),
    "warnings": len(warnings),
    "findings": errors,
    "warning_findings": warnings,
    "head": head,
    "origin_main": origin,
    "short_head": short_head,
    "registry_current_version": registry.get("current_version"),
    "non_claim_lock": "Public sync validation checks repository state agreement but does not prove runtime correctness."
}
out_json = ROOT / "reports" / "public_sync" / "latest_public_sync_report.json"
out_md = ROOT / "reports" / "public_sync" / "latest_public_sync_report.md"
out_json.parent.mkdir(parents=True, exist_ok=True)
out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
out_md.write_text(
    "# CMS-SA v0.2b3 Public Sync Report\n\n"
    f"- passed: `{passed}`\n"
    f"- errors: `{len(errors)}`\n"
    f"- warnings: `{len(warnings)}`\n"
    f"- short_head: `{short_head}`\n"
    f"- registry_current_version: `{registry.get('current_version')}`\n\n"
    "## Findings\n\n"
    + ("\n".join(f"- `{e}`" for e in errors) if errors else "- none\n")
    + "\n\n## Warnings\n\n"
    + ("\n".join(f"- `{w}`" for w in warnings) if warnings else "- none\n")
    + "\n\nNon-claim lock: public sync validation is not runtime correctness.\n",
    encoding="utf-8",
)
print(json.dumps(report, indent=2))
raise SystemExit(0 if passed else 1)