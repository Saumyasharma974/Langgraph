from pydantic import BaseModel, Field
from typing import Literal

class InterviewFeedback(BaseModel):

    score: int = Field(
        ge=1,
        le=10,
        description="Score between 1 and 10"
    )

    correct: bool

    strengths: list[str]

    weaknesses: list[str]

    improvement: str

    next_action: Literal[
        "follow_up",
        "new_question",
        "finish"
    ]
