from langchain_core.prompts import ChatPromptTemplate


def get_role():
    print("FUNCTION CALLED")
    return "programming teacher"


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


partial_prompt = prompt.partial(
    role=get_role
)


print("PARTIAL VARIABLES:")
print(partial_prompt.partial_variables)


print("\nINPUT VARIABLES:")
print(partial_prompt.input_variables)

print("\nINVOKING PROMPT...")

messages = partial_prompt.invoke({
    "topic": "JWT"
})

print("\nFINAL MESSAGES:")
print(messages)