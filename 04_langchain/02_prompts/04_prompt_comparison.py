from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate
)


# ==============================
# PromptTemplate
# ==============================

text_prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language."
)

text_result = text_prompt.invoke({
    "topic": "JWT"
})

print("PROMPT TEMPLATE")
print(text_result)
print(type(text_result))
print(text_result.text)


# ==============================
# ChatPromptTemplate
# ==============================

chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a programming teacher."
    ),
    (
        "human",
        "Explain {topic} in simple language."
    )
])

chat_result = chat_prompt.invoke({
    "topic": "JWT"
})

print("\nCHAT PROMPT TEMPLATE")
print(chat_result)
print(type(chat_result))
print(chat_result.messages)
