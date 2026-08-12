from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)


# ==========================================
# STYLE 1: Tuple Syntax
# ==========================================

prompt_tuple = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant."
    ),
    (
        "placeholder",
        "{history}"
    ),
    (
        "human",
        "{question}"
    )
])


print("STYLE 1 - TUPLE")
print(prompt_tuple)
print()


# ==========================================
# STYLE 2: Explicit MessagesPlaceholder
# ==========================================

prompt_class = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant."
    ),
    MessagesPlaceholder(
        variable_name="history"
    ),
    (
        "human",
        "{question}"
    )
])


print("STYLE 2 - EXPLICIT CLASS")
print(prompt_class)