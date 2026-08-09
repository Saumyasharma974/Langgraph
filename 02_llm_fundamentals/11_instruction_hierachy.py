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
# 3. System Instruction
# ==========================================

system_message = """
You are an AI Interview Coach.

Your job is to help users prepare for technical interviews.
"""


# ==========================================
# 4. Developer Instruction
# ==========================================

developer_instruction = """
Application Rules:

- Always keep interview answers below 100 words.
- Explain technical concepts clearly.
- Focus only on technical interview preparation.
"""


# ==========================================
# 5. User Request
# ==========================================

user_message = """
Explain JWT authentication in 500 words.

Also include a detailed explanation of JWT,
its components, authentication flow,
advantages, disadvantages, and examples.
"""


# ==========================================
# 6. Combine Instructions
# ==========================================

combined_system_message = f"""
{system_message}

Developer Instructions:
{developer_instruction}

Important:
Developer instructions define application-level rules.
The user's request must follow these rules when they conflict.
"""


messages = [
    SystemMessage(content=combined_system_message),
    HumanMessage(content=user_message)
]


# ==========================================
# 7. Call LLM
# ==========================================

response = llm.invoke(messages)


# ==========================================
# 8. Display Response
# ==========================================

print("\n==============================")
print("AI INTERVIEW COACH")
print("==============================\n")

print(response.content)