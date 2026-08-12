from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a {role}."
    ),
    (
        "human",
        "Explain {topic}."
    )
])


print("ORIGINAL INPUT VARIABLES:")
print(prompt.input_variables)


partial_prompt = prompt.partial(
    role="programming teacher"
)


print("\nPARTIAL INPUT VARIABLES:")
print(partial_prompt.input_variables)


print("\nPARTIAL VARIABLES:")
print(partial_prompt.partial_variables)


messages = partial_prompt.invoke({
    "topic": "JWT"
})


print("\nFINAL MESSAGES:")
print(messages)