import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage


# ==========================================
# 1. Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


# ==========================================
# 2. Create Groq LLM
# ==========================================

llm = ChatGroq(
    api_key=api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0
)


# ==========================================
# 3. System Prompt
# ==========================================

system_prompt = """
Role:
You are an experienced AI Engineering mentor.

Context:
- I am a B.Tech graduate in Computer Science and Engineering.
- I am currently learning Agentic AI.
- I can dedicate 2-3 hours every day for hands-on development.
- I want to learn by building practical projects.
- I already know basic Python and LangChain concepts.

Task:
Design a simple Agentic AI content-generation system
that can generate approximately 1000 words of
high-quality content on a given topic.

The target is to optimize the system for a fast response,
ideally within approximately 2 minutes.
Do not claim that the response time can be guaranteed.

Requirements:
- Explain the proposed architecture.
- Explain the responsibility of each component.
- Explain the complete workflow.
- Recommend a suitable Groq model.
- Use Python and LangChain in the implementation approach.
- Explain how the system can generate high-quality content.
- Explain how the system can improve or review generated content.
- Consider latency and performance.
- Keep the solution suitable for a beginner learning Agentic AI.

Constraints:
- Use Python only.
- Use Groq as the only LLM provider.
- Use LangChain where appropriate.
- Keep the architecture simple.
- Do not add unnecessary libraries or technologies.
- Do not use NLTK or spaCy unless they are genuinely required.
- Do not use Flask or React unless they are genuinely required.
- Do not invent APIs, functions, libraries, or model names.
- Use the current LangChain ChatGroq approach.
- Use llm.invoke() for LLM calls.
- Clearly mention any assumptions.
- Do not guarantee a fixed response time.

Output Format:
1. Problem Understanding
2. Proposed Architecture
3. Components
4. Workflow
5. Technologies and Libraries
6. Implementation Approach
7. Project Structure
8. Example Code
9. Performance Considerations
10. Possible Improvements
"""


# ==========================================
# 4. Messages
# ==========================================

messages = [
    SystemMessage(
        content=system_prompt
    ),

    HumanMessage(
        content=(
            "Design the system according to the "
            "context, requirements, and constraints above."
        )
    )
]


# ==========================================
# 5. Call LLM
# ==========================================

response = llm.invoke(messages)


# ==========================================
# 6. Print Response
# ==========================================

print("\n========================================")
print("              AI RESPONSE")
print("========================================\n")

print(response.content)