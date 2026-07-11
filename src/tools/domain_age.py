"""Domain registration age — a freshly registered domain is a strong fraud signal.

Prefer RDAP over classic WHOIS: RDAP returns structured JSON, is more reliable, and is
much easier to hang an evidence chain off. Use `whoisit` for RDAP; fall back to
`python-whois` only for TLDs whose RDAP coverage is poor (some ccTLDs, e.g. .hk).
"""
from __future__ import annotations

from .base import ToolResult


def check_domain_age(domain: str, *, offline: bool = False) -> ToolResult:
    """Return registration date / age for `domain`.

    TODO(you): implement. Steps to think through:
      - use tldextract to reduce a URL to its registered domain first.
      - RDAP path (whoisit): parse the registration/creation date out of the response.
      - fallback path (python-whois): only when RDAP has no data for that TLD.
      - route through base.fetch so results are cached for offline eval.
      - surface a simple derived signal in ToolResult.data, e.g. age_in_days, so the
        judge doesn't have to parse dates itself. What age threshold counts as "high risk"?
    """
    raise NotImplementedError
