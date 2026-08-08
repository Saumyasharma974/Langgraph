import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# --------------------------------
# 1. Load environment variables
# --------------------------------

load_dotenv()


# --------------------------------
# 2. Get Groq API key
# --------------------------------

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


print("Groq API key loaded successfully")


# --------------------------------
# 3. Create Groq LLM
# --------------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=api_key,
    temperature=0
)


# --------------------------------
# 4. Send prompt to LLM
# --------------------------------

response = llm.invoke(
    # "Explain Agentic AI in simple language in 3 lines."
    # "You are a Python teacher. Explain async await ."

     "Write a Python function to reverse a string."
)


# --------------------------------
# 5. Print response
# --------------------------------

print("\nAI Response:")

print(response.content)