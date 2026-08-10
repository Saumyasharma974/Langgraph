# 🤖 Agentic AI & LangGraph Learning Journey

[![Status](https://img.shields.io/badge/Python-100%25-brightgreen)]()
[![Status](https://img.shields.io/badge/LLM%20Fundamentals-100%25-brightgreen)]()
[![Status](https://img.shields.io/badge/LangChain-In%20Progress-yellow)]()
[![Status](https://img.shields.io/badge/LangGraph-Upcoming-lightgrey)]()

A practical, step-by-step repository documenting my journey from **Python fundamentals** to **production-ready Agentic AI systems**, using Python, LLMs, LangChain, LangGraph, RAG, and Multi-Agent architectures.

This repository is designed so that anyone visiting it can understand:

- What I have studied
- Why I studied each topic
- What I implemented
- How the concepts connect
- What is completed
- What is coming next

> **Learning philosophy:** I don't try to memorize framework APIs. I first learn the engineering concepts behind AI agents, then implement them with LangChain / LangGraph.

---

## 🧭 How to Use This Repository

Follow the chapters in order:

```
01 — Python for Agentic AI
02 — LLM Fundamentals
03 — LangChain
04 — LangGraph
05 — Agents + Tools
06 — Memory
07 — RAG
08 — Multi-Agent Systems
09 — Production
```

Each chapter contains practical Python code and notes. Code is intentionally organized into small files so each concept can be studied independently.

---

## 🎯 Learning Goals

Through this repository, I aim to understand:

- Python fundamentals required for Agentic AI
- LLM fundamentals
- Prompt engineering
- LLM APIs and structured outputs
- Tool / function calling
- LangChain fundamentals
- LangGraph workflows, state management, and conditional routing
- Agent memory
- Human-in-the-loop workflows
- RAG and Agentic RAG
- Multi-agent architectures
- Production-ready AI agent systems

---

## 🧠 Learning Structure

The repository follows three layers:

| Layer | Focus Areas |
|---|---|
| **Layer 1 — Foundations** | Python · LLM Concepts · Prompting · Structured Data · Async Programming |
| **Layer 2 — AI Application Engineering** | LangChain · Tools · Tool Calling · LangGraph · State · Memory · RAG |
| **Layer 3 — Agentic Systems** | Agents · Agent Loops · Multi-Agent Systems · Human-in-the-Loop · Persistence · Observability · Production Deployment |

**Overall path:**

```
Python → LLM → LLM Application → Tool Calling → Stateful Workflow
   → Agent → RAG / Agentic RAG → Multi-Agent System → Production AI System
```

---

## 📚 Learning Roadmap

```
Python for Agentic AI
        ↓
LLM Fundamentals
        ↓
Prompt Engineering
        ↓
Structured Output
        ↓
Tool Calling
        ↓
LangChain
        ↓
LangGraph
        ↓
Agents + Tools
        ↓
Memory
        ↓
RAG
        ↓
Multi-Agent Systems
        ↓
Production AI Systems
```

---

## 📈 Current Progress

```
Python for Agentic AI       ██████████ 100% ✅
LLM Fundamentals            ██████████ 100% ✅
LangChain                   ░░░░░░░░░░  NEXT 🚀
LangGraph                   ░░░░░░░░░░  Upcoming
Agents & Tools               ░░░░░░░░░░  Upcoming
Memory                       ░░░░░░░░░░  Upcoming
RAG                          ░░░░░░░░░░  Upcoming
Multi-Agent Systems           ░░░░░░░░░░  Upcoming
Production                   ░░░░░░░░░░  Upcoming
```

---

## 🐍 Chapter 01 — Python for Agentic AI

**Status:** `██████████ 100% ✅`

The first phase focuses on the Python concepts required to understand and build AI agent systems.

**Topics covered:** Variables and data types · Lists and dictionaries · Loops · Functions · Parameters and return values · Type hints · `TypedDict` · State management · Agent-to-agent data flow · Conditional routing · Retry loops · Maximum attempt handling · Python classes · Pydantic · `BaseModel` · `Literal` · `Field` · Runtime validation · Exception handling · Modules and imports · Environment variables · `.env` configuration · `async`/`await` · `asyncio` · Concurrent operations with `asyncio.gather()`

### Understanding Agent State

One of the first concepts explored is shared agent state:

```python
from typing import TypedDict

class AgentState(TypedDict):
    task: str
    research: str | None
    content: str | None
    review: str | None
```

State flows across workflow steps:

```
User Task → Researcher → Research Result → Writer
   → Generated Content → Reviewer → Final Result
```

This provides the foundation for understanding state-based workflows in LangGraph.

### Conditional Agent Workflows

Explored how agents can make decisions based on current state:

```
START → Developer → Tester → Tests Passed?
                                /        \
                              YES          NO
                               ↓            ↓
                              END      Developer (retry)
```

Concepts introduced: conditional routing, retry workflows, termination conditions, maximum retry limits, and preventing infinite loops. These will later be implemented using LangGraph conditional edges.

### Agent Communication

Instead of working independently, agents consume outputs produced by previous agents:

```
Researcher → (research) → Writer → (content) → Reviewer → (review) → Final State
```

This clarified how shared state enables communication between specialized agents.

### Structured Data with Pydantic

```python
from typing import Literal
from pydantic import BaseModel, Field

class TaskDecision(BaseModel):
    agent: Literal["researcher", "developer", "reviewer"]
    reason: str
    priority: int = Field(ge=1, le=5)
```

This provides runtime validation, controlled agent selection, structured data, and type-safe outputs — later used with an actual LLM to generate structured AI decisions.

### Error Handling

AI systems interact with external services (LLM APIs, search APIs, databases, tools) that can fail:

```python
try:
    result = search_tool()
except Exception as error:
    print(error)
```

Instead of crashing the entire workflow, an agent system can decide to **retry**, **fall back**, **continue**, or **terminate**.

### Environment Variables

Secrets such as API keys are never hardcoded:

```python
from dotenv import load_dotenv
load_dotenv()
```

```
AI_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git via `.gitignore`; an `.env.example` file is committed instead.

### Asynchronous Agent Execution

Many AI operations are I/O-bound (LLM requests, search APIs, database queries, external tools). `async`/`await` lets other async tasks progress while waiting:

```python
async def research_agent():
    await asyncio.sleep(2)
    return "Research completed"
```

Independent agents can run concurrently:

```python
research, news, docs = await asyncio.gather(
    research_agent(),
    news_agent(),
    docs_agent()
)
```

```
                    Main
                     │
        ┌────────────┼────────────┐
        ↓             ↓            ↓
   Research         News          Docs
    Agent           Agent         Agent
        │             │            │
        └─────────────┼────────────┘
                       ↓
                Combined Result
```

---

## 🧠 Chapter 02 — LLM Fundamentals

**Status:** `██████████ 100% ✅`

The second phase focuses on understanding how LLM-powered applications work before moving deeper into LangChain and LangGraph.

### Topics Covered

| Area | Concepts |
|---|---|
| **LLM Basics** | What is an LLM? · LLM vs Agent · Tokens · Context / context window · Conversation history · Messages (system/human/AI) · Temperature · Hallucinations & limitations |
| **LLM Integration** | Groq API · `ChatGroq` · Environment variables for API keys · `invoke()` · `stream()` · `ainvoke()` · `astream()` · `response.content` · Response metadata & token usage |
| **Prompt Engineering** | Prompt structure (role, audience, task, context, requirements, constraints, output format) · Zero-shot & few-shot prompting · In-context learning · Role prompting · Context engineering · Prompt chaining |
| **Prompt Security** | Prompt injection (direct & indirect) · Instruction leakage · Instruction hierarchy · Treating user/external content as untrusted input · Input/output validation · Least privilege · Human approval for sensitive actions |
| **Structured Outputs** | Pydantic `BaseModel` · `Field` · `Literal` · Runtime validation · `with_structured_output()` · Structured agent decisions · Controlled routing/data |
| **Tool Calling** | `@tool` · `bind_tools()` · `tool_calls` · Tool arguments & execution · Multiple tools · Tool registry · `ToolMessage` · Manual tool-calling loop · LLM requests vs. application execution · Tool validation & security |
| **Reliability & Production Engineering** | Exception handling · Retry strategy · Exponential backoff · Timeouts · Rate limits · Token rate limits · Async LLM/tool operations · Sequential vs. concurrent execution · Parallel LLM calls · Latency optimization |
| **Token & Cost Engineering** | Token usage metadata · Prompt/completion/total tokens · Token limits · Cost optimization · Model selection · Capability vs. cost vs. latency trade-offs |
| **Grounding & Hallucination Mitigation** | Grounding with verified context · Grounded vs. ungrounded responses · Context-only answering · Safe fallback when information is unavailable |
| **Advanced LLM Evaluation** | Evaluation datasets · Expected outputs vs. predictions · Accuracy · Failure analysis · Prompt V1 vs. V2 · Regression testing · Edge cases · Category-wise evaluation · Dataset quality and limitations |

### Prompt Evaluation Result

A sentiment-classification prompt was evaluated on 10 test cases:

```
Prompt V1 Accuracy: 90%
Prompt V2 Accuracy: 100%
Improvement:        +10 percentage points
```

The failed V1 case:

```
Input:      The product is okay.
Expected:   Positive
Predicted:  Negative
```

The prompt was improved by clarifying the sentiment definitions and examples.

> **Lesson:** Prompt quality should be measured with test cases, not judged on intuition alone.

LLM Fundamentals is now complete. Deep implementation of output validation and guardrails is deferred to the LangChain phase, where they can be applied using structured outputs, parsers, validation, retries, and production-oriented chains.

---

## 🧪 LLM Fundamentals — Engineering Practice

The latest engineering phase focused on turning LLM concepts into measurable, production-oriented Python experiments.

### Streaming & Async

- Streaming with `llm.stream()`
- Async fundamentals with `asyncio`
- Async LLM calls with `ainvoke()`
- Async streaming with `astream()`
- Concurrent execution with `asyncio.gather()`

### Reliability & Performance

- Exception handling
- Retry strategies & exponential backoff
- Request and LLM-specific timeouts
- Request and token rate limits
- Token usage and response metadata
- Cost optimization & model selection (Groq)
- Sequential vs. parallel execution
- Parallel LLM calls & latency measurement/optimization

### Grounding & Evaluation

- Grounding using verified context
- Grounded vs. ungrounded responses
- Hallucination mitigation through context constraints
- Evaluation datasets & accuracy measurement
- Failure analysis & regression testing
- Prompt V1 vs. Prompt V2 comparison
- Edge-case testing & category-wise evaluation

### Evaluation Results

A 10-case sentiment benchmark improved from:

```
Prompt V1 → 90%
Prompt V2 → 100%
Improvement → +10 percentage points
```

A broader 15-case dataset exposed an important limitation:

```
Overall Accuracy → 80%
Clear Positive   → 100%
Clear Negative   → 100%
Edge Cases       → 40%
```

This demonstrated why representative datasets and edge cases matter more than relying on a single overall accuracy number.

### Current Boundary

Output validation and guardrails have been covered at the conceptual level. Their deeper implementation will be done with **LangChain**, alongside structured outputs, parsers, validation, retries, and production-oriented chains.

---

## ✍️ Prompt Engineering — Completed

### Prompt Anatomy

```
Role · Audience · Task · Context · Requirements · Constraints · Examples · Output Format
```

Not every prompt needs every field — the fields are chosen according to the task.

**Example**

```
Role:        You are an experienced backend teacher.
Audience:    The learner is a beginner developer.
Task:        Explain JWT authentication.
Context:     The learner understands basic APIs but has never implemented authentication.
Requirements:
  - Explain what JWT is.
  - Explain how JWT authentication works.
  - Explain Header, Payload and Signature.
Constraints:
  - Use simple language.
  - Explain technical terms.
  - Avoid unnecessary jargon.
Output Format:
  1. What is JWT?
  2. How does it work?
  3. Main components
  4. Real-world example
  5. Key takeaway
```

### Zero-Shot

```
Classify this sentence as Positive or Negative.
```

### Few-Shot

```
Example: I love this movie. → Positive
Example: This service is terrible. → Negative

Now classify: I really enjoyed the experience.
```

### Context Engineering

Prompt engineering isn't only about wording the instruction — context engineering focuses on supplying the model with the right information, in the right structure, at the right time:

```
User Input + System Instructions + Conversation History
   + Application State + Retrieved Data + Tool Results
```

### Prompt Chaining

Complex work can be divided into multiple LLM calls:

```
Topic → Generate key points → Expand points → Review and polish → Final content
```

This improves control but increases model calls, latency, and token usage.

### Prompt Injection

A user or external document may try to override intended instructions — for example, asking the model to ignore its system prompt and adopt a different persona. Applications should treat user/external content as untrusted input and keep important behavior controlled by higher-priority instructions and application logic.

### Instruction Leakage

A user may try to get the model to reveal hidden instructions. The system should not expose confidential system/developer instructions.

### Key Lesson

```
Good Prompt → Clear Task → Relevant Context → Controlled Output → Evaluation → Improved Prompt
```

---

## 🛠️ Mini Project — AI Interview Coach

**Status:** `██████████ 100% ✅`

To practically apply the LLM concepts learned so far, I built an **AI Interview Coach**: an application that conducts a technical interview using Groq and evaluates candidate answers using Pydantic structured output.

### Features

- Interview type selection: DSA, Backend, Python, AI/ML, Full Stack
- AI-generated interview questions
- Candidate answer input
- Structured answer evaluation (score 1–10)
- Strength and weakness identification
- Improvement suggestions
- Adaptive question difficulty
- Conversation history and score tracking
- Final interview report with average score and overall assessment
- Error handling

### Architecture

```
User → Select Interview Type → Groq LLM → Generate Question
   → Candidate Answer → Structured LLM → Pydantic Validation
   → Interview Feedback
            ┌──────────┼──────────┐
            ↓          ↓          ↓
        Strengths  Weaknesses   Score
            └──────────┼──────────┘
                        ↓
             Adaptive Next Question
                        ↓
                  Final Report
```

### Technologies Used

Python · Groq · LangChain · Pydantic · python-dotenv

---

## 📂 Current Repository Structure

```
agentic-ai-langgraph-learning/
│
├── 01_python_for_agents/
│   ├── 01_state_basics.py
│   ├── 02_functions.py
│   ├── 03_typed_state.py
│   ├── 04_conditional_routing.py
│   ├── 05_pydantic_task.py
│   ├── 06_exception_handling.py
│   ├── 08_async_await.py
│   │
│   └── 07_modules_and_env/
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── researcher.py
│       │   └── writer.py
│       │
│       ├── .env.example
│       ├── .gitignore
│       └── main.py
│
├── 02_llm_fundamentals/
│   ├── 01_basic_llm_call.py
│   ├── 02_messages.py
│   ├── 03_tool_calling.py
│   ├── 04_multiple_tools.py
│   ├── 05_complete_tool_loop.py
│   ├── 06_structured_output.py
│   ├── 14_streaming.py
│   ├── 15_async_basics.py
│   ├── 16_async_llm.py
│   ├── 17_error_handling.py
│   ├── 18_retry_strategy.py
│   ├── 19_exponential_backoff.py
│   ├── 20_timeout.py
│   ├── 21_llm_timeout.py
│   ├── 22_rate_limits.py
│   ├── 23_token_rate_limit.py
│   ├── 24_token_usage.py
│   ├── 25_cost_optimization.py
│   ├── 26_model_selection.py
│   ├── 27_latency_optimization.py
│   ├── 28_grounding.py
│   ├── 29_grounding_comparison.py
│   ├── 30_llm_evaluation.py
│   ├── 31_regression_testing.py
│   ├── 32_evaluation_dataset.py
│   └── README.md
│
├── 03_ai_interview_coach/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── services/
│   ├── .env.example
│   ├── .gitignore
│   ├── requirements.txt
│   └── README.md
│
├── README.md
└── requirements.txt
```

> The repository structure will continue to evolve as new concepts and projects are added.

---

## 🗺️ Upcoming Chapters

### Chapter 02 — LLM Fundamentals (Completed)

**Covered:** LLM basics · Messages · Prompt Engineering · Zero-shot/Few-shot Prompting · Role Prompting · Context Engineering · Prompt Chaining · Prompt Injection · Instruction Hierarchy · Prompt Security · Structured Outputs · Tool Calling · Streaming · Async LLM calls · Error Handling · Retry Strategies · Exponential Backoff · Timeouts · Rate Limits · Token Usage · Cost Optimization · Model Selection · Latency Optimization · Grounding · Hallucination Mitigation · Advanced Evaluation · Regression Testing · Evaluation Datasets · Failure Analysis

**Deferred to LangChain:** Deep implementation of output validation and guardrails using structured output, parsers, validation, retries, and production patterns.

### Currently Learning

**LangChain** — fundamentals, chains, structured outputs, parsers, validation, and production-oriented patterns.

### Next Major Phase

```
LangChain → LangGraph → Agents → Memory → RAG
   → Agentic RAG → Multi-Agent Systems → Production
```

---

## ✅ Completed So Far

Python foundation for Agentic AI · Agent state concepts · Conditional routing · Retry and termination concepts · Pydantic validation · Async Python fundamentals · LLM basics · Messages · Prompt Engineering · Context Engineering · Prompt Chaining · Prompt Injection · Instruction Hierarchy · Prompt Security · Structured Outputs · Tool Calling · Manual Tool Loop · Streaming · Async LLM calls · Error Handling · Retry Strategy · Exponential Backoff · Timeouts · Rate Limits · Token Usage · Cost Optimization · Model Selection · Latency Optimization · Grounding · Hallucination Mitigation · Advanced Evaluation · Regression Testing · Evaluation Dataset · Failure Analysis

---

## 👨‍💻 Author

**Saumya Sharma**

Learning and building in: `Agentic AI` · `LangGraph` · `LangChain` · `Python` · `LLMs` · `Multi-Agent Systems`

---

⭐ If you find this learning journey useful, feel free to star the repository and follow along as I continue building more advanced Agentic AI systems.
