"""Entities extracted from a suspicious message.

This is the hand-off between the extraction step (②) and the planning step (③):
the planner decides which tools to call based on what entities are present.

Starter model — shape it to what your extractor actually produces. Design question
to settle first: pure-LLM extraction vs. LLM + regex hybrid (phones/URLs are easy
for regex; brand names and "urgency phrasing" are not).
"""
from __future__ import annotations

from pydantic import BaseModel, Field


class Entities(BaseModel):
    urls: list[str] = Field(default_factory=list)
    phone_numbers: list[str] = Field(default_factory=list)
    emails: list[str] = Field(default_factory=list)
    brands: list[str] = Field(default_factory=list, description="Impersonated brands, e.g. HSBC")
    amounts: list[str] = Field(default_factory=list, description="Money amounts mentioned")
    urgency_phrases: list[str] = Field(default_factory=list, description="Pressure / time-pressure language")
    payment_methods: list[str] = Field(default_factory=list, description="Gift card, crypto, wire, etc.")

    # TODO(you): add/remove fields to match your extractor. Consider whether you
    # want a confidence per entity, or the source span in the original text.
