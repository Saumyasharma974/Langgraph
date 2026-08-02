from typing import TypedDict


class AgentState(TypedDict):
    task: str
    code: str | None
    test_result: str | None
    status: str
    attempts: int


state: AgentState = {
    "task": "Build authentication API",
    "code": None,
    "test_result": None,
    "status": "pending",
    "attempts": 0
}


def developer(state: AgentState) -> AgentState:

    print("\nDeveloper is working...")

    state["attempts"] += 1

    print("Attempt:", state["attempts"])

    if state["attempts"] == 1:
        state["code"] = "Authentication code v1"
    else:
        state["code"] = "Authentication code v2"

    print("Generated:", state["code"])

    return state


def tester(state: AgentState) -> AgentState:

    print("\nTester is working...")

    code = state["code"]

    print("Testing:", code)

    if code == "Authentication code v2":

        state["test_result"] = "Tests passed"
        state["status"] = "passed"

    else:

        state["test_result"] = "Tests failed"
        state["status"] = "failed"

    print(state["test_result"])

    return state


def decide_next_action(state: AgentState) -> str:

    if state["status"] == "passed":
        return "end"

    return "developer"


MAX_ATTEMPTS = 3


while state["attempts"] < MAX_ATTEMPTS:

    state = developer(state)

    state = tester(state)

    route = decide_next_action(state)

    if route == "end":

        print("\nWorkflow completed!")
        break

    print("\nRetrying...")


print("\nFinal State:")
print(state)