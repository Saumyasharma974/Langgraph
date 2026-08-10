from langchain_core.messages import SystemMessage
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

api_key=os.getenv('GROQ_API_KEY')

if not api_key:
    raise ValueError("Groq API key not found in environment variables")

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0
)

messages=[
    SystemMessage("""
Role:
You are an experienced science teacher.

Audience:
You are teaching a Class 10 student who already knows basic Class 8 concepts of reproduction.

Task:
Explain reproduction in females in a simple and educational way.

Context:
The student has basic knowledge of reproduction from Class 8 but needs a Class 10 level explanation.

Requirements:
- Explain the topic step by step.
- Use simple language suitable for a Class 10 student.
- Explain important scientific terms when they are introduced.
- Use bullet points where appropriate.
- Include a simple text-based diagram where useful.
- Include a simple flowchart to explain the process.
- Clearly explain the role of the major female reproductive organs.
- Explain the overall process in a logical sequence.

Constraints:
- Do not use unnecessarily complex terminology.
- Do not include irrelevant information.
- Do not make up scientific facts.
- If something is uncertain, clearly say so instead of guessing.
- Keep the explanation educational and age-appropriate.
- Do not use slang.

Output Format:
1. Introduction
2. Main female reproductive organs
3. Functions of each organ
4. Step-by-step explanation of the reproductive process
5. Simple text-based diagram
6. Simple flowchart
7. Key points to remember
8. Short summary
"""),
HumanMessage(content="""
Explain reproduction in females.
I want to understand the topic step by step.
""")
]
response=llm.stream(messages)
final_response=""
for chunk in response:
    print(chunk.content,end='',flush=True)
    final_response+=chunk.content

print(final_response)



