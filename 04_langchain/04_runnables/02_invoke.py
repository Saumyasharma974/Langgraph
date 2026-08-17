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


# -----------------------------------
# PROMPT INVOKE
# -----------------------------------

prompt_result = prompt.invoke({
    "topic": "JWT"
})

print("PROMPT OUTPUT:")
print(prompt_result)

print("\nPROMPT OUTPUT TYPE:")
print(type(prompt_result))


# -----------------------------------
# MODEL INVOKE
# -----------------------------------

model_result = model.invoke(prompt_result)

print("\nMODEL OUTPUT:")
print(model_result)

print("\nMODEL OUTPUT TYPE:")
print(type(model_result))


# -----------------------------------
# PARSER INVOKE
# -----------------------------------

parser_result = parser.invoke(model_result)

print("\nPARSER OUTPUT:")
print(parser_result)

print("\nPARSER OUTPUT TYPE:")
print(type(parser_result))