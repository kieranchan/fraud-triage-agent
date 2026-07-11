"""Shared plumbing for every tool: timeout, retry, and — importantly — a cache hook.

WHY THE CACHE HOOK MATTERS (this is the single most important design decision in the
project). Your Week-3 regression eval reruns 200+ samples every time you tweak a prompt.
If each run hits VirusTotal/RDAP live:
  - metrics drift because the *external world* changed, not your code (useless for regression),
  - you blow the free-tier quota (VirusTotal free ≈ 4 req/min, 500/day),
  - dead phishing URLs read as "clean" and get miscounted as model errors.

Fix: snapshot every tool's response into eval/fixtures/ when you build the dataset,
and have offline eval read from there. Two modes:
  - LIVE   : real network call, and (optionally) write the response to fixtures.
  - OFFLINE: read the cached fixture; never touch the network.

Every tool should call through here so they all get caching + retry + timeouts for free.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolResult:
    """Uniform result every tool returns, so the judge can treat them alike."""

    source: str                       # tool name, e.g. "virustotal"
    ok: bool                          # False on error/timeout (still recorded — never dropped)
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


def fetch(
    source: str,
    cache_key: str,
    live_call,            # a zero-arg callable that performs the real network request
    *,
    offline: bool = False,
) -> ToolResult:
    """Run a tool call through the cache + resiliency layer.

    Behaviour to implement:
      - offline=True  -> load eval/fixtures/<source>/<cache_key>.json and return it;
                         if the fixture is missing, that's an explicit error (don't
                         silently fall through to a live call in offline mode).
      - offline=False -> call live_call() with a timeout + a couple of retries;
                         optionally persist the response to the fixture path so it can
                         be replayed offline later.

    TODO(you): implement. Decide the fixture path scheme and the retry/timeout policy.
    Think about what makes a stable cache_key (e.g. the normalised URL/domain).
    """
    raise NotImplementedError
