from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
text = README.read_text(encoding="utf-8", errors="replace") if README.exists() else ""
errors = []
required = ["CMS--SA-v0.2b3","RCC--N-passing","architecture-passing","README%20audit-passing","directory%20box-passing","render%20hygiene-passing","markdown%20structure-passing","public%20sync-local--guard","K__CMS-1.0","D__CMS-0.0","non--claim--locks-active"]
for b in required:
    if b not in text: errors.append(f"missing_badge:{b}")
for stale in ["CMS--SA-v0.1.2","RCC--N-scaffolded","README%20audit-local--ready","Current checkpoint | CMS-SA v0.2a"]:
    if stale in text: errors.append(f"stale_status:{stale}")
for idx,ch in enumerate(text):
    if ord(ch)<32 and ch not in ("\n","\r"): errors.append(f"control_character:{idx}:{ord(ch)}"); break
for frag in ["\ncc/nexus","\neports/","$GitHead","$Kcms","$Dcms"]:
    if frag in text: errors.append(f"bad_fragment:{frag.encode('unicode_escape').decode('ascii')}")
for sec in ["## Repository Layers","## Historical Report Archive","### Gap Classes the AI Must Detect","## Law of Sufficient Form"]:
    if sec not in text: errors.append(f"missing_section:{sec}")
passed = not errors
report = {"schema":"CMS-SA-v0.2b3-readme-render-hygiene","passed":passed,"errors":len(errors),"findings":errors,"checked_badges":len(required),"non_claim_lock":"README render hygiene is not runtime correctness."}
out_json = ROOT/"reports"/"render_hygiene"/"latest_readme_render_hygiene.json"
out_md = ROOT/"reports"/"render_hygiene"/"latest_readme_render_hygiene.md"
out_json.parent.mkdir(parents=True, exist_ok=True)
out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
out_md.write_text("# CMS-SA v0.2b3 README Render Hygiene\n\n"+f"- passed: `{passed}`\n- errors: `{len(errors)}`\n\n"+"## Findings\n\n"+("\n".join(f"- `{e}`" for e in errors) if errors else "- none\n")+"\n", encoding="utf-8")
print(json.dumps(report, indent=2))
raise SystemExit(0 if passed else 1)