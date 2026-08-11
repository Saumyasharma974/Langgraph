import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage


# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


# Create model
model = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0
)


# Create prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant."
    ),
    (
        "placeholder",
        "{history}"
    ),
    (
        "human",
        "{question}"
    )
])


# Previous conversation
history = [
    HumanMessage(content="My name is Saumya."),
    AIMessage(content="Nice to meet you, Saumya."),
    HumanMessage(content="I am learning Agentic AI."),
    AIMessage(content="That's great!")
]


# Create messages
messages = prompt.invoke({
    "history": history,
    "question": "What am i learning?"
})


print("MESSAGES:")
print(messages)


# Send messages to LLM
response = model.invoke(messages)


print("\nAI RESPONSE:")
print(response.content)