from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from cms.alignment.multilevel import write_multilevel_alignment_report  # noqa: E402


def main() -> int:
    report = write_multilevel_alignment_report()
    print(json.dumps({
        "schema": "CMS-SA-v0.3b2-multilevel-alignment-emission",
        "passed": report.get("passed") is True,
        "version": report.get("version"),
        "feedback_items_checked": report.get("feedback_items_checked"),
        "feedback_items_aligned": report.get("feedback_items_aligned"),
        "wrote": [
            "outputs/alignment/latest_multilevel_alignment_report.json",
            "reports/alignment/latest_multilevel_alignment_report.json",
            "reports/alignment/latest_multilevel_alignment_report.md"
        ],
        "non_claim_lock": "Alignment emission writes repository evidence artifacts only."
    }, indent=2))
    return 0 if report.get("passed") is True else 1


if __name__ == "__main__":
    raise SystemExit(main())