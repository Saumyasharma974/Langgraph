from langchain_core.prompts import HumanMessagePromptTemplate


template = HumanMessagePromptTemplate.from_template(
    "Explain {topic} in {language}."
)


print("TEMPLATE:")
print(template)


print("\nINPUT VARIABLES:")
print(template.input_variables)

message = template.format(
    topic="JWT",
    language="English"
)

print("\nFORMATTED MESSAGE:")
print(message)

print("\nMESSAGE TYPE:")
print(type(message))