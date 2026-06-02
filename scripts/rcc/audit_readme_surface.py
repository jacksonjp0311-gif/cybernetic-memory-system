from pathlib import Path
import json
import re
ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
readme = README.read_text(encoding="utf-8", errors="replace") if README.exists() else ""
required = ["PART I - Human README","PART II - RCC Nexus README","PART III - AI Agent README","README + Mini Repo Audit Map","AI Failure Learning Ledger","Human Director Box","Current Public Metrics","Repository Layers","Historical Report Archive","Gap Classes the AI Must Detect","Agent Geometry Layer","Process Alignment Layer","Law of Sufficient Form","AI Rule - Directory Box and Mini README Synchronization","Full Directory Box","README Structure, Public Sync Guard, and Tau Lesson Embedding","MINI_README_UPDATE_RULE_START","Markdown-structure rule","Public-sync rule"]
missing = []
if not re.search(r"Current checkpoint:\s*\*\*CMS-SA v0\.2b3[\s\-–—][^*]+\*\*", readme):
    missing.append("Current checkpoint: **CMS-SA v0.2b3 ...**")
for token in required:
    if token not in readme: missing.append(token)
mini_missing = []
for p in ROOT.rglob("README.md"):
    rel = str(p.relative_to(ROOT)).replace("\\","/")
    if rel == "README.md": continue
    text = p.read_text(encoding="utf-8", errors="replace")
    if "MINI_README_UPDATE_RULE_START" not in text: mini_missing.append(rel)
passed = not missing and not mini_missing
report = {"schema":"CMS-SA-v0.2b3-readme-mini-repo-audit","passed":passed,"errors":len(missing)+len(mini_missing),"warnings":0,"accepted_checkpoint_pattern":"CMS-SA v0.2b3","missing_root_tokens":missing,"mini_readmes_missing_update_rule":mini_missing,"non_claim_lock":"README audits improve context alignment but do not prove runtime correctness."}
out_json = ROOT/"reports"/"readme"/"latest_readme_mini_repo_audit.json"
out_md = ROOT/"reports"/"readme"/"latest_readme_mini_repo_audit.md"
out_json.parent.mkdir(parents=True, exist_ok=True)
out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
out_md.write_text("# CMS README / Mini Repo Audit\n\n"+f"- passed: `{passed}`\n- errors: `{report['errors']}`\n- warnings: `0`\n\n", encoding="utf-8")
print(json.dumps(report, indent=2))
raise SystemExit(0 if passed else 1)