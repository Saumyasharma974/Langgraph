# from pydantic import BaseModel


# class RouterDecision(BaseModel):
#     agent: str
#     reason: str


# decision = RouterDecision(
#     agent="researcher",
#     reason="The task requires research"
# )


# print("Selected Agent:", decision.agent)

# print("Reason:", decision.reason)

from typing import Literal
from pydantic import BaseModel, Field


# --------------------------------
# 1. Create Pydantic Model
# --------------------------------

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


# --------------------------------
# 2. Create Object
# --------------------------------

decision = TaskDecision(
    agent="developer",
    reason="User wants an API",
    priority=10
)


# --------------------------------
# 3. Access Values
# --------------------------------

print("Selected Agent:", decision.agent)

print("Reason:", decision.reason)

print("Priority:", decision.priority)


# --------------------------------
# 4. Convert Pydantic Model to Dict
# --------------------------------

data = decision.model_dump()

print("\nDictionary:")
print(data)