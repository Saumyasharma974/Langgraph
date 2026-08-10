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
# 3. Rate Limit Configuration
# ==========================================

RATE_LIMIT = 3


# ==========================================
# 4. LLM Requests
# ==========================================

for request_number in range(1, 6):

    print(f"\nRequest {request_number}")

    if request_number <= RATE_LIMIT:

        try:
            response = llm.invoke(
                "Explain JWT authentication in one simple sentence."
            )

            print("Status: Approved ✅")
            print("Response:", response.content)

        except Exception as e:

            print("LLM request failed ❌")
            print("Error:", e)

    else:

        print("Status: Rate limit exceeded ❌")
        print("Request blocked.")