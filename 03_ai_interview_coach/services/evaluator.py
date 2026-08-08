from services.llm import structured_llm
from models.feedback import InterviewFeedback

def evaluate_answer(
    interview_type: str,
    question: str,
    answer: str
) -> InterviewFeedback:

    evaluation_prompt = f"""

You are an expert technical interviewer.

Interview Type:
{interview_type}

Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer.

Give a score from 1 to 10.

Determine whether the answer is technically correct.

Identify:

1. Strengths
2. Weaknesses
3. Improvement

Choose next_action:

follow_up:
Use this when the candidate needs
a follow-up question.

new_question:
Use this when the candidate performed
well enough for a new question.

finish:
Use this when the interview should end.

Be fair and technically accurate.

"""

    feedback = structured_llm.invoke(
        evaluation_prompt
    )

    return feedback
