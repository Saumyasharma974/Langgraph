import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0
)


# ==========================================
# Prompt V1
# ==========================================

response1 = llm.invoke(
    "Explain JWT authentication in complete detail."
)

usage1 = response1.response_metadata["token_usage"]


# ==========================================
# Prompt V2
# ==========================================

response2 = llm.invoke(
    "Explain JWT authentication in exactly 5 concise bullet points."
)

usage2 = response2.response_metadata["token_usage"]


# ==========================================
# Results
# ==========================================

print("=" * 50)
print("PROMPT V1")
print("=" * 50)

print(response1.content)

print("\nToken Usage:")
print(usage1)


print("\n" + "=" * 50)
print("PROMPT V2")
print("=" * 50)

print(response2.content)

print("\nToken Usage:")
print(usage2)


print("\n" + "=" * 50)
print("COMPARISON")
print("=" * 50)

print("V1 Total Tokens:", usage1["total_tokens"])
print("V2 Total Tokens:", usage2["total_tokens"])

print(
    "Tokens Saved:",
    usage1["total_tokens"] - usage2["total_tokens"]
)