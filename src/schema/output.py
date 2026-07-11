"""The final structured triage report — the Agent's output contract.

Every conclusion must be traceable to concrete evidence (that's the "evidence chain"
selling point). Feed this model to `client.messages.parse(..., output_format=TriageReport)`
so the model is forced to fill it and Pydantic validates the result.

Starter model — refine the fields as your judgment logic firms up.
"""
from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Evidence(BaseModel):
    """One piece of evidence backing a red flag or the overall verdict."""

    source: str = Field(description="Which tool/step produced this, e.g. 'virustotal', 'rdap', 'typosquat'")
    finding: str = Field(description="What was found, in one line")
    # TODO(you): consider a `weight` or `severity` so the judge can reason about
    # how much each piece of evidence should move the verdict.


class TriageReport(BaseModel):
    risk_level: RiskLevel
    confidence: float = Field(ge=0.0, le=1.0, description="0-1 calibrated confidence")
    red_flags: list[str] = Field(default_factory=list, description="Named risk signals that fired")
    evidence: list[Evidence] = Field(default_factory=list)
    rationale: str = Field(description="Human-readable reasoning tying evidence to the verdict")

    # TODO(you): decide whether you want a `recommended_action` (e.g. block / warn /
    # send to human review) — ties into the "宁误报不漏报 + 人工复核层" trade-off.
