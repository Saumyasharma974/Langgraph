import os
import asyncio

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
# 3. Async LLM Function
# ==========================================

async def ask_llm():

    response = await llm.ainvoke(
        "Explain how JWT authentication works in simple language."
    )

    return response


# ==========================================
# 4. Main Function with Timeout
# ==========================================

async def main():

    try:

        response = await asyncio.wait_for(
            ask_llm(),
            timeout=5
        )

        print("\nLLM Response:")
        print(response.content)

    except asyncio.TimeoutError:

        print("\nLLM request timed out.")

    except Exception as e:

        print("\nLLM request failed:")
        print(e)


# ==========================================
# 5. Run Program
# ==========================================

asyncio.run(main())