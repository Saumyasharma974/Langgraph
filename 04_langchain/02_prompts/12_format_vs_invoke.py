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


data = {
    "role": "programming teacher",
    "topic": "JWT"
}


# ==========================================
# 1. format()
# ==========================================

formatted = prompt.format(**data)

print("FORMAT:")
print(formatted)

print("\nFORMAT TYPE:")
print(type(formatted))


# ==========================================
# 2. format_messages()
# ==========================================

formatted_messages = prompt.format_messages(**data)

print("\nFORMAT_MESSAGES:")
print(formatted_messages)

print("\nFORMAT_MESSAGES TYPE:")
print(type(formatted_messages))


# ==========================================
# 3. invoke()
# ==========================================

result = prompt.invoke(data)

print("\nINVOKE:")
print(result)

print("\nINVOKE TYPE:")
print(type(result))

print("\nMESSAGES INSIDE CHAT PROMPT VALUE:")
print(result.messages)

print("\nMESSAGE TYPES:")

for message in result.messages:
    print(type(message))