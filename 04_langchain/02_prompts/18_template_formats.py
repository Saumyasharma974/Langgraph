# from langchain_core.prompts import ChatPromptTemplate


# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("human", "Explain {topic}.")
#     ],
#     template_format="f-string"
# )


# print("INPUT VARIABLES:")
# print(prompt.input_variables)


# messages = prompt.invoke({
#     "topic": "JWT"
# })


# print("\nMESSAGES:")
# print(messages)



# from langchain_core.prompts import ChatPromptTemplate


# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("human", "Explain {{topic}}.")
#     ],
#     template_format="mustache"
# )


# print("INPUT VARIABLES:")
# print(prompt.input_variables)


# messages = prompt.invoke({
#     "topic": "JWT"
# })


# print("\nMESSAGES:")
# print(messages)



from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "Explain {{ topic }}.")
    ],
    template_format="jinja2"
)


print("INPUT VARIABLES:")
print(prompt.input_variables)


messages = prompt.invoke({
    "topic": "JWT"
})


print("\nMESSAGES:")
print(messages)