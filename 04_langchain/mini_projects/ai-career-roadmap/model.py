from dotenv import load_dotenv
from langchain_groq import ChatGroq

from schema import CareerRoadmap


load_dotenv()


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)


structured_model = model.with_structured_output(
    CareerRoadmap
)