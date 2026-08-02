import os

from dotenv import load_dotenv

from agents.researcher import researcher
from agents.writer import writer


# Load environment variables
load_dotenv()


# Get API key
api_key = os.getenv("AI_API_KEY")


# Validate API key
if api_key is None:
    raise ValueError("AI_API_KEY is missing")


print("API key loaded successfully")


# User topic
topic = "Agentic AI"


# Research
research_result = researcher(topic)


# Writing
article = writer(research_result)


print("\nFinal Article:")
print(article)