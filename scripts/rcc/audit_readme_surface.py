from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]

required_root_tokens = [
    "Current checkpoint: **CMS-SA v0.1.2",
    "PART I - Human README",
    "PART II - RCC Nexus README",
    "PART III - AI Agent README",
    "README + Mini Repo Audit Map",
    "AI Failure Learning Ledger",
    "MINI_README_UPDATE_RULE_START",
]

readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
missing_tokens = [t for t in required_root_tokens if t not in readme]

mini_readmes = list(ROOT.rglob("README.md"))
mini_missing_rule = []
for p in mini_readmes:
    rel = str(p.relative_to(ROOT)).replace("\\", "/")
    if rel == "README.md":
        continue
    text = p.read_text(encoding="utf-8", errors="replace")
    if "MINI_README_UPDATE_RULE_START" not in text:
        mini_missing_rule.append(rel)

passed = not missing_tokens and not mini_missing_rule
report = {
    "schema": "CMS-SA-v0.1.2-readme-mini-repo-audit",
    "passed": passed,
    "errors": len(missing_tokens) + len(mini_missing_rule),
    "warnings": 0,
    "missing_root_tokens": missing_tokens,
    "mini_readmes_missing_update_rule": mini_missing_rule,
    "non_claim_lock": "README audits improve context alignment but do not prove runtime correctness."
}

out_json = ROOT / "reports" / "readme" / "latest_readme_mini_repo_audit.json"
out_md = ROOT / "reports" / "readme" / "latest_readme_mini_repo_audit.md"
out_json.parent.mkdir(parents=True, exist_ok=True)
out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
out_md.write_text(
    "# CMS README / Mini Repo Audit\n\n"
    f"- passed: `{passed}`\n"
    f"- errors: `{report['errors']}`\n"
    f"- warnings: `0`\n"
    f"- mini READMEs scanned: `{len(mini_readmes)}`\n\n"
    "Non-claim lock: README audit is not runtime correctness.\n",
    encoding="utf-8",
)

print(json.dumps(report, indent=2))
raise SystemExit(0 if passed else 1)