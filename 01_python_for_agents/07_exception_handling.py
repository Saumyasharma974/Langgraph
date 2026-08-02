# File: 06_exception_handling.py

from typing import TypedDict


# --------------------------------
# 1. Define Agent State
# --------------------------------

class AgentState(TypedDict):
    task: str
    result: str | None
    status: str
    error: str | None


# --------------------------------
# 2. Initial State
# --------------------------------

state: AgentState = {
    "task": "Search information about LangGraph",
    "result": None,
    "status": "pending",
    "error": None
}


# --------------------------------
# 3. Fake Search Tool
# --------------------------------

def search_tool(query: str) -> str:

    print("Searching for:", query)

    return "LangGraph information found"


# --------------------------------
# 4. Researcher Agent
# --------------------------------

def researcher(state: AgentState) -> AgentState:

    print("\nResearcher is working...")

    try:

        # Read task from state
        task = state["task"]

        # Call search tool
        result = search_tool(task)

        # Store successful result
        state["result"] = result
        state["status"] = "success"
        state["error"] = None

    except Exception as e:

        # Store error information
        state["result"] = None
        state["status"] = "failed"
        state["error"] = str(e)

    return state


# --------------------------------
# 5. Execute Agent
# --------------------------------

state = researcher(state)


# --------------------------------
# 6. Print Final State
# --------------------------------

print("\nFinal State:")
print(state)