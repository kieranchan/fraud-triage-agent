"""Week 1: a hand-written ReAct loop (NO framework).

Goal of this file is *understanding* — before LangGraph hides the loop from you,
write it yourself so you can explain "what decides the next tool, and when is the
evidence enough" in an interview.

Start with ONE tool (url_reputation). Get: input a URL -> the Agent decides to look
it up -> reads the result -> gives a verdict. Then make it loop.

The shape below is intentionally skeletal. Fill in the TODOs yourself.
"""
from __future__ import annotations

MAX_ITERATIONS = 5  # hard cap so a bad reflection step can't loop forever


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
