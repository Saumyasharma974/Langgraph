from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)


system_template = SystemMessagePromptTemplate.from_template(
    "You are a {role}"
)

human_template = HumanMessagePromptTemplate.from_template(
    "Explain {topic}."
)

ai_template = AIMessagePromptTemplate.from_template(
    "{answer}"
)

prompt = ChatPromptTemplate.from_messages([
    system_template,
    human_template,
    ai_template
])

print("CHAT PROMPT:")
print(prompt)

print("\nINPUT VARIABLES:")
print(prompt.input_variables)

messages = prompt.invoke({
    "role":"programming teacher",
    "topic": "JWT",
    "answer": "JWT is a token used for authentication."
})

print("\nFINAL MESSAGES:")
print(messages)

print("\nMESSAGE TYPES:")

for message in messages.messages:
    print(type(message))