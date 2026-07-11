"""Smoke tests — confirm the package imports and schemas are well-formed.

Grow this as you implement. The real regression suite is eval/run_eval.py; these are
just fast unit-level checks.
"""
from __future__ import annotations

from src.schema.output import RiskLevel, TriageReport


def test_risk_levels_exist():
    assert {r.value for r in RiskLevel} == {"high", "medium", "low"}


def test_triage_report_validates():
    report = TriageReport(
        risk_level=RiskLevel.LOW,
        confidence=0.1,
        red_flags=[],
        evidence=[],
        rationale="nothing suspicious",
    )
    assert report.risk_level is RiskLevel.LOW

    # TODO(you): add tests as you build — e.g. entity extraction on a known string,
    # typosquat scoring hsbc-hk.xyz against hsbc.com, metrics math on a tiny fixture.
