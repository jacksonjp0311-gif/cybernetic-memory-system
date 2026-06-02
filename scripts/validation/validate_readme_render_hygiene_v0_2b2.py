from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
text = README.read_text(encoding="utf-8", errors="replace") if README.exists() else ""

errors = []

required_badges = [
    "CMS--SA-v0.2b2",
    "RCC--N-passing",
    "architecture-passing",
    "lineage-recorded",
    "README%20audit-passing",
    "directory%20box-passing",
    "render%20hygiene-passing",
    "K__CMS-1.0",
    "D__CMS-0.0",
    "non--claim--locks-active",
]

for badge in required_badges:
    if badge not in text:
        errors.append(f"missing_badge:{badge}")

for stale in [
    "CMS--SA-v0.1.2",
    "RCC--N-scaffolded",
    "README%20audit-local--ready",
    "Current checkpoint | CMS-SA v0.2a",
    "Current checkpoint CMS-SA v0.2a",
]:
    if stale in text:
        errors.append(f"stale_status:{stale}")

# Reject ASCII control characters except newline/carriage-return.
bad_controls = []
for idx, ch in enumerate(text):
    code = ord(ch)
    if code < 32 and ch not in ("\n", "\r"):
        bad_controls.append({"index": idx, "ord": code})
if bad_controls:
    errors.append(f"control_characters:{len(bad_controls)}")

# Reject common mojibake / PowerShell escape residues observed in v0.2b1.
bad_fragments = [
    "`\text",
    "`\tpowershell",
    "`\text",
    "`\t",
    "\x0b",
    "\x07",
    "\x0c",
    "\x08",
    "\x1b",
    "\ncc/nexus",
    "\neports/",
    "\nuntime",
    "\nelease",
    "source, \x0balidation",
    "$GitHead",
    "$MetricPassed",
    "$ReadmePassed",
    "$RccPassed",
    "$RuntimePassed",
    "$Kcms",
    "$Dcms",
    "$Class",
    "$ReleaseAllowed",
]

for frag in bad_fragments:
    if frag in text:
        printable = frag.encode("unicode_escape").decode("ascii")
        errors.append(f"bad_fragment:{printable}")

required_clean_paths = [
    "`rcc/nexus/route_map.json`",
    "`rcc/nexus/task_routing_matrix.md`",
    "`reports/release/`",
    "`reports/render_hygiene/`",
    "`tests/`",
    "`src/cms/`",
]

for path in required_clean_paths:
    if path not in text:
        errors.append(f"missing_clean_path:{path}")

required_sections = [
    "## Human Director Box",
    "## Current Public Metrics",
    "## Quick Start",
    "## PART I - Human README",
    "## PART II - RCC Nexus README",
    "## PART III - AI Agent README",
    "## README + Mini Repo Audit Map",
    "## AI Failure Learning Ledger",
    "## Agent Geometry Layer",
    "## Process Alignment Layer",
    "## AI Rule - Directory Box and Mini README Synchronization",
    "## Full Directory Box",
]

for section in required_sections:
    if section not in text:
        errors.append(f"missing_section:{section}")

passed = not errors

report = {
    "schema": "CMS-SA-v0.2b2-readme-render-hygiene",
    "passed": passed,
    "errors": len(errors),
    "findings": errors,
    "checked_badges": len(required_badges),
    "non_claim_lock": "README render hygiene improves readability and traceability but does not prove runtime correctness."
}

out_json = ROOT / "reports" / "render_hygiene" / "latest_readme_render_hygiene.json"
out_md = ROOT / "reports" / "render_hygiene" / "latest_readme_render_hygiene.md"
out_json.parent.mkdir(parents=True, exist_ok=True)
out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
out_md.write_text(
    "# CMS-SA v0.2b2 README Render Hygiene\n\n"
    f"- passed: `{passed}`\n"
    f"- errors: `{len(errors)}`\n"
    f"- checked_badges: `{len(required_badges)}`\n\n"
    "## Findings\n\n"
    + ("\n".join(f"- `{e}`" for e in errors) if errors else "- none\n")
    + "\n\nNon-claim lock: render hygiene is not runtime correctness.\n",
    encoding="utf-8",
)

print(json.dumps(report, indent=2))
raise SystemExit(0 if passed else 1)