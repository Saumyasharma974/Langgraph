task=" Build login api"

agents = [
    "planner",
    "developer",
    "writer",
    "reviewer"
]

state = {
    "task": task,
    "current_agent": "planner",
    "completed": False,
    "result": None
}

print("Task:", state["task"])
print("Current Agent:", state["current_agent"])

print("\nAvailable Agents:")

for agent in agents:
    print("-", agent)

state["current_agent"] = "writer"

print("\nNew Current Agent:", state["current_agent"])

state["result"] = "Research completed"
state["completed"] = True

print("\nFinal State:")
print(state)