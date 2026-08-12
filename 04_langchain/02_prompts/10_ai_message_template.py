from langchain_core.prompts import AIMessagePromptTemplate


template = AIMessagePromptTemplate.from_template(
    "The answer is: {answer}"
)


print("TEMPLATE:")
print(template)


print("\nINPUT VARIABLES:")
print(template.input_variables)

message = template.format(
    answer="JWT is used for authentication."
)


print("\nFORMATTED MESSAGE:")
print(message)


print("\nMESSAGE TYPE:")
print(type(message))