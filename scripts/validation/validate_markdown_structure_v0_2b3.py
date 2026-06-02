from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
text = README.read_text(encoding="utf-8", errors="replace") if README.exists() else ""
lines = text.splitlines()
errors = []

if len(lines) < 180:
    errors.append(f"line_count_too_low:{len(lines)}")

required_sections = [
    "# Cybernetic Memory System - Feedback-Governed Repository Memory Runtime",
    "## Current CMS Snapshot",
    "## Human Director Box",
    "## Current Public Metrics",
    "## Quick Start",
    "## Repository Layers",
    "## Historical Report Archive",
    "## PART I - Human README",
    "## PART II - RCC Nexus README",
    "## PART III - AI Agent README",
    "## README + Mini Repo Audit Map",
    "### Gap Classes the AI Must Detect",
    "## AI Failure Learning Ledger",
    "## Agent Geometry Layer",
    "## Process Alignment Layer",
    "## AI Rule - Directory Box and Mini README Synchronization",
    "## Law of Sufficient Form",
    "## Full Directory Box",
]
for section in required_sections:
    if section not in lines:
        errors.append(f"missing_isolated_section:{section}")

for i, line in enumerate(lines[:-1]):
    if line.startswith("| ") and line.endswith(" |") and "---" not in line:
        nxt = lines[i + 1]
        prev = lines[i - 1] if i > 0 else ""
        if line.count("|") >= 3 and not (nxt.startswith("|---") or "---" in prev):
            errors.append(f"table_header_without_separator:line_{i+1}:{line[:80]}")

for frag in [
    "Layer What it answers Primary output",
    "Surface Result",
    "Shell Meaning",
    "Change type Read first Validate",
    "Scan step Surface What to check",
    "Lesson ID Failure observed Root cause Permanent rule",
    "Rule Requirement",
]:
    if frag in text:
        errors.append(f"collapsed_table_fragment:{frag}")

long_lines = [i + 1 for i, line in enumerate(lines) if len(line) > 500]
if long_lines:
    errors.append(f"long_lines_over_500:{long_lines[:10]}")

if text.count("```") % 2 != 0:
    errors.append("unbalanced_code_fences")

passed = not errors
report = {
    "schema": "CMS-SA-v0.2b3-markdown-structure",
    "passed": passed,
    "errors": len(errors),
    "findings": errors,
    "line_count": len(lines),
    "non_claim_lock": "Markdown structure validation improves public rendering but does not prove runtime correctness."
}
out_json = ROOT / "reports" / "markdown_structure" / "latest_markdown_structure.json"
out_md = ROOT / "reports" / "markdown_structure" / "latest_markdown_structure.md"
out_json.parent.mkdir(parents=True, exist_ok=True)
out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
out_md.write_text(
    "# CMS-SA v0.2b3 Markdown Structure Validation\n\n"
    f"- passed: `{passed}`\n"
    f"- errors: `{len(errors)}`\n"
    f"- line_count: `{len(lines)}`\n\n"
    "## Findings\n\n"
    + ("\n".join(f"- `{e}`" for e in errors) if errors else "- none\n")
    + "\n\nNon-claim lock: Markdown structure validation is not runtime correctness.\n",
    encoding="utf-8",
)
print(json.dumps(report, indent=2))
raise SystemExit(0 if passed else 1)