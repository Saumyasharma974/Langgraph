# import asyncio
# import time


# async def research_task():
#     await asyncio.sleep(3)
#     return "Research completed"


# async def examples_task():
#     await asyncio.sleep(2)
#     return "Examples completed"


# # async def main():

# #     start = time.perf_counter()

# #     result1 = await research_task()
# #     result2 = await examples_task()

# #     end = time.perf_counter()

# #     print(result1)
# #     print(result2)

# #     print(f"Sequential Time: {end - start:.2f} seconds")

# async def main():

#     start = time.perf_counter()

#     results = await asyncio.gather(
#         research_task(),
#         examples_task()
#     )

#     end = time.perf_counter()

#     print(results[0])
#     print(results[1])

#     print(f"Parallel Time: {end - start:.2f} seconds")
# asyncio.run(main())\



import os
import asyncio
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
# 3. LLM Task 1
# ==========================================

async def explain_jwt():

    response = await llm.ainvoke(
        "Explain JWT authentication in 3 concise bullet points."
    )

    return response.content


# ==========================================
# 4. LLM Task 2
# ==========================================

async def explain_oauth():

    response = await llm.ainvoke(
        "Explain OAuth authentication in 3 concise bullet points."
    )

    return response.content


# ==========================================
# 5. Parallel Execution
# ==========================================

async def main():

    start = time.perf_counter()

    results = await asyncio.gather(
        explain_jwt(),
        explain_oauth()
    )

    end = time.perf_counter()

    print("=" * 50)
    print("JWT")
    print("=" * 50)
    print(results[0])

    print("\n" + "=" * 50)
    print("OAUTH")
    print("=" * 50)
    print(results[1])

    print("\n" + "=" * 50)
    print("PERFORMANCE")
    print("=" * 50)

    print(f"Total Time: {end - start:.2f} seconds")


# ==========================================
# 6. Run
# ==========================================

asyncio.run(main())