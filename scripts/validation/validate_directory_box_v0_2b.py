from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
cands = [ROOT/"docs"/"directory"/"cms_full_directory_box_v0_2b3.json", ROOT/"docs"/"directory"/"cms_full_directory_box_v0_2b2.json"]
manifest_path = next((p for p in cands if p.exists()), cands[0])
readme = README.read_text(encoding="utf-8", errors="replace") if README.exists() else ""
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
required = ["## Human Director Box","## Current Public Metrics","## Repository Layers","## Historical Report Archive","## Agent Geometry Layer","## Process Alignment Layer","## Law of Sufficient Form","## AI Rule - Directory Box and Mini README Synchronization","## Full Directory Box"]
missing_anchors = [a for a in required if a not in readme]
missing_rows = [row["path"] for row in manifest.get("rows", []) if f"`{row['path']}`" not in readme]
dupes, seen = [], set()
for row in manifest.get("rows", []):
    p=row["path"]
    if p in seen: dupes.append(p)
    seen.add(p)
missing_disk = [row["path"] for row in manifest.get("rows", []) if not (ROOT/row["path"].rstrip("/")).exists()]
passed = not missing_anchors and not missing_rows and not dupes and not missing_disk
report = {"schema":"CMS-SA-v0.2b3-directory-box-validation","passed":passed,"errors":len(missing_anchors)+len(missing_rows)+len(dupes)+len(missing_disk),"manifest":str(manifest_path.relative_to(ROOT)).replace("\\","/"),"missing_anchors":missing_anchors,"missing_directory_rows":missing_rows,"duplicate_rows":dupes,"missing_paths_on_disk":missing_disk,"row_count":len(manifest.get("rows", [])),"non_claim_lock":"Directory box validation is navigation validation, not code correctness."}
out_json = ROOT/"reports"/"directory"/"latest_directory_box_validation.json"
out_md = ROOT/"reports"/"directory"/"latest_directory_box_validation.md"
out_json.parent.mkdir(parents=True, exist_ok=True)
out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
out_md.write_text("# CMS-SA v0.2b3 Directory Box Validation\n\n"+f"- passed: `{passed}`\n- errors: `{report['errors']}`\n- row_count: `{report['row_count']}`\n\n", encoding="utf-8")
print(json.dumps(report, indent=2))
raise SystemExit(0 if passed else 1)