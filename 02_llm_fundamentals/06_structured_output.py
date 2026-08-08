# 06_structured_output.py

import os

from dotenv import load_dotenv

from pydantic import BaseModel, Field

from typing import Literal

from langchain_groq import ChatGroq


# --------------------------------
# 1. Load environment variables
# --------------------------------

load_dotenv()


# --------------------------------
# 2. Get API key
# --------------------------------

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


# --------------------------------
# 3. Create LLM
# --------------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=api_key,
    temperature=0
)


# --------------------------------
# 4. Define structured output
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
# 5. Connect LLM with schema
# --------------------------------

structured_llm = llm.with_structured_output(
    TaskDecision
)


# --------------------------------
# 6. Give task to LLM
# --------------------------------

task = """
Build a login API using FastAPI.
The API should support user registration,
login and JWT authentication.
"""


# --------------------------------
# 7. Get structured response
# --------------------------------

result = structured_llm.invoke(
    task
)


# --------------------------------
# 8. Print result
# --------------------------------

print("\nStructured Result:")

print(result)


# --------------------------------
# 9. Access individual fields
# --------------------------------

print("\nAgent:", result.agent)

print("Reason:", result.reason)

print("Priority:", result.priority)