from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate(
    [
        ("human", "Explain {topic} in {language}.")
    ],
    input_variables=["topic"],
    validate_template=True
)

print(prompt)