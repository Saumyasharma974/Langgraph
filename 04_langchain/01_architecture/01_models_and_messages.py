import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)


# ==========================================
# 1. Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


# ==========================================
# 2. Create Chat Model
# ==========================================

model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0,
)


# ==========================================
# 3. Create Messages
# ==========================================

messages = [
    SystemMessage(
        content="You are a helpful programming teacher."
    ),
    HumanMessage(
        content="Explain what LangChain is in simple words."
    ),
]


# ==========================================
# 4. Invoke Model
# ==========================================

response = model.invoke(messages)


# ==========================================
# 5. Inspect Response
# ==========================================

print("\nMESSAGE TYPE:")
print(type(response))

print("\nCONTENT:")
print(response.content)

print("\nUSAGE:")
print(response.usage_metadata)

print("\nTOOL CALLS:")
print(response.tool_calls)

print("\nRESPONSE METADATA:")
print(response.response_metadata)