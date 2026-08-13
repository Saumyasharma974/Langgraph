from pydantic import BaseModel, Field


class WeekPlan(BaseModel):
    week: int = Field(
        description="Week number"
    )

    focus: str = Field(
        description="Main learning focus for this week"
    )

    tasks: list[str] = Field(
        description="Specific tasks to complete during this week"
    )


class CareerRoadmap(BaseModel):
    target_role: str = Field(
        description="The user's target software development role"
    )

    duration: str = Field(
        description="Total duration of the career roadmap"
    )

    skills: list[str] = Field(
        description="Important skills the user should learn"
    )

    projects: list[str] = Field(
        description="Projects the user should build"
    )

    interview_preparation: list[str] = Field(
        description="Interview preparation activities"
    )

    weekly_plan: list[WeekPlan] = Field(
        description="Detailed weekly learning plan"
    )