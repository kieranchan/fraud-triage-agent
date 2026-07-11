"""Match text against known scam-script patterns.

Detects classic fraud phrasing: urgency ("your account will be suspended"), payment
demands (gift cards / crypto / wire), impersonation of authorities, etc.

Design guidance from CLAUDE.md: do NOT hard-code this as a giant if-else chain — that's
neither agent-like nor extensible. Prefer a data-driven pattern library, and consider a
semantic option (sentence-transformers) later so you catch paraphrased/novel scripts.
"""
from __future__ import annotations

from .base import ToolResult


def match_scam_patterns(text: str) -> ToolResult:
    """Return which known scam patterns `text` matches.

    TODO(you): implement. Decisions to make:
      - v1: a curated pattern library (categorised phrases) loaded from data, matched
        by keyword/regex — kept OUT of the code as data.
      - v2 (optional): semantic similarity against a phrase library so paraphrases and
        unseen scripts still hit.
      - output the matched categories + which phrase triggered, so it can become evidence.
    """
    raise NotImplementedError
