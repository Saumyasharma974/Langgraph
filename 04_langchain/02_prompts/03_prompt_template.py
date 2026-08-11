from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language."
)


result = prompt.invoke({
    "topic": "JWT"
})


print(result)
print(type(result))

print("\nACTUAL TEXT:")
print(result.text)