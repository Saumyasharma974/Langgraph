# import os

# from dotenv import load_dotenv

# from langchain_groq import ChatGroq

# from langchain_core.messages import (
#     SystemMessage,
#     HumanMessage,
# )


# # --------------------------------
# # 1. Load environment variables
# # --------------------------------

# load_dotenv()


# # --------------------------------
# # 2. Get Groq API key
# # --------------------------------

# api_key = os.getenv("GROQ_API_KEY")

# if not api_key:
#     raise ValueError("GROQ_API_KEY is missing")


# # --------------------------------
# # 3. Create LLM
# # --------------------------------

# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     groq_api_key=api_key,
#     temperature=0
# )


# # --------------------------------
# # 4. Create messages
# # --------------------------------

# messages = [

#     SystemMessage(
#         content=(
#             "You are an expert Python teacher. "
#         )
#     ),

#     HumanMessage(
#         content="Explain Recursion."
#     )
# ]


# # --------------------------------
# # 5. Send messages to LLM
# # --------------------------------

# response = llm.invoke(messages)


# # --------------------------------
# # 6. Print AI response
# # --------------------------------

# print("\nAI Response:")

# print(response.content)

import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=api_key,
    temperature=0
)


messages = [
    SystemMessage(
        content="You are an expert Python teacher. Explain in simple Hinglish."
    )
]


# -------------------------------
# First question
# -------------------------------

messages.append(
    HumanMessage(
        content="What is async/await?"
    )
)

response = llm.invoke(messages)

print("AI:", response.content)


# Add AI response to conversation
messages.append(response)


# -------------------------------
# Second question
# -------------------------------

messages.append(
    HumanMessage(
        content="Give me a simple example."
    )
)

response = llm.invoke(messages)

print("\nAI:", response.content)