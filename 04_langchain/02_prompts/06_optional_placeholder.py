from numpy.lib import _histograms_impl
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant."
    ),
    MessagesPlaceholder(
        variable_name="history",
        optional=True
    ),
    (
        "human",
        "{question}"
    )
])
history = [
    HumanMessage(content="My name is Saumya."),
    AIMessage(content="Nice to meet you, Saumya.")
]


print("Input variables:")
print(prompt.input_variables)

print("\nOptional variables:")
print(prompt.optional_variables)


messages = prompt.invoke({
    "history":history,
    "question": "What is JWT?"
})


print("\nMessages:")
print(messages)