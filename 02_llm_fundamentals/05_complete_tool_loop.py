import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.tools import tool

from langchain_core.messages import (
    HumanMessage,
    ToolMessage,
)


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
# 4. Create Tools
# --------------------------------

@tool
def calculator(a: float, b: float) -> float:
    """Multiply two numbers."""

    return a * b


@tool
def get_weather(city: str) -> str:
    """Get the weather of a city."""

    weather_data = {
        "Delhi": "32°C and sunny",
        "Mumbai": "29°C and cloudy",
        "Bangalore": "24°C and rainy"
    }

    return weather_data.get(
        city,
        "Weather information not available"
    )


@tool
def search_topic(topic: str) -> str:
    """Search for information about a topic."""

    return f"Information found about {topic}"


# --------------------------------
# 5. Tool Registry
# --------------------------------

tools = [
    calculator,
    get_weather,
    search_topic
]

tool_registry = {
    "calculator": calculator,
    "get_weather": get_weather,
    "search_topic": search_topic
}


# --------------------------------
# 6. Bind tools to LLM
# --------------------------------

llm_with_tools = llm.bind_tools(tools)


# --------------------------------
# 7. User message
# --------------------------------

user_message = HumanMessage(
    content="What is the weather in Delhi?"
)


# --------------------------------
# 8. First LLM call
# --------------------------------

ai_response = llm_with_tools.invoke(
    [user_message]
)


print("\nAI Response:")
print(ai_response.content)

print("\nTool Calls:")
print(ai_response.tool_calls)


# --------------------------------
# 9. Execute tool calls
# --------------------------------

tool_messages = []

for tool_call in ai_response.tool_calls:

    tool_name = tool_call["name"]

    tool_args = tool_call["args"]

    print("\nSelected Tool:", tool_name)

    print("Arguments:", tool_args)


    # Find selected tool
    selected_tool = tool_registry.get(tool_name)


    if selected_tool is None:

        print("Tool not found")

        continue


    # Execute tool
    result = selected_tool.invoke(
        tool_args
    )


    print("Tool Result:", result)


    # --------------------------------
    # 10. Create ToolMessage
    # --------------------------------

    tool_message = ToolMessage(
        content=str(result),
        tool_call_id=tool_call["id"]
    )


    tool_messages.append(tool_message)


# --------------------------------
# 11. Create complete conversation
# --------------------------------

messages = [
    user_message,
    ai_response,
    *tool_messages
]


# --------------------------------
# 12. Final LLM call
# --------------------------------

final_response = llm_with_tools.invoke(
    messages
)


# --------------------------------
# 13. Final Answer
# --------------------------------

print("\nFinal AI Answer:")

print(final_response.content)