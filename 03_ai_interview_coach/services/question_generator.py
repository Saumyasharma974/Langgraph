from langchain_core.messages import HumanMessage
from services.llm import llm
from models.feedback import InterviewFeedback

def generate_first_question(interview_type: str, conversation_history: list):
    messages = conversation_history + [
        HumanMessage(
            content=(
                f"Start a {interview_type} interview. "
                f"Generate one medium-difficulty "
                f"{interview_type} interview question. "
                f"Do not provide the answer."
            )
        )
    ]

    response = llm.invoke(messages)
    return response.content

def generate_next_question(
    interview_type: str,
    conversation_history: list,
    previous_feedback: InterviewFeedback
):
    if previous_feedback.score < 5:
        difficulty = "slightly easier"
    elif previous_feedback.score <= 7:
        difficulty = "similar difficulty"
    else:
        difficulty = "slightly harder"

    messages = conversation_history + [
        HumanMessage(
            content=(
                f"Continue the {interview_type} interview.\n\n"
                f"The candidate's previous score was "
                f"{previous_feedback.score}/10.\n\n"
                f"The candidate's previous weaknesses were:\n"
                f"{', '.join(previous_feedback.weaknesses)}\n\n"
                f"Generate exactly one new {difficulty} "
                f"interview question.\n\n"
                f"Do not provide the answer."
            )
        )
    ]

    response = llm.invoke(messages)
    return response.content
