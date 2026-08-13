from langchain_core.messages import HumanMessage, AIMessage


history = []


def add_user_message(message):
    history.append(
        HumanMessage(content=message)
    )


def add_ai_message(message):
    history.append(
        AIMessage(content=message)
    )


def get_history():
    return history