import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing")

topic=input('Enter your Topic')

llm=ChatGroq(model_name="llama-3.1-8b-instant",api_key=api_key)

prompt1=f"""gGiven the {topic}, generate 5 important points that should be covered when explaining this topic to a beginner."""
points=llm.invoke(prompt1)
print(points.content)

prompt2=f"""Please expand each of these points into a short paragraph:

{points.content}

Focus on clarity and simplicity, suitable for someone who is new to the topic."""
response2=llm.invoke(prompt2)


response3=response2.content
prompt3=f"""{response3}.Review the explanation for clarity, remove unnecessary repetition, and produce a final polished version for a beginner."""

response4=llm.invoke(prompt3)
print(response4.content)
