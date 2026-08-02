from typing import TypedDict


class AgentState(TypedDict):
    task: str
    plan: str | None
    code: str | None
    test_result: str | None
    
state: AgentState = {
    "task": "Build AI chatbot",
    "plan": "",
    "code": "",
    "test_result": ""
}


def planner(state: AgentState) -> AgentState:

    print("Planner is working...")

    state["plan"] = "Create chatbot architecture"

    return state


def developer(state: AgentState) -> AgentState:

    print("Developer is working...")

    plan = state["plan"]

    print("Following plan:", plan)

    state["code"] = "Chatbot code generated"

    return state


def tester(state: AgentState) -> AgentState:

    print("Tester is working...")

    code = state["code"]

    print("Testing:", code)

    state["test_result"] = "All tests passed"

    return state


state = planner(state)
state = developer(state)
state = tester(state)


print("\nFinal State:")
print(state)