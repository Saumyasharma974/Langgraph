# state = {
#     "task": "Research about LangGraph",
#     "plan": None,
#     "research": None,
#     "review": None
# }


# def planner(state: dict) -> dict:

#     print("Planner is working...")

#     state["plan"] = "Research LangGraph fundamentals"

#     return state


# def researcher(state: dict) -> dict:

#     print("Researcher is working...")

#     task = state["task"]

#     print("Researching:", task)

#     state["research"] = "LangGraph research completed"

#     return state


# def reviewer(state: dict) -> dict:

#     print("Reviewer is working...")

#     state["review"] = "Research approved"

#     return state


# state = planner(state)

# state = researcher(state)

# state = reviewer(state)


# print("\nFinal State:")

# print(state)




state = {
    "task": "Build AI chatbot",
    "plan": None,
    "code": None,
    "test_result": None
}

def planner(state:dict) -> dict:

    print("Planner is working...")

    state["plan"] = "Build AI chatbot"

    return state

def coder(state:dict) -> dict:

    print("Coder is working...")

    task = state["task"]

    print("Coding:", task)

    state["code"] = "AI chatbot code completed"

    return state

def tester(state:dict) -> dict:

    print("Tester is working...")

    task = state["task"]

    print("Testing:", task)

    state["test_result"] = "AI chatbot code tested"

    return state



state = planner(state)

state = coder(state)

state = tester(state)

print("\nFinal State:")
print(state)
