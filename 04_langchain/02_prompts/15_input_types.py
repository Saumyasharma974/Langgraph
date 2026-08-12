from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)


# ---------------------------------------
# Create ChatPromptTemplate
# ---------------------------------------

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    
    MessagesPlaceholder("history"),
    
    ("human", "{question}")
])


# ---------------------------------------
# Inspect prompt
# ---------------------------------------

print("INPUT VARIABLES:")
print(prompt.input_variables)

print("\nOPTIONAL VARIABLES:")
print(prompt.optional_variables)

print("\nINPUT TYPES:")
print(prompt.input_types)


# ---------------------------------------
# Conversation history
# ---------------------------------------

history = [
    HumanMessage(content="My name is Saumya."),
    AIMessage(content="Nice to meet you, Saumya.")
]


# ---------------------------------------
# Invoke prompt
# ---------------------------------------

messages = prompt.invoke({
    "history": history,
    "question": "What is my name?"
})


# ---------------------------------------
# Final messages
# ---------------------------------------

print("\nFINAL PROMPT:")
print(messages)


# ---------------------------------------
# Message types
# ---------------------------------------

print("\nMESSAGE TYPES:")

for message in messages.messages:
    print(type(message))