from prompt import prompt

from model import (
    model,
    structured_model
)

from memory import (
    add_user_message,
    add_ai_message,
    get_history
)


print("====================================")
print("     AI CAREER ROADMAP GENERATOR")
print("====================================")


# -----------------------------------
# Get Career Profile
# -----------------------------------

current_skills = input("\nCurrent skills: ")
target_role = input("Target role: ")
experience = input("Experience level: ")
daily_time = input("Daily study time: ")
timeline = input("Target timeline: ")


# -----------------------------------
# Create Partial Prompt
# -----------------------------------

career_prompt = prompt.partial(
    current_skills=current_skills,
    target_role=target_role,
    experience=experience,
    daily_time=daily_time,
    timeline=timeline
)


# -----------------------------------
# Debug Information
# -----------------------------------

print("\n====================================")
print("        PROMPT INFORMATION")
print("====================================")

print("\nINPUT VARIABLES:")
print(career_prompt.input_variables)

print("\nOPTIONAL VARIABLES:")
print(career_prompt.optional_variables)

print("\nPARTIAL VARIABLES:")
print(career_prompt.partial_variables)


# ===================================
# FIRST REQUEST
# ===================================

question = "Create my personalized career roadmap."


# -----------------------------------
# Get History
# -----------------------------------

history = get_history()


# -----------------------------------
# Create Prompt
# -----------------------------------

result = career_prompt.invoke({
    "question": question,
    "history": history
})


print("\n====================================")
print("          FINAL PROMPT")
print("====================================")

print(result)


# -----------------------------------
# Structured Model
# -----------------------------------

roadmap = structured_model.invoke(result)


# -----------------------------------
# Display Roadmap
# -----------------------------------

print("\n====================================")
print("        YOUR CAREER ROADMAP")
print("====================================")


print("\nTARGET ROLE:")
print(roadmap.target_role)


print("\nDURATION:")
print(roadmap.duration)


print("\nSKILLS TO LEARN:")

for skill in roadmap.skills:
    print(f"- {skill}")


print("\nPROJECTS:")

for project in roadmap.projects:
    print(f"- {project}")


print("\nINTERVIEW PREPARATION:")

for item in roadmap.interview_preparation:
    print(f"- {item}")


print("\nWEEKLY PLAN:")

for week in roadmap.weekly_plan:

    print(f"\nWeek {week.week}")

    print(f"Focus: {week.focus}")

    print("Tasks:")

    for task in week.tasks:
        print(f"- {task}")


# -----------------------------------
# Save First Conversation
# -----------------------------------

add_user_message(question)


# Save a readable version of roadmap
roadmap_text = f"""
Target Role: {roadmap.target_role}

Duration: {roadmap.duration}

Skills:
{chr(10).join(f"- {skill}" for skill in roadmap.skills)}

Projects:
{chr(10).join(f"- {project}" for project in roadmap.projects)}

Interview Preparation:
{chr(10).join(f"- {item}" for item in roadmap.interview_preparation)}

Weekly Plan:
{
    chr(10).join(
        f"Week {week.week}: {week.focus}\n"
        + chr(10).join(f"  - {task}" for task in week.tasks)
        for week in roadmap.weekly_plan
    )
}
"""


add_ai_message(roadmap_text)


# ===================================
# FOLLOW-UP CONVERSATION
# ===================================

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:

        print("\nGoodbye! 👋")

        break


    # -----------------------------------
    # Get Previous Conversation
    # -----------------------------------

    history = get_history()


    # -----------------------------------
    # Create Prompt
    # -----------------------------------

    result = career_prompt.invoke({
        "question": question,
        "history": history
    })


    # -----------------------------------
    # Normal Model for Follow-up
    # -----------------------------------

    response = model.invoke(result)


    print("\nAI:")
    print(response.content)


    # -----------------------------------
    # Save Conversation
    # -----------------------------------

    add_user_message(question)

    add_ai_message(response.content)