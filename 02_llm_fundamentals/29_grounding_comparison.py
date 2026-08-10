import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage


# ==========================================
# 1. Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


# ==========================================
# 2. Create LLM
# ==========================================

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0
)


# ==========================================
# 3. Context
# ==========================================

context = """
Our company provides 24 paid leaves per year.
Employees can carry forward up to 10 unused leaves.
"""


question = "How many paid leaves does the company provide?"


# ==========================================
# 4. Ungrounded Response
# ==========================================

print("=" * 60)
print("UNGROUNDED RESPONSE")
print("=" * 60)

ungrounded_response = llm.invoke(
    question
)

print(ungrounded_response.content)


# ==========================================
# 5. Grounded Response
# ==========================================

print("\n" + "=" * 60)
print("GROUNDED RESPONSE")
print("=" * 60)

grounded_system_prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the provided context.

CONTEXT:
{context}

Rules:
- Do not use outside knowledge.
- Do not make up information.
- If the answer is not present in the context,
  say: "I don't have enough information."
"""

messages = [
    SystemMessage(content=grounded_system_prompt),
    HumanMessage(content=question)
]

grounded_response = llm.invoke(messages)

print(grounded_response.content)