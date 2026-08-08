from langchain_groq import ChatGroq
from config import GROQ_API_KEY
from models.feedback import InterviewFeedback

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0
)

structured_llm = llm.with_structured_output(
    InterviewFeedback
)
