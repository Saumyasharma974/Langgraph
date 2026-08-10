import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


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
# 3. Make LLM Call
# ==========================================

response = llm.invoke(
    "Explain JWT authentication in simple language."
)


# ==========================================
# 4. Print Response
# ==========================================

print("Response:")
print(response.content)


# ==========================================
# 5. Print Response Metadata
# ==========================================

print("\nResponse Metadata:")
print(response.response_metadata)