"""Shared agent state — the object that flows through the loop / graph.

Both the Week-1 hand-written loop and the Week-2 LangGraph version read and write
this. Keep it the single source of truth for "what do we know so far".
"""
from __future__ import annotations

from typing import Any, TypedDict

# NOTE: LangGraph works nicely with a TypedDict state. Start here and grow it.
# You'll evolve these fields as the nodes take shape.


class AgentState(TypedDict, total=False):
    raw_input: str                 # original suspicious message / URL
    clean_input: str               # after input_guard normalisation
    entities: Any                  # schema.entities.Entities (once extraction runs)
    evidence: list[dict[str, Any]] # accumulated tool findings (the evidence chain)
    plan: list[str]                # which tools the planner wants to call next
    iterations: int                # reflect-loop counter (guard against runaway loops)
    report: Any                    # schema.output.TriageReport (final)

    # TODO(you): add fields as you need them — e.g. per-tool raw responses, timings,
    # a Langfuse trace id. Keep it lean; don't dump everything in here.
