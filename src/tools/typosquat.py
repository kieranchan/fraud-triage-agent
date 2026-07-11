"""Typosquatting / impersonation detection.

Catches domains that mimic a real brand — e.g. `hsbc-hk.xyz` impersonating HSBC. Uses
edit distance (rapidfuzz) against a list of known legit brand domains.

Note this tool only makes sense to run once you HAVE a candidate domain and a set of
brands to compare against — that's a good example of the planner (③) choosing a tool
based on earlier findings, not running everything blindly.
"""
from __future__ import annotations

from .base import ToolResult


def check_typosquat(domain: str, brand_domains: list[str]) -> ToolResult:
    """Score how closely `domain` mimics any domain in `brand_domains`.

    TODO(you): implement. Think through:
      - which rapidfuzz scorer fits (ratio? partial? token?) — and why edit distance
        alone misses tricks like homoglyphs or added hyphens/keywords ("-secure", "-hk").
      - where does brand_domains come from? (a small curated list to start.)
      - this tool is local/deterministic — no network — so it doesn't need base.fetch,
        but its output should still be a ToolResult for uniformity.
    """
    raise NotImplementedError
