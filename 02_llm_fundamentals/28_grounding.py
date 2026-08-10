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
# 3. Verified Context
# ==========================================

context = """
Our company provides 24 paid leaves per year.
Employees can carry forward up to 10 unused leaves.
"""


# ==========================================
# 4. Grounded Question Function
# ==========================================

def ask_grounded_question(question):

    system_prompt = f"""
You are a helpful assistant.

Answer the user's question using ONLY the provided context.

CONTEXT:
{context}

Rules:
- Do not use outside knowledge.
- Do not make up information.
- If the answer is not present in the context,
  say: "I don't have enough information."
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=question)
    ]

    response = llm.invoke(messages)

    return response.content


# ==========================================
# 5. Test 1 — Information exists
# ==========================================

question1 = "How many paid leaves does the company provide?"

print("=" * 50)
print("QUESTION 1")
print("=" * 50)

print("Question:", question1)
print("\nAnswer:")
print(ask_grounded_question(question1))


# ==========================================
# 6. Test 2 — Information does NOT exist
# ==========================================

question2 = "How many sick leaves does the company provide?"

print("\n" + "=" * 50)
print("QUESTION 2")
print("=" * 50)

print("Question:", question2)
print("\nAnswer:")
print(ask_grounded_question(question2))