# PROGRESS —— 智能诈骗研判 Agent

> 活文档：记「现在在哪 / 下一步 / 为什么」。每次会话开始先读它，完成步骤后更新它。
> 约定见 CLAUDE.md「进度维护」。稳定约定进 CLAUDE.md，易变状态进这里。

## 📍 现在在哪
Week 1。tool-use 往返脚手架已就位（`react_loop.py`：`URL_REPUTATION_TOOL` schema + `_fake_url_reputation` stub + `demo_single_round_trip` 骨架，核心为 TODO(you)）。等本人实现 `demo_single_round_trip`。

## ▶️ 下一步（1–3 条，做完就换）
- [ ] 实现 `demo_single_round_trip`：单轮 tool-use 往返（用 stub）→ 跑通后交我审阅
- [ ] 包成带 `MAX_ITERATIONS` 的 `while` 循环（`run_react_loop`）
- [ ] 把 stub 换成真 `url_reputation`（VirusTotal / urlscan / Safe Browsing 三选一，先申请 key）
- [ ] judge 用 `response_format(json_schema)` + Pydantic 校验产出 TriageReport

## 🗺️ 路线图（大局，勾进度）
- [~] W1 手写单工具 ReAct loop（URL 信誉）—— 进行中
- [ ] W2 多工具 + 实体抽取 + LangGraph 重构 + Pydantic schema
- [ ] W3 评估体系（数据集 + fixtures + 指标/混淆矩阵 + LLM-as-judge + Langfuse）
- [ ] W4（可选）多模态截图输入 + demo 前端

## 🧠 决策日志（只增不改，带日期 + 为什么）
- 2026-07-11 研判后端由 Claude 改为 **grok-4.5（经自建 CPA / CLIProxyAPI 网关，OpenAI 兼容端点）**。原因：走自己的代理；grok 只在 `/v1/chat/completions` 可用（`/v1/messages` 返回空）。`src/llm.py` 做成 provider 无关，换模型只改 `.env` 的 `LLM_MODEL`。
- 2026-07-11 结构化输出改用 OpenAI `response_format(json_schema)` + Pydantic 校验（弃用 Anthropic 专属 `messages.parse`）。

## 🧰 环境状态
- `.venv` 已建（暂只装 openai + python-dotenv；跑 `pip install -r requirements.txt` 补齐其余依赖）
- `.env` 已配（CPA 域名 + key + `LLM_MODEL=grok-4.5`），已 gitignore
- 冒烟测试 `python -m src.llm` → 打印 `pong`（链路已通）
