from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser


load_dotenv()


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful programming teacher."
    ),
    (
        "human",
        "Explain {topic} in exactly 3 simple points."
    )
])


parser = StrOutputParser()


# -----------------------------
# Prompt
# -----------------------------

prompt_value = prompt.invoke({
    "topic": "JWT"
})


print("STEP 1 - PROMPT:")
print(prompt_value)


# -----------------------------
# Model
# -----------------------------

response = model.invoke(prompt_value)


print("\nSTEP 2 - MODEL:")
print(response)


# -----------------------------
# Parser
# -----------------------------

result = parser.invoke(response)


print("\nSTEP 3 - PARSER:")
print(result)


print("\nFINAL TYPE:")
print(type(result))