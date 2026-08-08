import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage


# --------------------------------
# 1. Load environment variables
# --------------------------------

load_dotenv()


# --------------------------------
# 2. Get API key
# --------------------------------

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


# --------------------------------
# 3. Create LLM
# --------------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=api_key,
    temperature=0
)


# --------------------------------
# 4. Create Tool
# --------------------------------

@tool
def calculator(a: float, b: float) -> float:
    """Multiply two numbers."""

    return a * b


# --------------------------------
# 5. Bind Tool to LLM
# --------------------------------

llm_with_tools = llm.bind_tools(
    [calculator]
)


# --------------------------------
# 6. User Question
# --------------------------------

user_question = "What is 25 multiplied by 4?"


# --------------------------------
# 7. First LLM Call
# --------------------------------

response = llm_with_tools.invoke(
    user_question
)


print("\nAI Tool Call:")
print(response.tool_calls)


# --------------------------------
# 8. Get Tool Call
# --------------------------------

tool_call = response.tool_calls[0]
print(tool_call)


# --------------------------------
# 9. Execute Tool
# --------------------------------

tool_result = calculator.invoke(
    tool_call["args"]
)


print("\nTool Result:")
print(tool_result)


# --------------------------------
# 10. Create ToolMessage
# --------------------------------

tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call["id"]
)


# --------------------------------
# 11. Send Tool Result back to LLM
# --------------------------------

messages = [
    user_question,
    response,
    tool_message
]


final_response = llm_with_tools.invoke(
    messages
)


# --------------------------------
# 12. Final Answer
# --------------------------------

print("\nFinal AI Answer:")
print(final_response.content)