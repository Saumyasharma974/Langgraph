import os
import time

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
# 3. Retry Configuration
# ==========================================

max_attempts = 3


# ==========================================
# 4. LLM Call with Exponential Backoff
# ==========================================

for attempt in range(1, max_attempts + 1):

    print(f"\nAttempt {attempt}")

    try:
        response = llm.invoke(
            "Explain JWT authentication in simple language."
        )

        print("\nLLM Response:")
        print(response.content)

        print("\nRequest successful!")
        break

    except Exception as e:

        print(f"Request failed: {e}")

        if attempt == max_attempts:
            print("\nMaximum retry attempts reached.")
            print("Request failed permanently.")

        else:
            delay = 2 ** (attempt - 1)

            print(f"Retrying in {delay} seconds...")

            time.sleep(delay)