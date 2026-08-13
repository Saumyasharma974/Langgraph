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
        "Explain {topic} in simple language."
    )
])


parser = StrOutputParser()


# -----------------------------
# Step 1: Create Prompt
# -----------------------------

prompt_value = prompt.invoke({
    "topic": "JWT"
})


print("PROMPT:")
print(prompt_value)


# -----------------------------
# Step 2: Invoke Model
# -----------------------------

response = model.invoke(prompt_value)


print("\nRAW MODEL RESPONSE:")
print(response)

print("\nRAW RESPONSE TYPE:")
print(type(response))


# -----------------------------
# Step 3: Parse Response
# -----------------------------

result = parser.invoke(response)


print("\nPARSED RESPONSE:")
print(result)

print("\nPARSED RESPONSE TYPE:")
print(type(result))

print("\nIS STRING:")
print(isinstance(result, str))