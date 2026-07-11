"""URL / domain reputation lookup.

Week 1's single tool. Query a reputation source and turn the response into a ToolResult
the judge can reason about. Candidate sources (confirm current free-tier terms first):
  - VirusTotal  (URL/domain/file reputation; ~4 req/min, 500/day free)
  - urlscan.io  (URL behaviour scan)
  - Google Safe Browsing (known-malicious URL list)

Start with ONE. Route the actual HTTP through src.tools.base.fetch so you get caching.
"""
from __future__ import annotations

from .base import ToolResult


def check_url_reputation(url: str, *, offline: bool = False) -> ToolResult:
    """Return a reputation verdict for `url`.

    TODO(you): implement. Steps to think through:
      - normalise the URL (this becomes the cache_key so fixtures are stable).
      - build the provider request; wrap the live call in a lambda passed to base.fetch.
      - map the provider's response to ToolResult.data — pull out the few fields that
        actually matter for judgment (e.g. #engines flagging it), not the whole blob.
      - what does a *clean* result mean for a URL that might just be brand-new? (This is
        exactly the dataset-decay trap — a dead malicious URL can look clean.)
    """
    raise NotImplementedError
