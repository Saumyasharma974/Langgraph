# def divide(a, b):
#     return a / b


# try:
#     a = float(input("Enter a: "))
#     b = float(input("Enter b: "))

#     result = divide(a, b)

#     print("Result:", result)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# except ValueError:
#     print("Please enter valid numbers.")


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

try:
    response=llm.invoke("Hi")
    print(response.content)
except Exception as e:
    print(e)