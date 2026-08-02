from typing import TypedDict


# --------------------------------
# 1. Define State
# --------------------------------

class AgentState(TypedDict):
    task: str
    research: str | None
    content: str | None
    review: str | None


# --------------------------------
# 2. Initial State
# --------------------------------

state: AgentState = {
    "task": "Write article about Agentic AI",
    "research": None,
    "content": None,
    "review": None
}


# --------------------------------
# 3. Researcher Agent
# --------------------------------

def researcher(state: AgentState) -> AgentState:

    print("Researcher is working...")

    # Read task from state
    task = state["task"]

    print("Researching:", task)

    # Update research
    state["research"] = "Agentic AI research completed"

    return state


# --------------------------------
# 4. Writer Agent
# --------------------------------

def writer(state: AgentState) -> AgentState:

    print("\nWriter is working...")

    # Read researcher's output
    research = state["research"]

    print("Writing using research:", research)

    # Update content
    state["content"] = "Agentic AI article generated"

    return state


# --------------------------------
# 5. Reviewer Agent
# --------------------------------

def reviewer(state: AgentState) -> AgentState:

    print("\nReviewer is working...")

    # Read writer's output
    content = state["content"]

    print("Reviewing content:", content)

    # Update review
    state["review"] = "Article approved"

    return state


# --------------------------------
# 6. Execute Workflow
# --------------------------------

state = researcher(state)

state = writer(state)

state = reviewer(state)


# --------------------------------
# 7. Final State
# --------------------------------

print("\nFinal State:")

print(state)