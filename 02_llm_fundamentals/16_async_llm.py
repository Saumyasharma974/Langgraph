import os
import asyncio

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage


# ==========================================
# 1. Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found in environment variables")


# ==========================================
# 2. Create LLM
# ==========================================

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0
)


# ==========================================
# 3. Async Streaming LLM Call
# ==========================================

async def explain_topic(topic):

    prompt = f"""
You are a backend teacher.

Explain the topic "{topic}" in a simple and concise manner.

Requirements:
- Assume the learner is a beginner.
- Use simple language.
- Explain important concepts clearly.
- Give a practical understanding.
"""

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=f"Explain {topic}.")
    ]

    full_response = ""

    async for chunk in llm.astream(messages):

        print(chunk.content, end="", flush=True)

        full_response += chunk.content

    return full_response


# ==========================================
# 4. Async Normal LLM Call
# ==========================================

async def give_examples(topic):

    prompt = f"""
You are a backend teacher.

Give real-world examples for the topic "{topic}"
in a simple and concise manner.

Requirements:
- Give beginner-friendly examples.
- Explain each example briefly.
- Use practical examples.
"""

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=f"Give real-world examples of {topic}.")
    ]

    response = await llm.ainvoke(messages)

    return response.content


# ==========================================
# 5. Run Both Tasks Concurrently
# ==========================================

async def main():

    results = await asyncio.gather(
        explain_topic("JWT"),
        give_examples("JWT")
    )

    return results


# ==========================================
# 6. Run Async Program
# ==========================================

results = asyncio.run(main())


# ==========================================
# 7. Display Final Results
# ==========================================

print("\n\n")
print("=" * 50)
print("COMPLETE EXPLANATION")
print("=" * 50)

print(results[0])

print("\n\n")
print("=" * 50)
print("REAL-WORLD EXAMPLES")
print("=" * 50)

print(results[1])