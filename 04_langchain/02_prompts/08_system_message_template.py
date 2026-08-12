from langchain_core.prompts import SystemMessagePromptTemplate


template = SystemMessagePromptTemplate.from_template(
    "You are an expert {role}."
)


print("TEMPLATE:")
print(template)


print("\nINPUT VARIABLES:")
print(template.input_variables)

message = template.format(
    role="Python teacher"
)

print("\nFORMATTED MESSAGE:")
print(message)

print("\nMESSAGE TYPE:")
print(type(message))