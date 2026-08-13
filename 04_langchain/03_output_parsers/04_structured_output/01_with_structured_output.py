from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field


load_dotenv()


# -----------------------------------
# Pydantic Schema
# -----------------------------------

class Answer(BaseModel):

    answer: str = Field(
        description="The answer to the user's question"
    )

    difficulty: str = Field(
        description="Difficulty level of the explanation"
    )


# -----------------------------------
# Chat Model
# -----------------------------------

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)


# -----------------------------------
# Structured Output Model
# -----------------------------------

structured_model = model.with_structured_output(
    Answer,
    include_raw=True
)


print("STRUCTURED MODEL:")
print(structured_model)


# -----------------------------------
# Invoke Model
# -----------------------------------

result = structured_model.invoke(
    "Explain JWT in simple language."
)


# -----------------------------------
# Complete Result
# -----------------------------------

print("\nRESULT:")
print(result)


# -----------------------------------
# Result Type
# -----------------------------------

print("\nRESULT TYPE:")
print(type(result))


# -----------------------------------
# Raw Response
# -----------------------------------

print("\nRAW RESPONSE:")
print(result["raw"])


print("\nRAW RESPONSE TYPE:")
print(type(result["raw"]))


# -----------------------------------
# Parsed Response
# -----------------------------------

print("\nPARSED RESPONSE:")
print(result["parsed"])


print("\nPARSED RESPONSE TYPE:")
print(type(result["parsed"]))


# -----------------------------------
# Parsed Fields
# -----------------------------------

print("\nANSWER:")
print(result["parsed"].answer)


print("\nDIFFICULTY:")
print(result["parsed"].difficulty)


# -----------------------------------
# Parsing Error
# -----------------------------------

print("\nPARSING ERROR:")
print(result["parsing_error"])