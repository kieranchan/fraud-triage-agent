"""CLI entry point: analyse one suspicious message / URL and print the report.

Usage (once implemented):
    python -m src.main "https://hsbc-hk.xyz/verify your account now"
"""
from __future__ import annotations

import sys


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print('usage: python -m src.main "<suspicious text or url>"')
        return 2

    suspicious_input = argv[1]

    # TODO(you): call the agent (react_loop.run_react_loop in Week 1, the compiled
    # graph in Week 2) and pretty-print the TriageReport.
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
