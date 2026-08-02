# 🤖 Agentic AI & LangGraph Learning Journey

A practical, step-by-step repository documenting my journey of learning **Agentic AI, LangGraph, LangChain, and Multi-Agent Systems using Python**.

The goal of this repository is not just to learn frameworks, but to understand the core concepts behind AI agents and gradually build **production-ready multi-agent applications**.

---

## 🎯 Learning Goals

Through this repository, I aim to understand:

* Python fundamentals required for Agentic AI
* LLM fundamentals
* Structured LLM outputs
* Tool / Function Calling
* LangChain fundamentals
* LangGraph workflows
* State management
* Conditional routing
* Agent memory
* Human-in-the-loop workflows
* RAG and Agentic RAG
* Multi-Agent architectures
* Production-ready AI agent systems

---

# 📚 Learning Roadmap

```text
Python for Agentic AI
        ↓
LLM Fundamentals
        ↓
LLM APIs
        ↓
Prompting & Messages
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
Production Project
```

---

# 🐍 Chapter 01 — Python for Agentic AI

The first phase focuses only on the Python concepts required to understand and build AI agent systems.

## Topics Covered

* Variables and Data Types
* Lists and Dictionaries
* Loops
* Functions
* Parameters and Return Values
* Type Hints
* `TypedDict`
* State Management
* Agent-to-Agent Data Flow
* Conditional Routing
* Retry Loops
* Maximum Attempt Handling
* Python Classes
* Pydantic
* `BaseModel`
* `Literal`
* `Field`
* Runtime Validation
* Exception Handling
* Modules and Imports
* Environment Variables
* `.env` Configuration
* `async` / `await`
* `asyncio`
* Concurrent Operations with `asyncio.gather()`

---

# 🧠 Understanding Agent State

One of the first concepts explored in this repository is **shared agent state**.

Example:

```python
from typing import TypedDict


class AgentState(TypedDict):
    task: str
    research: str | None
    content: str | None
    review: str | None
```

The state can be shared across different workflow steps:

```text
User Task
    ↓
Researcher
    ↓
Research Result
    ↓
Writer
    ↓
Generated Content
    ↓
Reviewer
    ↓
Final Result
```

This provides the foundation for understanding state-based workflows in LangGraph.

---

# 🔀 Conditional Agent Workflows

I also explored how agents can make decisions based on the current state.

Example workflow:

```text
START
  ↓
Developer
  ↓
Tester
  ↓
Tests Passed?
 /          \
YES          NO
 ↓            ↓
END       Developer
              ↑
              └── Retry
```

This introduced concepts such as:

* Conditional routing
* Retry workflows
* Termination conditions
* Maximum retry limits
* Preventing infinite loops

These concepts will later be implemented using **LangGraph conditional edges**.

---

# 🔄 Agent Communication

Instead of agents working independently, agents can consume outputs produced by previous agents.

Example:

```text
Researcher
    │
    │ research
    ▼
Writer
    │
    │ content
    ▼
Reviewer
    │
    │ review
    ▼
Final State
```

This helped me understand how shared state can be used for communication between specialized agents.

---

# 📦 Structured Data with Pydantic

Pydantic is used to define and validate structured data.

Example:

```python
from typing import Literal

from pydantic import BaseModel, Field


class TaskDecision(BaseModel):

    agent: Literal[
        "researcher",
        "developer",
        "reviewer"
    ]

    reason: str

    priority: int = Field(
        ge=1,
        le=5
    )
```

This provides:

* Runtime validation
* Controlled agent selection
* Structured data
* Type-safe outputs

Later, this concept will be used for **structured LLM outputs and agent routing decisions**.

---

# ⚠️ Error Handling

AI systems interact with external services such as:

* LLM APIs
* Search APIs
* Databases
* External tools

These services can fail.

To handle failures safely, I explored:

```python
try:
    result = search_tool()

except Exception as error:
    print(error)
```

Instead of crashing the entire workflow, agents can store errors in state and decide whether to:

```text
Retry
Fallback
Continue
Terminate
```

---

# 🔐 Environment Variables

Secrets such as API keys should never be hardcoded.

Environment variables are loaded using:

```python
from dotenv import load_dotenv

load_dotenv()
```

Example `.env`:

```text
AI_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore`.

An `.env.example` file can be committed instead:

```text
AI_API_KEY=
```

---

# ⚡ Asynchronous Agent Execution

Many AI operations are I/O-bound:

* LLM requests
* Search APIs
* Database queries
* External tools

Python's `async/await` allows other async tasks to make progress while waiting for these operations.

Example:

```python
async def research_agent():

    await asyncio.sleep(2)

    return "Research completed"
```

Independent agents can also run concurrently:

```python
research, news, docs = await asyncio.gather(
    research_agent(),
    news_agent(),
    docs_agent()
)
```

Conceptually:

```text
               Main
                │
       ┌────────┼────────┐
       ↓        ↓        ↓
   Research    News     Docs
    Agent      Agent    Agent
       │        │        │
       └────────┼────────┘
                ↓
          Combined Result
```

---

# 🗂️ Repository Structure

```text
agentic-ai-langgraph-learning/
│
├── 01_python_for_agents/
│   │
│   ├── 01_state_basics.py
│   ├── 02_functions.py
│   ├── 03_typed_state.py
│   ├── 04_conditional_routing.py
│   ├── 05_pydantic_task.py
│   ├── 06_exception_handling.py
│   ├── 08_async_await.py
│   │
│   └── 07_modules_and_env/
│       │
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── researcher.py
│       │   └── writer.py
│       │
│       ├── .env.example
│       ├── .gitignore
│       └── main.py
│
├── README.md
└── requirements.txt
```

> The repository structure will continue to evolve as new concepts and projects are added.

---

# 🛠️ Setup

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project:

```bash
cd agentic-ai-langgraph-learning
```

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📦 Current Dependencies

```text
pydantic
python-dotenv
```

More dependencies will be added as the repository progresses into LangChain and LangGraph.

---

# 🗺️ Upcoming Chapters

## Chapter 02 — LLM Fundamentals

* What is an LLM?
* Tokens
* Context Window
* Temperature
* System Messages
* User Messages
* AI Messages
* Prompting
* LLM API Calls
* Structured Outputs
* Tool Calling

## Chapter 03 — LangChain

* Models
* Messages
* Prompt Templates
* Structured Output
* Tools
* `@tool`
* Tool Calling

## Chapter 04 — LangGraph

* StateGraph
* State
* Nodes
* Edges
* `START`
* `END`
* `compile()`
* `invoke()`
* Conditional Edges
* Cycles and Retry Workflows

## Chapter 05 — Agents

* Agent Architecture
* ReAct Pattern
* ToolNode
* Agent Loops
* Multiple Tools
* Error Handling

## Chapter 06 — Memory

* Short-Term Memory
* MessagesState
* Reducers
* Checkpointers
* Conversation Threads
* Persistent State

## Chapter 07 — RAG & Agentic RAG

* Embeddings
* Vector Databases
* Retrieval
* RAG
* Retrieval Tools
* Agentic RAG

## Chapter 08 — Multi-Agent Systems

* Specialized Agents
* Shared State
* Supervisor Architecture
* Router Architecture
* Agent Handoffs
* Subgraphs
* Hierarchical Agent Systems
* Parallel Agent Execution

## Chapter 09 — Production

* FastAPI Integration
* Streaming
* Persistence
* Logging
* Observability
* LangSmith
* Error Handling
* Retry Strategies
* Cost Control
* Security
* Deployment

---

# 🚀 Final Goal

The final goal of this learning journey is to build a **production-grade multi-agent AI system** where specialized agents can:

```text
Understand a task
      ↓
Plan the work
      ↓
Select appropriate agents
      ↓
Use external tools
      ↓
Collaborate through shared state
      ↓
Review generated work
      ↓
Retry when necessary
      ↓
Maintain memory
      ↓
Return the final result
```

Rather than treating AI agents as simple LLM wrappers, this repository focuses on understanding the engineering concepts required to build **reliable, stateful and scalable agentic workflows**.

---

## 📈 Current Progress

```text
Python for Agentic AI       ██████████ 100% ✅
LLM Fundamentals            ░░░░░░░░░░ Upcoming
LangChain                   ░░░░░░░░░░ Upcoming
LangGraph                   ░░░░░░░░░░ Upcoming
Agents & Tools              ░░░░░░░░░░ Upcoming
Memory                      ░░░░░░░░░░ Upcoming
RAG                         ░░░░░░░░░░ Upcoming
Multi-Agent Systems         ░░░░░░░░░░ Upcoming
Production                  ░░░░░░░░░░ Upcoming
```

---

## 👨‍💻 Author

**Saumya Sharma**

Learning and building in:

`Agentic AI` • `LangGraph` • `LangChain` • `Python` • `LLMs` • `Multi-Agent Systems`

---

⭐ If you find this learning journey useful, feel free to star the repository and follow along as I continue building more advanced Agentic AI systems.
