from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    (
        "human",
        "Explain {topic} in {language}."
    )
])


print("Required variables:")
print(prompt.input_variables)


print("\nCreating messages...")


messages = prompt.invoke({
    "topic": "JWT",
    "language": "English",
     "level": "beginner"
})

print(messages)