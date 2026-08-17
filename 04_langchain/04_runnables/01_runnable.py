from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


# -----------------------------------
# MODEL
# -----------------------------------

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)


# -----------------------------------
# PROMPT
# -----------------------------------

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


# -----------------------------------
# PARSER
# -----------------------------------

parser = StrOutputParser()


# -----------------------------------
# CHECK TYPES
# -----------------------------------

print("PROMPT TYPE:")
print(type(prompt))

print("\nMODEL TYPE:")
print(type(model))

print("\nPARSER TYPE:")
print(type(parser))


# -----------------------------------
# CHECK INVOKE
# -----------------------------------

print("\nPROMPT HAS INVOKE:")
print(hasattr(prompt, "invoke"))

print("\nMODEL HAS INVOKE:")
print(hasattr(model, "invoke"))

print("\nPARSER HAS INVOKE:")
print(hasattr(parser, "invoke"))