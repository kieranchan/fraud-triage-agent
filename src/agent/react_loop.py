"""Week 1: a hand-written ReAct loop (NO framework).

Goal of this file is *understanding* — before LangGraph hides the loop from you,
write it yourself so you can explain "what decides the next tool, and when is the
evidence enough" in an interview.

Start with ONE tool (url_reputation). Get: input a URL -> the Agent decides to look
it up -> reads the result -> gives a verdict. Then make it loop.

The shape below is intentionally skeletal. Fill in the TODOs yourself.

LLM calls go through src.llm.chat() (grok-4.5 via the CPA gateway). This is an
OpenAI-style tool loop: the model asks for a tool when
resp.choices[0].finish_reason == "tool_calls"; you run it, append a
{"role": "tool", "tool_call_id": ..., "content": ...} message, then call again
until it stops. (See CLAUDE.md "LLM 用法".)
"""
from __future__ import annotations

from .. import llm
from ..tools.base import ToolResult

MAX_ITERATIONS = 5  # hard cap so a bad reflection step can't loop forever


# ---------------------------------------------------------------------------
# Week-1 stepping stone: ONE tool-use round-trip (no loop yet).
# Goal: watch the messages list roll —
#   user  ->  assistant(tool_calls)  ->  tool(result)  ->  assistant(verdict)
# Once you can narrate every step, you fold it into the while-loop in
# run_react_loop() below. The two helpers here are plumbing (provided) so you
# can focus on the control flow, which is yours to write.
# ---------------------------------------------------------------------------

# The tool schema you expose to the model (OpenAI / function-calling shape).
URL_REPUTATION_TOOL = {
    "type": "function",
    "function": {
        "name": "check_url_reputation",
        "description": "Look up a URL's reputation; returns how many engines flag it as malicious.",
        "parameters": {
            "type": "object",
            "properties": {"url": {"type": "string", "description": "the URL to check"}},
            "required": ["url"],
        },
    },
}


def _fake_url_reputation(url: str) -> ToolResult:
    """TEMPORARY stub so you can wire the loop before touching a real API.
    Swap for src.tools.url_reputation.check_url_reputation once the loop works.
    """
    return ToolResult(
        source="url_reputation(stub)",
        ok=True,
        data={"malicious_votes": 7, "total_engines": 90, "note": "hard-coded stub"},
    )


def demo_single_round_trip(suspicious_input: str) -> str:
    """Week-1 milestone #1: drive ONE tool-use round-trip by hand.

    Build the messages list so it evolves like this:
      1. messages = [{"role": "user", "content": <ask it to triage suspicious_input>}]
      2. resp = llm.chat(messages, tools=[URL_REPUTATION_TOOL])
      3. if resp.choices[0].finish_reason == "tool_calls":
           - tc = resp.choices[0].message.tool_calls[0]   # tc.id, tc.function.name/.arguments
           - APPEND the assistant message (the one carrying tool_calls) to messages
           - run _fake_url_reputation(<parsed args>) and get a ToolResult
           - APPEND {"role": "tool", "tool_call_id": tc.id, "content": <result as a string>}
      4. resp = llm.chat(messages)          # no tools this time
      5. return resp.choices[0].message.content   # the model's verdict

    TODO(you): implement steps 1-5. Three easy-to-miss bits:
      - append the assistant tool_calls message BEFORE the tool result, else the
        next call errors ("tool result without a preceding tool call").
      - tc.function.arguments is a JSON *string* — json.loads() it to get {"url": ...}.
      - the assistant message can be appended as resp.choices[0].message.model_dump()
        (a plain dict) so it round-trips cleanly.
    """
    raise NotImplementedError


def run_react_loop(suspicious_input: str) -> object:
    """Run the agentic loop on one input and return a TriageReport.

    The loop you're implementing (steps map to the diagram in CLAUDE.md):
      1. guard + normalise the input          (src.security.input_guard)
      2. extract entities                      (② — start simple: just URLs)
      3. PLAN: given what we know, which tool(s) to call next? (③)
      4. call the chosen tool(s)               (④ — src.tools.*)
      5. REFLECT: is the evidence enough to decide? (⑤)
           - not enough AND iterations < MAX_ITERATIONS -> back to step 3
           - enough (or cap hit)                        -> step 6
      6. JUDGE: weigh all evidence -> TriageReport (⑥)

    Key design decisions to make yourself (discuss them first if you want):
      - How does the planner decide the next tool? (LLM tool-use? simple rules?)
      - What's the "enough evidence" test in step 5? Be concrete — a vague test is
        what turns a real loop into a fake one.
      - Why re-query is pointless for deterministic tools: the loop's value is
        picking a DIFFERENT tool based on findings, not repeating one.
    """
    # TODO(you): implement the loop. Suggested scaffold to fill in:
    #
    # state = {"raw_input": suspicious_input, "evidence": [], "iterations": 0}
    # ... guard + extract ...
    # while state["iterations"] < MAX_ITERATIONS:
    #     plan = plan_next_tools(state)
    #     if not plan:            # planner says "done"
    #         break
    #     run the tools in `plan`, append findings to state["evidence"]
    #     state["iterations"] += 1
    #     if evidence_is_sufficient(state):
    #         break
    # return judge(state)
    raise NotImplementedError
