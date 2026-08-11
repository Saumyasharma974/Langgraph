# from langchain_core.prompts import ChatPromptTemplate


# prompt = ChatPromptTemplate.from_messages([
#     ("human", "Explain {topic}")
# ])


# messages = prompt.invoke({
#     "topic": "JWT",
#     "topic":"nodemon"
# })


# print(messages)


from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    (
       "system",
       "You are an expert {role}."
    ),
    (
        "human",
        "Explain {topic} in {language} for a {level} student."
    )
])


messages = prompt.invoke({
    "role": "Python teacher",
    "topic": "JWT",
    "language": "English",
    "level": "beginner"
})


print(messages)