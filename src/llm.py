"""Provider-agnostic LLM client for the agent.

Talks to the CPA (CLIProxyAPI) gateway via its **OpenAI-compatible** endpoint
(`/v1/chat/completions`). Everything is config-driven from `.env`, so you can
switch models/providers (grok-4.5, and the claude-* / gpt-5.x the proxy also
exposes) without touching code — just change LLM_MODEL.

    .env:
      LLM_BASE_URL   e.g. https://cliproxy-do3.oragenode.online/v1
      LLM_API_KEY    CPA key (sent as Authorization: Bearer ...)
      LLM_MODEL      e.g. grok-4.5

This module is deliberately ONLY transport. The agent's reasoning — planning,
the tool-use loop, the judge — lives in src/agent and is yours to write; it
calls chat() from here.

Quick connectivity check:  python -m src.llm
"""
from __future__ import annotations

import functools
import os

from dotenv import load_dotenv
from openai import OpenAI


@functools.lru_cache(maxsize=1)
def _client() -> OpenAI:
    """Build the OpenAI-SDK client once, pointed at the CPA gateway."""
    load_dotenv()
    base_url = os.environ.get("LLM_BASE_URL")
    api_key = os.environ.get("LLM_API_KEY")
    if not base_url or not api_key:
        raise RuntimeError(
            "LLM_BASE_URL / LLM_API_KEY not set. Copy .env.example to .env and fill them in."
        )
    return OpenAI(base_url=base_url, api_key=api_key)


def model() -> str:
    """The configured model id (defaults to grok-4.5)."""
    load_dotenv()
    return os.environ.get("LLM_MODEL", "grok-4.5")


def chat(messages: list[dict], *, tools=None, response_format=None, **kwargs):
    """Thin passthrough to chat.completions.create — returns the raw SDK response.

    - tools=[...]            -> function calling; watch resp.choices[0].finish_reason == "tool_calls"
    - response_format={...}  -> structured output; pair a json_schema with Pydantic validation
    Any other create() kwargs (temperature, max_tokens, tool_choice, ...) pass through.
    """
    params: dict = {"model": kwargs.pop("model", model()), "messages": messages}
    if tools is not None:
        params["tools"] = tools
    if response_format is not None:
        params["response_format"] = response_format
    params.update(kwargs)
    return _client().chat.completions.create(**params)


if __name__ == "__main__":  # smoke test: python -m src.llm
    resp = chat(
        [{"role": "user", "content": "Reply with the single word: pong"}],
        max_tokens=10,
    )
    print(f"model={model()}  ->  {resp.choices[0].message.content!r}")
