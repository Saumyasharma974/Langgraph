from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()


# -----------------------------
# MODEL
# -----------------------------

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)


# -----------------------------
# PROMPT
# -----------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a programming teacher."
    ),
    (
        "human",
        "Explain {topic} in simple language."
    )
])


# -----------------------------
# PARSER
# -----------------------------

parser = StrOutputParser()


# -----------------------------
# OUR PYTHON FUNCTION
# -----------------------------

def clean_response(text):
    return text.strip()


# Convert Python function into Runnable
cleaner = RunnableLambda(clean_response)


# -----------------------------
# CREATE CHAIN
# -----------------------------

chain = prompt | model | parser | cleaner


# -----------------------------
# RUN
# -----------------------------

result = chain.invoke({
    "topic": "JWT"
})


print("FINAL RESULT:")
print(result)

print("\nRESULT TYPE:")
print(type(result))