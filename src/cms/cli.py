from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from cms.core.runtime import CMSRuntime


def main() -> None:
    parser = argparse.ArgumentParser(prog="cms", description="Cybernetic Memory System CLI")
    sub = parser.add_subparsers(dest="command")

    cycle = sub.add_parser("cycle", help="Run the minimal CMS cycle")
    cycle.add_argument("--repo", default=".")
    cycle.add_argument("--profile", default="CMS-Core")

    observe = sub.add_parser("observe", help="Observe repository state")
    observe.add_argument("--repo", default=".")

    args = parser.parse_args()

    if args.command == "cycle":
        result = CMSRuntime(args.repo, args.profile).run_cycle()
        print(json.dumps(asdict(result), indent=2, ensure_ascii=False))
        return

    if args.command == "observe":
        runtime = CMSRuntime(args.repo)
        print(json.dumps(runtime.observe_repository(), indent=2, ensure_ascii=False))
        return

    parser.print_help()


if __name__ == "__main__":
    main()