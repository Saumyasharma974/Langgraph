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
# PIPE OPERATOR
# -----------------------------------

chain = prompt | model | parser


print("CHAIN:")
print(chain)


print("\nCHAIN TYPE:")
print(type(chain))


# -----------------------------------
# INVOKE
# -----------------------------------

result = chain.invoke({
    "topic": "JWT"
})


print("\nRESULT:")
print(result)


print("\nRESULT TYPE:")
print(type(result))