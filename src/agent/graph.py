"""Week 2: the same loop, rebuilt on LangGraph.

Once the hand-written loop works, port it here to get proper state management,
conditional branches, and (later) clean Langfuse tracing. The conditional edge out
of `reflect` is what makes this a real loop rather than a linear pipeline.

This file is wiring only — the actual node logic lives in `nodes.py`.
"""
from __future__ import annotations

from .state import AgentState

MAX_ITERATIONS = 5


def build_graph():
    """Assemble and compile the StateGraph.

    Sketch of the wiring you'll build (pseudocode — fill in with real LangGraph API):

        graph = StateGraph(AgentState)
        graph.add_node("extract", nodes.extract_entities)
        graph.add_node("plan",    nodes.plan_tools)
        graph.add_node("tools",   nodes.call_tools)
        graph.add_node("judge",   nodes.judge)

        graph.set_entry_point("extract")
        graph.add_edge("extract", "plan")
        graph.add_edge("plan", "tools")
        # conditional edge = the reflection loop:
        graph.add_conditional_edges("tools", nodes.reflect, {
            "continue": "plan",   # need more evidence -> plan again
            "done":     "judge",  # enough (or MAX_ITERATIONS hit) -> judge
        })
        graph.add_edge("judge", END)
        return graph.compile()

    TODO(you): implement with the real LangGraph API. Make sure `reflect` respects
    MAX_ITERATIONS so the "continue" branch can't spin forever.
    """
    raise NotImplementedError
