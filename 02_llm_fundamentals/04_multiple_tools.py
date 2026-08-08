import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool


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
    """Get the current weather of a city."""

    # Fake data for learning
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

    # Fake search result for learning
    return f"Information found about {topic}"


# --------------------------------
# 5. Put all tools in a list
# --------------------------------

tools = [
    calculator,
    get_weather,
    search_topic
]


# --------------------------------
# 6. Bind tools to LLM
# --------------------------------

llm_with_tools = llm.bind_tools(tools)


# --------------------------------
# 7. User question
# --------------------------------

user_question = "What is the weather in Delhi?"


# --------------------------------
# 8. Ask LLM
# --------------------------------

response = llm_with_tools.invoke(
    user_question
)


# --------------------------------
# 9. Check tool calls
# --------------------------------

print("\nAI Tool Calls:")

print(response.tool_calls)


# --------------------------------
# 10. Execute selected tools
# --------------------------------

for tool_call in response.tool_calls:

    tool_name = tool_call["name"]

    tool_args = tool_call["args"]

    print("\nSelected Tool:", tool_name)

    print("Arguments:", tool_args)


    if tool_name == "calculator":

        result = calculator.invoke(tool_args)


    elif tool_name == "get_weather":

        result = get_weather.invoke(tool_args)


    elif tool_name == "search_topic":

        result = search_topic.invoke(tool_args)


    else:

        result = "Unknown tool"


    print("Tool Result:", result)