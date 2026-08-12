from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate(
    [
        ("human", "Explain {topic}.")
    ],
    input_types={
        "topic": str
    }
)


print("INPUT VARIABLES:")
print(prompt.input_variables)

print("\nINPUT TYPES:")
print(prompt.input_types)


messages = prompt.invoke({
    "topic": "JWT"
})

print("\nFINAL MESSAGES:")
print(messages)