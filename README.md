# Anti-Fraud Triage Agent (智能诈骗研判 Agent)

An autonomous LLM agent that takes a suspicious message (SMS / email text / URL), runs
**entity extraction → multi-source intelligence lookup → risk judgment**, and produces a
structured fraud-risk report with an evidence chain (risk level + confidence + red flags +
per-claim sources).

> Status: **early-stage prototype / learning project.** Not a production system.

## Why an agent, not a single classifier?
It decides *what to look up, how many times, and when the evidence is sufficient* —
autonomous planning, tool use, and a reflection loop. That makes it explainable,
extensible, and able to integrate multiple real-time intelligence sources.

## Architecture (ReAct)
```
input → parse → extract entities → plan → call tools (parallel) → reflect (enough?) → judge → structured output
```

## Tech stack
Python 3.11+ · Claude API (`anthropic`) · Pydantic v2 · LangGraph · rapidfuzz · RDAP/WHOIS · Langfuse

## Layout
- `src/agent/` — orchestration (state, ReAct loop, LangGraph, nodes)
- `src/tools/` — external intel tools (URL reputation, domain age, typosquat, scam patterns)
- `src/schema/` — Pydantic contracts (extracted entities, final report)
- `src/security/` — untrusted-input guard (the input is itself a scam message)
- `eval/` — reproducible offline eval + metrics + LLM-as-judge

## Getting started
```bash
python -m venv .venv && . .venv/Scripts/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env    # then fill in your API keys
```

## Roadmap
See `CLAUDE.md` for the phased plan and working conventions.
