"""The individual steps of the agent, as functions.

Each takes the agent state and returns an update to it. Shared by both the
hand-written loop and the LangGraph version. This is the core reasoning of the
project — implement it yourself.
"""
from __future__ import annotations

from .state import AgentState


def extract_entities(state: AgentState) -> AgentState:
    """② Pull URLs / phones / brands / urgency phrasing / payment methods from the text.

    TODO(you): implement. Decide pure-LLM vs LLM+regex (discuss the trade-off first).
    Remember to run the text through src.security.input_guard before it hits a prompt.
    Output should populate state["entities"] (schema.entities.Entities).
    """
    raise NotImplementedError


def plan_tools(state: AgentState) -> AgentState:
    """③ Decide which tools to call next, given current entities + evidence.

    TODO(you): implement. This is where the agent EARNS the name "agent" — the choice
    must depend on findings (e.g. new domain -> then check typosquatting). Populate
    state["plan"]. Return an empty plan to signal "nothing more worth checking".
    """
    raise NotImplementedError


def call_tools(state: AgentState) -> AgentState:
    """④ Execute the planned tools (can run in parallel) and append findings.

    TODO(you): implement. Dispatch to src.tools.*; append each result to
    state["evidence"]. Failed tools should still produce a recorded (error) finding —
    don't silently drop them.
    """
    raise NotImplementedError


def reflect(state: AgentState) -> str:
    """⑤ Is the evidence enough? Return the branch key: "continue" or "done".

    TODO(you): implement. Must honour MAX_ITERATIONS (return "done" if the cap is
    hit). Make the sufficiency test concrete and defensible — you'll be asked to
    justify it.
    """
    raise NotImplementedError


def judge(state: AgentState) -> AgentState:
    """⑥ Weigh all evidence into a TriageReport (risk level + confidence + reasons).

    TODO(you): implement via src.llm.chat(...) with
      response_format={"type": "json_schema", "json_schema": {"name": "triage_report",
        "strict": True, "schema": TriageReport.model_json_schema()}}
    then validate with TriageReport.model_validate_json(resp.choices[0].message.content).
    Every red flag should map to a piece of evidence in state["evidence"].
    """
    raise NotImplementedError
