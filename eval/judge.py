"""LLM-as-judge: score the QUALITY of the agent's reasoning, not just the final label.

A correct label with hand-wavy or hallucinated reasoning is still a weak result in a
security context. Use a separate Claude call to grade each rationale on things like:
evidence sufficiency, logical consistency, and absence of hallucinated facts.

Keep the judge independent of the agent (fresh context, its own prompt) so it's not
just rubber-stamping. This is a strong thing to show — most candidates only check labels.
"""
from __future__ import annotations


def score_rationale(suspicious_input: str, report: object) -> dict:
    """Grade one TriageReport's rationale. Return per-criterion scores + notes.

    TODO(you): implement with a separate client.messages call (consider a Pydantic
    output schema for the scores, like the main agent does). Decide your rubric:
    e.g. evidence_grounded (0-1), logically_consistent (0-1), no_hallucination (0-1).
    """
    raise NotImplementedError
