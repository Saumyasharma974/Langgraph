from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


load_dotenv()


# -----------------------------------
# MODEL
# -----------------------------------

model = ChatGroq(
    model="openai/gpt-oss-120b",
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
# CREATE SEQUENCE
# -----------------------------------

chain = RunnableSequence(
    prompt,
    model,
    parser
)


print("CHAIN:")
print(chain)


print("\nCHAIN TYPE:")
print(type(chain))


# -----------------------------------
# INVOKE SEQUENCE
# -----------------------------------

result = chain.invoke({
    "topic": "JWT"
})


print("\nRESULT:")
print(result)


print("\nRESULT TYPE:")
print(type(result))